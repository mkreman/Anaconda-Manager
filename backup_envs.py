import os


os.system('title Backing up Anaconda Envs')
os.system('cls')
os.system('conda deactivate')


class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def backup_env(path, env):
    print(f"{Colors.OKBLUE}Storing packages of {env}'s environment in the directory: {path}{Colors.ENDC}")
    os.system(f"""conda activate {env} & cd "{path}" & conda list --explicit > {env + '_requirement.txt'}""")
    print(f"{Colors.OKBLUE}{env + '_requirement.txt'} is exported to {path}{Colors.ENDC}")


print(f"""{Colors.HEADER}========================================
Welcome to Anaconda Manager Application!
========================================{Colors.ENDC}
""")

stream = os.popen("where python")
anaconda_path = stream.read().split('\n')[0][:-10]

print(f"""{Colors.OKBLUE}Your Anaconda is located at the following path{Colors.ENDC}""")
print(f"{Colors.OKCYAN}{anaconda_path}{Colors.ENDC}")

print(f"""\n{Colors.OKBLUE}Please wait checking for your Anaconda Environments
---------------------------------------------------{Colors.ENDC}""")
envs = os.popen("conda env list").read().strip().split('\n')[2:]

print(f"""\n{Colors.OKBLUE}Following are your Anaconda Environments
----------------------------------------{Colors.ENDC}""")
[print(f"{Colors.OKCYAN}{i + 1}, {env.replace('*', ' ')}{Colors.ENDC}") for i, env in enumerate(envs)]

for env in envs:
    env_name = env.split()[0]
    print(f"""{Colors.WARNING}{"-" * len(f"{env_name} is selected")}\n{env_name} is selected{Colors.ENDC}""")
    backup_env("C:\\Users\\MkReman\\My Drive\\Python\\Files\\EnvBackupFiles", env_name)
