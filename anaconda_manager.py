import os
import sys


os.system('title Anaconda Manager')
os.system('cls')
os.system('conda deactivate')


class Colors:
    HEADER = '\033[95m'
    MESSAGE = '\033[94m'
    OKCYAN = '\033[96m'
    QUESTION = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def ask_env_name():
    name = input(f"{Colors.QUESTION}Enter the name of environment: {Colors.ENDC}")
    while True:
        if name == 'b':
            return False
        elif name.find('/') == -1 and name.find(' ') == -1 and name.find(':') == -1 and\
                name.find('#') == -1:
            return name
        else:
            print(f"{Colors.WARNING}Env name '{name}' is invalid, Characters not allowed: ('/', ' ', ':', '#')\n"
                  f"{Colors.ENDC}")
            name = input(f"{Colors.QUESTION}Enter the name of environment: {Colors.ENDC}")


def ask_requirement_path():
    text_path = input(f"{Colors.QUESTION}Enter the path where requirement text file is stored: {Colors.ENDC}")
    while True:
        if text_path == 'b':
            return False
        elif os.path.exists(text_path):
            return text_path
        else:
            print(f"{Colors.WARNING}File path '{text_path}' does not exits!{Colors.ENDC}")
            text_path = input(f"{Colors.QUESTION}Enter the path where requirement text file is stored: {Colors.ENDC}")


def ask_env_index(length):
    index = input(f"""\n{Colors.QUESTION}Select the Environment by typing the respective index number: {Colors.ENDC}""")
    while True:
        if index == 'b':
            return False
        elif index.isnumeric() and 0 < int(index) <= length:
            return int(index)
        else:
            print(f"{Colors.WARNING}Invalid response!{Colors.ENDC}")
            index = input(f"""\n{Colors.QUESTION}Select the Environment by typing the respective index number: {Colors.ENDC}""")


def ask_path():
    path = input(f"{Colors.QUESTION}Enter the path where you want to store text file: {Colors.ENDC}")
    while True:
        if path == 'b':
            return False
        elif os.path.exists(path):
            return path
        else:
            print(f"{Colors.WARNING}Path '{path}' does not exits!{Colors.ENDC}")
            path = input(f"{Colors.QUESTION}Enter the path where you want to store text file: {Colors.ENDC}")


def ask_response(length):
    response = input(f"{Colors.QUESTION}Select the index of the operation: {Colors.ENDC}")
    while True:
        if response == 'b':
            return False
        elif not response.isnumeric() or int(response) > length or int(response) < 1:
            print(f"{Colors.WARNING}Invalid Response!")
            response = input(f"{Colors.QUESTION}Select the index of the operation: {Colors.ENDC}")
        else:
            return response


print(f"""{Colors.HEADER}===========================================
Welcome to Anaconda Manager Application-2.0!
==========================================={Colors.ENDC}
""")

stream = os.popen("where python")
for path in stream.read().split('\n'):
    if path[-20:] == 'anaconda3\\python.exe':
        anaconda_path = path[:-10]
        print(f"""{Colors.MESSAGE}Your Anaconda is located at the following path{Colors.ENDC}""")
        print(f"{Colors.OKCYAN}{anaconda_path}{Colors.ENDC}")
        break
    else:
        sys.exit(f"{Colors.WARNING}Anaconda is not found in your system{Colors.ENDC}")


options = f"""\n\n{Colors.MESSAGE}================================
Select the operation from below:
--------------------------------{Colors.ENDC}\n"""
option_list = [
    "Take back-up as text file",
    "Create environment from a text file",
    "Create a environment",
    "Install packages into existing environment using text file",
    "Remove env",
    "Rename the environment",
    "Clone an environment",
    "List all packages",
    "List the history of each change to a environment",
    "Restore environment to a previous revision",
    "List of environments",
    "Close"]
for i, option in enumerate(option_list):
    options += f"[{str(i + 1)}] " + option + '\n'
options += f"""\n{Colors.MESSAGE}-----------------------------------
You can type 'b' to go back anytime
-----------------------------------{Colors.ENDC}\n"""

while True:
    print(options)
    response = ask_response(len(option_list))
    if not response:
        break

    elif option_list[int(response) - 1] == "Create a environment":  # 3rd Option
        env_name = ask_env_name()
        if not env_name:
            continue    # If it's 'b' then ask_env_name returns False

        os.system(f"conda create --name {env_name}")
        os.system('pause')

    elif option_list[int(response) - 1] == "Take back-up as text file":
        envs = [env for env in os.listdir(os.path.join(anaconda_path, 'envs')) if os.path.isdir(os.path.join(os.path.join(anaconda_path, 'envs'), env))]
        print(f"""\n{Colors.MESSAGE}Select env from followings
--------------------------{Colors.ENDC}""")
        [print(f"{Colors.OKCYAN}{i + 1}) {env}{Colors.ENDC}") for i, env in enumerate(envs)]

        env_index = ask_env_index(len(envs))
        if not env_index:
            continue
        env_name = envs[int(int(env_index)) - 1].split()[0]
        print(f"""{Colors.WARNING}{"-" * len(f"{env_index}th environment {env_name} is selected")}
{env_index}th environment {env_name} is selected{Colors.ENDC}""")

        path = ask_path()
        if not path:
            continue

        print(f"{Colors.MESSAGE}Storing packages of {env_name}'s environment in the directory: {path}{Colors.ENDC}")
        os.system(f"""conda activate {env_name} & cd "{path}" & conda list --explicit > {env_name + '_requirement.txt'}""")
        print(f"{Colors.MESSAGE}{env_name + '_requirement.txt'} is exported to {path}{Colors.ENDC}")
        os.system('pause')

    elif option_list[int(response) - 1] == "Create environment from a text file":
        requirement_path = ask_requirement_path()
        if not requirement_path:
            continue

        env_name = ask_env_name()
        if not env_name:
            continue  # If it's 'b' then ask_env_name returns False

        path = '\\'.join(requirement_path.split('\\')[:-1])
        file_name = requirement_path.split('\\')[-1]
        print(f"""{Colors.MESSAGE}\n{'-' * len(f"Creating {env_name} env using {file_name} file")}
        Creating {env_name} env using {file_name} file{Colors.ENDC}""")
        os.system(f"""cd "{path}" & conda create --name {env_name} --file {file_name}""")
        os.system(f"cd {os.path.expanduser('~')}")
        print(f"{Colors.MESSAGE}{env_name} env created!{Colors.ENDC}")
        os.system('pause')

    elif option_list[int(response) - 1] == "Install packages into existing environment using text file":
        envs = [env for env in os.listdir(os.path.join(anaconda_path, 'envs')) if os.path.isdir(os.path.join(os.path.join(anaconda_path, 'envs'), env))]

        print(f"""\n{Colors.MESSAGE}Select env from followings
--------------------------{Colors.ENDC}""")
        [print(f"{Colors.OKCYAN}{i + 1}) {env}{Colors.ENDC}") for i, env in enumerate(envs)]

        env_index = ask_env_index(len(envs))
        if not env_index:
            continue
        env_name = envs[int(env_index) - 1].split()[0]
        print(f"""{Colors.WARNING}{"-" * len(f"{env_index}th environment {env_name} is selected")}
{env_index}th environment {env_name} is selected{Colors.ENDC}""")

        requirement_path = ask_requirement_path()
        if not requirement_path:
            continue

        path = '\\'.join(requirement_path.split('\\')[:-1])
        file_name = requirement_path.split('\\')[-1]
        print(f"""{Colors.MESSAGE}\n{'-'*len(f"Installing packages into {env_name} env listed in {file_name} file")}
Installing packages into {env_name} env listed in {file_name} file{Colors.ENDC}""")
        os.system(f"""cd "{path}" & conda install --name {env_name} --file {file_name}""")
        os.system(f"cd {os.path.expanduser('~')}")
        print(f"{Colors.MESSAGE}Packages installed on {env_name}!{Colors.ENDC}")
        os.system('pause')

    elif option_list[int(response) - 1] == "Remove env":
        envs = [env for env in os.listdir(os.path.join(anaconda_path, 'envs')) if os.path.isdir(os.path.join(os.path.join(anaconda_path, 'envs'), env))]

        print(f"""\n{Colors.MESSAGE}Select env from followings
--------------------------{Colors.ENDC}""")
        [print(f"{Colors.OKCYAN}{i + 1}) {env}{Colors.ENDC}") for i, env in enumerate(envs)]

        env_index = ask_env_index(len(envs))
        if not env_index:
            continue
        env_name = envs[int(env_index) - 1].split()[0]
        print(f"""{Colors.WARNING}{"-" * len(f"{env_index}th environment {env_name} is selected")}
{env_index}th environment {env_name} is selected{Colors.ENDC}""")
        conformation = input(f"{Colors.WARNING}Are you sure, you want to remove {env_name} env [y/n]: {Colors.ENDC}")
        while True:
            if conformation.lower() in ['y', 'yes']:
                print(f"""{Colors.MESSAGE}\n{'-' * len(f'Removing env {env_name}')}\nRemoving env {env_name}{Colors.ENDC}""")
                os.system(f"conda deactivate & conda env remove --name {env_name}")
                print(f"{Colors.MESSAGE}Removed all packages in environment {env_name}:{Colors.ENDC}")
                break
            elif conformation.lower() in ['n', 'no', 'b']:
                break
            else:
                print(f"{Colors.WARNING}Invalid response!{Colors.ENDC}")
                conformation = input(f"{Colors.WARNING}Are you sure, you want to remove {env_name} [y/n]: {Colors.ENDC}")
        os.system('pause')

    elif option_list[int(response) - 1] == "Rename the environment":
        envs = [env for env in os.listdir(os.path.join(anaconda_path, 'envs')) if os.path.isdir(os.path.join(os.path.join(anaconda_path, 'envs'), env))]

        print(f"""\n{Colors.MESSAGE}Select env from followings
--------------------------{Colors.ENDC}""")
        [print(f"{Colors.OKCYAN}{i + 1}) {env}{Colors.ENDC}") for i, env in enumerate(envs)]

        env_index = ask_env_index(len(envs))
        if not env_index:
            continue
        env_name = envs[int(env_index) - 1].split()[0]
        print(f"""{Colors.WARNING}{"-" * len(f"{env_index}th environment {env_name} is selected")}
{env_index}th environment {env_name} is selected{Colors.ENDC}""")

        new_name = ask_env_name()
        if not new_name:
            continue  # If it's 'b' then ask_env_name returns False
        os.rename(os.path.join(anaconda_path, 'envs', env_name), os.path.join(anaconda_path, 'envs', new_name))
        print(f"{Colors.MESSAGE}Env name {env_name} is changed to {new_name}")
        os.system('pause')

    elif option_list[int(response) - 1] == "Clone an environment":
        envs = [env for env in os.listdir(os.path.join(anaconda_path, 'envs')) if os.path.isdir(os.path.join(os.path.join(anaconda_path, 'envs'), env))]

        print(f"""\n{Colors.MESSAGE}Select env from followings
--------------------------{Colors.ENDC}""")
        [print(f"{Colors.OKCYAN}{i + 1}) {env}{Colors.ENDC}") for i, env in enumerate(envs)]

        env_index = ask_env_index(len(envs))
        if not env_index:
            continue
        env_name = envs[env_index - 1].split()[0]
        print(f"""{Colors.WARNING}{"-" * len(f"{env_index}th environment {env_name} is selected")}
{env_index}th environment {env_name} is selected{Colors.ENDC}""")
        print(f"""{Colors.QUESTION}\n-------------------------------{Colors.ENDC}""")

        new_env_name = ask_env_name()
        if not new_env_name:
            continue
        os.system(f"conda create --clone {env_name} --name {new_env_name}")
        os.system('pause')

    elif option_list[int(response) - 1] == "List all packages":
        envs = [env for env in os.listdir(os.path.join(anaconda_path, 'envs')) if os.path.isdir(os.path.join(os.path.join(anaconda_path, 'envs'), env))]

        print(f"""\n{Colors.MESSAGE}Select env from followings
--------------------------{Colors.ENDC}""")
        [print(f"{Colors.OKCYAN}{i + 1}) {env}{Colors.ENDC}") for i, env in enumerate(envs)]

        env_index = ask_env_index(len(envs))
        if not env_index:
            continue
        env_name = envs[env_index - 1].split()[0]
        print("\n---------------------------------------------------------------------------")
        os.system(f"conda list -n {env_name}")
        os.system('pause')

    elif option_list[int(response) - 1] == "List the history of each change to a environment":
        envs = [env for env in os.listdir(os.path.join(anaconda_path, 'envs')) if os.path.isdir(os.path.join(os.path.join(anaconda_path, 'envs'), env))]

        print(f"""\n{Colors.MESSAGE}Select env from followings
--------------------------{Colors.ENDC}""")
        [print(f"{Colors.OKCYAN}{i + 1}) {env}{Colors.ENDC}") for i, env in enumerate(envs)]

        env_index = ask_env_index(len(envs))
        if not env_index:
            continue
        env_name = envs[env_index - 1].split()[0]
        os.system(f"conda activate {env_name} & conda list --revisions")
        os.system("conda deactivate")
        os.system('pause')

    elif option_list[int(response) - 1] == "Restore environment to a previous revision":
        envs = [env for env in os.listdir(os.path.join(anaconda_path, 'envs')) if os.path.isdir(os.path.join(os.path.join(anaconda_path, 'envs'), env))]

        print(f"""\n{Colors.MESSAGE}Select env from followings
--------------------------{Colors.ENDC}""")
        [print(f"{Colors.OKCYAN}{i + 1}) {env}{Colors.ENDC}") for i, env in enumerate(envs)]

        env_index = ask_env_index(len(envs))
        if not env_index:
            continue
        env_name = envs[env_index - 1].split()[0]
        version = input("Enter the revision: ")
        flag = True
        while flag:
            if version == 'b':
                flag = False
            elif version.isnumeric():
                break
            else:
                print(f"{Colors.WARNING}Invalid Version No!{Colors.ENDC}")
        else:
            continue

        os.system(f"conda activate {env_name} & conda install --revision {version}")
        os.system("conda deactivate")
        print(f"""{Colors.MESSAGE}{'-'*len(f"Version {version} is restored of {env_name}")}Version {version} is restored of {env_name}{Colors.ENDC}""")
        os.system('pause')

    elif option_list[int(response) - 1] == "List of environments":
        envs = [env for env in os.listdir(os.path.join(anaconda_path, 'envs')) if os.path.isdir(os.path.join(os.path.join(anaconda_path, 'envs'), env))]

        print(f"""\n{Colors.MESSAGE}Select env from followings
--------------------------{Colors.ENDC}""")
        [print(f"{Colors.OKCYAN}{i + 1}) {env}{Colors.ENDC}") for i, env in enumerate(envs)]
        os.system('pause')

    elif option_list[int(response) - 1] == "Close":
        break
