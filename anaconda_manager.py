import os


os.system('title Anaconda Manager')
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


def create_env(requirement_path, env_name):
    path = '\\'.join(requirement_path.split('\\')[:-1])
    file_name = requirement_path.split('\\')[-1]
    print(f"""{Colors.OKBLUE}\n{'-'*len(f"Creating {env_name} env using {file_name} file")}
Creating {env_name} env using {file_name} file{Colors.ENDC}""")
    os.system(f"""cd "{path}" & conda create --name {env_name} --file {file_name}""")
    os.system(f"cd {os.path.expanduser('~')}")
    print(f"{Colors.OKBLUE}{env_name} env created!{Colors.ENDC}")


def remove_env(env_name):
    print(f"""{Colors.OKBLUE}\n{'-'*len(f'Removing env {env_name}')}
Removing env {env_name}{Colors.ENDC}""")
    os.system(f"conda deactivate & conda env remove --name {env_name}")
    print(f"{Colors.OKBLUE}Removed all packages in environment {env_name}:{Colors.ENDC}")


print(f"""{Colors.HEADER}========================================
Welcome to Anaconda Manager Application!
========================================{Colors.ENDC}
""")

stream = os.popen("where python")
anaconda_path = stream.read().split('\n')[0][:-10]

print(f"""{Colors.OKBLUE}Your Anaconda is located at the following path{Colors.ENDC}""")
print(f"{Colors.OKCYAN}{anaconda_path}{Colors.ENDC}")

options = f"""\n\n{Colors.OKBLUE}================================
Select the operation from below:
--------------------------------{Colors.ENDC}
[1] Take back-up as text file
[2] Create environment from a text file
[3] Remove the environment
[4] Rename the environment
[5] Make exact copy of an environment
[6] List all packages
[7] List the history of each change to the current environment
[8] Restore environment to a previous revision
[9] List of environments
[10] Close"""
print(options)

response = input(f"{Colors.OKGREEN}Select the index of the operation: {Colors.ENDC}")
while True:
    if response == '1':
        print(f"""\n{Colors.OKBLUE}Please wait checking for your Anaconda Environments
---------------------------------------------------{Colors.ENDC}""")
        envs = os.popen("conda env list").read().strip().split('\n')[2:]

        print(f"""\n{Colors.OKBLUE}Following are your Anaconda Environments
----------------------------------------{Colors.ENDC}""")
        [print(f"{Colors.OKCYAN}{i + 1}, {env.replace('*', ' ')}{Colors.ENDC}") for i, env in enumerate(envs)]

        env_index = int(input(f"""\n{Colors.OKGREEN}Select the Environment by typing the respective index number: {Colors.ENDC}"""))
        env_name = envs[env_index - 1].split()[0]
        print(f"""{Colors.WARNING}{"-" * len(f"{env_index}th environment {env_name} is selected")}
{env_index}th environment {env_name} is selected{Colors.ENDC}""")

        path = input(f"{Colors.OKGREEN}Enter the path where you want to store text file: {Colors.ENDC}")
        backup_env(path, env_name)

    elif response == '2':
        requirement_path = input(f"{Colors.OKGREEN}Enter the path where requirement text file is stored: {Colors.ENDC}")
        env_name = input(f"{Colors.OKGREEN}Enter the name of environment: {Colors.ENDC}")
        create_env(requirement_path, env_name)

    elif response == '3':
        print(f"""\n{Colors.OKBLUE}Please wait checking for your Anaconda Environments
---------------------------------------------------{Colors.ENDC}""")
        envs = os.popen("conda env list").read().strip().split('\n')[2:]

        print(f"""\n{Colors.OKBLUE}Following are your Anaconda Environments
----------------------------------------{Colors.ENDC}""")
        [print(f"{Colors.OKCYAN}{i+1}, {env.replace('*', ' ')}{Colors.ENDC}") for i, env in enumerate(envs)]

        env_index = int(input(f"""\n{Colors.OKGREEN}Select the Environment by typing the respective index number: {Colors.ENDC}"""))
        env_name = envs[env_index - 1].split()[0]
        print(f"""{Colors.WARNING}{"-" * len(f"{env_index}th environment {env_name} is selected")}
{env_index}th environment {env_name} is selected{Colors.ENDC}""")
        conformation = input(f"{Colors.WARNING}Are you sure, you want to remove {env_name} env [y/n]: {Colors.ENDC}")
        while True:
            if conformation.lower() in ['y', 'yes']:
                remove_env(env_name)
                break
            elif conformation.lower() in ['n', 'no']:
                break
            else:
                print(f"{Colors.WARNING}Invalid response!{Colors.ENDC}")
                conformation = input(f"{Colors.WARNING}Are you sure, you want to remove {env_name} [y/n]: {Colors.ENDC}")

    elif response == '4':
        print(f"""\n{Colors.OKBLUE}Please wait checking for your Anaconda Environments
---------------------------------------------------{Colors.ENDC}""")
        envs = os.popen("conda env list").read().strip().split('\n')[2:]

        print(f"""\n{Colors.OKBLUE}Following are your Anaconda Environments
----------------------------------------{Colors.ENDC}""")
        [print(f"{Colors.OKCYAN}{i+1}, {env.replace('*', ' ')}{Colors.ENDC}") for i, env in enumerate(envs)]

        env_index = int(input(f"""\n{Colors.OKGREEN}Select the Environment by typing the respective index number: {Colors.ENDC}"""))
        env_name = envs[env_index - 1].split()[0]
        print(f"""{Colors.WARNING}{"-" * len(f"{env_index}th environment {env_name} is selected")}
{env_index}th environment {env_name} is selected{Colors.ENDC}""")
        new_name = input(f"{Colors.OKGREEN}Enter the new name: {Colors.ENDC}")
        os.rename(os.path.join(anaconda_path, 'envs', env_name), os.path.join(anaconda_path, 'envs', new_name))

    elif response == '5':
        print(f"""\n{Colors.OKBLUE}Please wait checking for your Anaconda Environments
---------------------------------------------------{Colors.ENDC}""")
        envs = os.popen("conda env list").read().strip().split('\n')[2:]

        print(f"""\n{Colors.OKBLUE}Following are your Anaconda Environments
----------------------------------------{Colors.ENDC}""")
        [print(f"{Colors.OKCYAN}{i+1}, {env.replace('*', ' ')}{Colors.ENDC}") for i, env in enumerate(envs)]

        env_index = int(input(f"""\n{Colors.OKGREEN}Select the Environment by typing the respective index number: {Colors.ENDC}"""))
        env_name = envs[env_index - 1].split()[0]
        print(f"""{Colors.WARNING}{"-" * len(f"{env_index}th environment {env_name} is selected")}
{env_index}th environment {env_name} is selected{Colors.ENDC}""")
        new_env_name = input(f"""{Colors.OKGREEN}\n-------------------------------\nEnter the name of environment: {Colors.ENDC}""")
        os.system(f"conda create --clone {env_name} --name {new_env_name}")

    elif response == '6':
        print(f"""\n{Colors.OKBLUE}Please wait checking for your Anaconda Environments
---------------------------------------------------{Colors.ENDC}""")
        envs = os.popen("conda env list").read().strip().split('\n')[2:]

        print(f"""\n{Colors.OKBLUE}Following are your Anaconda Environments
----------------------------------------{Colors.ENDC}""")
        [print(f"{Colors.OKCYAN}{i+1}, {env.replace('*', ' ')}{Colors.ENDC}") for i, env in enumerate(envs)]

        env_index = int(input(f"""\n{Colors.OKGREEN}Select the Environment by typing the respective index number: {Colors.ENDC}"""))
        env_name = envs[env_index - 1].split()[0]
        print("\n----------------------------------------------------------------")
        os.system(f"conda activate {env_name} & conda list")
        os.system("conda deactivate")

    elif response == '7':
        print(f"""\n{Colors.OKBLUE}Please wait checking for your Anaconda Environments
---------------------------------------------------{Colors.ENDC}""")
        envs = os.popen("conda env list").read().strip().split('\n')[2:]

        print(f"""\n{Colors.OKBLUE}Following are your Anaconda Environments
----------------------------------------{Colors.ENDC}""")
        [print(f"{Colors.OKCYAN}{i+1}, {env.replace('*', ' ')}{Colors.ENDC}") for i, env in enumerate(envs)]

        env_index = int(input(f"""\n{Colors.OKGREEN}Select the Environment by typing the respective index number: {Colors.ENDC}"""))
        env_name = envs[env_index - 1].split()[0]
        os.system(f"conda activate {env_name} & conda list --revisions")
        os.system("conda deactivate")

    elif response == '8':
        print(f"""\n{Colors.OKBLUE}Please wait checking for your Anaconda Environments
---------------------------------------------------{Colors.ENDC}""")
        envs = os.popen("conda env list").read().strip().split('\n')[2:]

        print(f"""\n{Colors.OKBLUE}Following are your Anaconda Environments
----------------------------------------{Colors.ENDC}""")
        [print(f"{Colors.OKCYAN}{i+1}, {env.replace('*', ' ')}{Colors.ENDC}") for i, env in enumerate(envs)]

        env_index = int(input(f"""\n{Colors.OKGREEN}Select the Environment by typing the respective index number: {Colors.ENDC}"""))
        env_name = envs[env_index - 1].split()[0]
        version = int(input("Enter the revision: "))
        os.system(f"conda activate {env_name} & conda install --revision {version}")
        os.system("conda deactivate")
        print(f"""{Colors.OKBLUE}{'-'*len(f"Version {version} is restored of {env_name}")}Version {version} is restored of {env_name}{Colors.ENDC}""")

    elif response == '9':
        print(f"""\n{Colors.OKBLUE}Please wait checking for your Anaconda Environments
---------------------------------------------------{Colors.ENDC}""")
        envs = os.popen("conda env list").read().strip().split('\n')[2:]

        print(f"""\n{Colors.OKBLUE}Following are your Anaconda Environments
----------------------------------------{Colors.ENDC}""")
        [print(f"{Colors.OKCYAN}{i+1}, {env.replace('*', ' ')}{Colors.ENDC}") for i, env in enumerate(envs)]
    elif response == '10':
        break
    else:
        print(f"{Colors.WARNING}Invalid response!{Colors.ENDC}")
    print(options)
    response = input(f"{Colors.OKGREEN}Select the index of the operation: {Colors.ENDC}")
