import os
import sys
from utils import *
import platform

if platform.system() == 'Windows':
    os.system('title Anaconda Manager')
    os.system('cls')
    os.system('conda deactivate')
elif platform.system() == 'Linux':
    os.system('clear')


print(f"""{Colors.HEADER}============================================
Welcome to Anaconda Manager Application-2.0!
============================================{Colors.ENDC}""")

anaconda_path = get_anaconda_path()

options = f"""\n\n{Colors.MESSAGE}================================
Select the operation from below:
--------------------------------{Colors.ENDC}\n"""
option_list = [
    "Take back-up of an environment",
    "Create environment from a back-up file",
    "Create environment",
    "Install packages into existing environment using a back-up file",
    "Remove environment",
    "Rename environment",
    "Clone environment",
    "List all packages in an environment",
    "List all revision / History of an environment",
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

    elif option_list[int(response) - 1] == "Create environment":  # 3rd Option
        env_name = ask_env_name()
        if not env_name:
            continue    # If it's 'b' then ask_env_name returns False

        os.system(f"conda create --name {env_name}")
        input('Press Enter to continue...:')

    elif option_list[int(response) - 1] == "Take back-up of an evironment":
        # if anaconda_path is not defined then program will stop running according to the else condition in the line
        # anaconda_manager.py:102
        envs = ['base'] + [env for env in os.listdir(os.path.join(anaconda_path, 'envs')) if os.path.isdir(os.path.join(os.path.join(anaconda_path, 'envs'), env))]
        print(f"""\n{Colors.MESSAGE}Select env from followings
--------------------------{Colors.ENDC}""")
        [print(f"{Colors.OKCYAN}{i + 1}) {env}{Colors.ENDC}") for i, env in enumerate(envs)]

        env_index = ask_env_index(len(envs))
        if not env_index:
            continue
        env_name = envs[int(int(env_index)) - 1].split()[0]
        print(f"""{Colors.WARNING}{"-" * len(f"Environment '{env_name}' is selected")}
Environment '{env_name}' is selected{Colors.ENDC}""")

        path = ask_path()
        if not path:
            continue

        print(f"{Colors.MESSAGE}Storing packages of environment '{env_name}' in the directory: '{path}'{Colors.ENDC}")
        os.system(f"""conda activate {env_name} & cd "{path}" & conda env export --no-builds > {env_name + '_requirement.yml'}""")
        print(f"{Colors.MESSAGE}{env_name + '_requirement.txt'} is exported to {path}{Colors.ENDC}")
        input('Press Enter to continue...:')

    elif option_list[int(response) - 1] == "Create environment from a back-up file":
        requirement_path = ask_requirement_path()
        if not requirement_path:
            continue

        env_name = ask_env_name()
        if not env_name:
            continue  # If it's 'b' then ask_env_name returns False

        path = '\\'.join(requirement_path.split('\\')[:-1])
        file_name = requirement_path.split('\\')[-1]
        if file_name.split('.')[-1] != 'yml':
            print(f"""{Colors.WARNING}\n{'-' * len(f"Requirement file should be a 'yml' file")}
Requirement file should be a 'yml' file{Colors.ENDC}""")
            continue

        print(f"""{Colors.MESSAGE}\n{'-' * len(f"Creating {env_name} env using {file_name} file")}
Creating {env_name} env using {file_name} file{Colors.ENDC}""")
        os.system(f"""cd "{path}" & conda env create --name {env_name} --file {file_name}""")
        os.system(f"cd {os.path.expanduser('~')}")
        print(f"{Colors.MESSAGE}{env_name} env created!{Colors.ENDC}")
        input('Press Enter to continue...:')

    elif option_list[int(response) - 1] == "Install packages into existing environment using a back-up file":
        envs = ['base'] + [env for env in os.listdir(os.path.join(anaconda_path, 'envs')) if os.path.isdir(os.path.join(os.path.join(anaconda_path, 'envs'), env))]

        print(f"""\n{Colors.MESSAGE}Select env from followings
--------------------------{Colors.ENDC}""")
        [print(f"{Colors.OKCYAN}{i + 1}) {env}{Colors.ENDC}") for i, env in enumerate(envs)]

        env_index = ask_env_index(len(envs))
        if not env_index:
            continue
        env_name = envs[int(env_index) - 1].split()[0]
        print(f"""{Colors.WARNING}{"-" * len(f"Environment '{env_name}' is selected")}
Environment '{env_name}' is selected{Colors.ENDC}""")

        requirement_path = ask_requirement_path()
        if not requirement_path:
            continue

        path = '\\'.join(requirement_path.split('\\')[:-1])
        file_name = requirement_path.split('\\')[-1]
        print(f"""{Colors.MESSAGE}\n{'-'*len(f"Installing packages into {env_name} env listed in {file_name} file")}
Installing packages into {env_name} env listed in {file_name} file{Colors.ENDC}""")
        os.system(f"""cd "{path}" & conda env update --name {env_name} --file {file_name}""")
        os.system(f"cd {os.path.expanduser('~')}")
        print(f"{Colors.MESSAGE}Packages installed on {env_name}!{Colors.ENDC}")
        input('Press Enter to continue...:')

    elif option_list[int(response) - 1] == "Remove environment":
        envs = [env for env in os.listdir(os.path.join(anaconda_path, 'envs')) if os.path.isdir(os.path.join(os.path.join(anaconda_path, 'envs'), env))]

        print(f"""\n{Colors.MESSAGE}Select env from followings
--------------------------{Colors.ENDC}""")
        [print(f"{Colors.OKCYAN}{i + 1}) {env}{Colors.ENDC}") for i, env in enumerate(envs)]

        env_index = ask_env_index(len(envs))
        if not env_index:
            continue
        env_name = envs[int(env_index) - 1].split()[0]
        print(f"""{Colors.WARNING}{"-" * len(f"Environment '{env_name}' is selected")}
Environment '{env_name}' is selected{Colors.ENDC}""")
        conformation = input(f"{Colors.WARNING}Are you sure, you want to remove '{env_name}' env [y/n]: {Colors.ENDC}")
        while True:
            if conformation.lower() in ['y', 'yes']:
                print(f"""{Colors.MESSAGE}\n{'-' * len(f'Removing env {env_name}')}\nRemoving env {env_name}{Colors.ENDC}""")
                os.system(f"conda deactivate & conda env remove --name {env_name} -y")
                print(f"{Colors.MESSAGE}Removed all packages in environment {env_name}:{Colors.ENDC}")
                break
            elif conformation.lower() in ['n', 'no', 'b']:
                break
            else:
                print(f"{Colors.WARNING}Invalid response!{Colors.ENDC}")
                conformation = input(f"{Colors.WARNING}Are you sure, you want to remove {env_name} [y/n]: {Colors.ENDC}")
        input('Press Enter to continue...:')

    elif option_list[int(response) - 1] == "Rename environment":
        envs = [env for env in os.listdir(os.path.join(anaconda_path, 'envs')) if os.path.isdir(os.path.join(os.path.join(anaconda_path, 'envs'), env))]

        print(f"""\n{Colors.MESSAGE}Select env from followings
--------------------------{Colors.ENDC}""")
        [print(f"{Colors.OKCYAN}{i + 1}) {env}{Colors.ENDC}") for i, env in enumerate(envs)]

        env_index = ask_env_index(len(envs))
        if not env_index:
            continue
        env_name = envs[int(env_index) - 1].split()[0]
        print(f"""{Colors.WARNING}{"-" * len(f"Environment '{env_name}' is selected")}
Environment '{env_name}' is selected{Colors.ENDC}""")

        new_name = ask_env_name()
        if not new_name:
            continue  # If it's 'b' then ask_env_name returns False
        os.rename(os.path.join(anaconda_path, 'envs', env_name), os.path.join(anaconda_path, 'envs', new_name))
        print(f"{Colors.MESSAGE}Environment name '{env_name}' is changed to '{new_name}'")
        input('Press Enter to continue...:')

    elif option_list[int(response) - 1] == "Clone environment":
        envs = [env for env in os.listdir(os.path.join(anaconda_path, 'envs')) if os.path.isdir(os.path.join(os.path.join(anaconda_path, 'envs'), env))] + ['base']

        print(f"""\n{Colors.MESSAGE}Select env from followings
--------------------------{Colors.ENDC}""")
        [print(f"{Colors.OKCYAN}{i + 1}) {env}{Colors.ENDC}") for i, env in enumerate(envs)]

        env_index = ask_env_index(len(envs))
        if not env_index:
            continue
        env_name = envs[env_index - 1].split()[0]
        print(f"""{Colors.WARNING}{"-" * len(f"Environment '{env_name}' is selected")}
Environment '{env_name}' is selected{Colors.ENDC}""")
        print(f"""{Colors.QUESTION}\n-------------------------------{Colors.ENDC}""")

        new_env_name = ask_env_name()
        if not new_env_name:
            continue
        os.system(f"conda create --clone {env_name} --name {new_env_name}")
        input('Press Enter to continue...:')

    elif option_list[int(response) - 1] == "List all packages in an environment":
        envs = [env for env in os.listdir(os.path.join(anaconda_path, 'envs')) if os.path.isdir(os.path.join(os.path.join(anaconda_path, 'envs'), env))] + ['base']

        print(f"""\n{Colors.MESSAGE}Select env from followings
--------------------------{Colors.ENDC}""")
        [print(f"{Colors.OKCYAN}{i + 1}) {env}{Colors.ENDC}") for i, env in enumerate(envs)]

        env_index = ask_env_index(len(envs))
        if not env_index:
            continue
        env_name = envs[env_index - 1].split()[0]
        print("\n---------------------------------------------------------------------------")
        os.system(f"conda list -n {env_name}")
        input('Press Enter to continue...:')

    elif option_list[int(response) - 1] == "List all revision / History of an environment":
        envs = [env for env in os.listdir(os.path.join(anaconda_path, 'envs')) if os.path.isdir(os.path.join(os.path.join(anaconda_path, 'envs'), env))] + ['base']

        print(f"""\n{Colors.MESSAGE}Select env from followings
--------------------------{Colors.ENDC}""")
        [print(f"{Colors.OKCYAN}{i + 1}) {env}{Colors.ENDC}") for i, env in enumerate(envs)]

        env_index = ask_env_index(len(envs))
        if not env_index:
            continue
        env_name = envs[env_index - 1].split()[0]
        os.system(f"conda activate {env_name} & conda list --revisions")
        os.system("conda deactivate")
        input('Press Enter to continue...:')

    elif option_list[int(response) - 1] == "Restore environment to a previous revision":
        envs = [env for env in os.listdir(os.path.join(anaconda_path, 'envs')) if os.path.isdir(os.path.join(os.path.join(anaconda_path, 'envs'), env))] + ['base']

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
        print(f"""{Colors.MESSAGE}{'-'*len(f"Version {version} is restored of {env_name}")}\nVersion {version} is restored of {env_name}{Colors.ENDC}""")
        input('Press Enter to continue...:')

    elif option_list[int(response) - 1] == "List of environments":
        envs = ['base'] + [env for env in os.listdir(os.path.join(anaconda_path, 'envs')) if os.path.isdir(os.path.join(os.path.join(anaconda_path, 'envs'), env))]

        print(f"""\n{Colors.MESSAGE}Select env from followings
--------------------------{Colors.ENDC}""")
        [print(f"{Colors.OKCYAN}{i + 1}) {env}{Colors.ENDC}") for i, env in enumerate(envs)]
        input('Press Enter to continue...:')

    elif option_list[int(response) - 1] == "Close":
        break
