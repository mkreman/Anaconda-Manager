import os
import sys
import json
import platform


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


def get_anaconda_path():
    if os.path.exists(f'./anaconda-path-{platform.system()}.json'):
        return json.load(open(f'./anaconda-path-{platform.system()}.json'))['anaconda_path']
    else:
        anaconda_path = input(f"{Colors.QUESTION}Enter the path to your Anaconda folder:{Colors.ENDC} \n")
        with open(f'./anaconda-path-{platform.system()}.json', 'w') as f:
            json.dump({'anaconda_path': anaconda_path}, f)

anaconda_path = get_anaconda_path()

def ask_env_name():
    name = input(f"{Colors.QUESTION}Enter the name of environment: {Colors.ENDC}")
    envs = ['base'] + [env for env in os.listdir(os.path.join(anaconda_path, 'envs')) if os.path.isdir(os.path.join(os.path.join(anaconda_path, 'envs'), env))]
    while True:
        if name == 'b':
            return False
        elif name in envs:
            print(f"{Colors.WARNING}'{name}' env is already exists!{Colors.ENDC}")
            name = input(f"{Colors.QUESTION}Enter the name of environment: {Colors.ENDC}")
            continue
        elif name.find('/') == -1 and name.find(' ') == -1 and name.find(':') == -1 and\
                name.find('#') == -1:
            return name
        else:
            print(f"{Colors.WARNING}Env name '{name}' is invalid, Characters not allowed: ('/', ' ', ':', '#')\n"
                  f"{Colors.ENDC}")
            name = input(f"{Colors.QUESTION}Enter the name of environment: {Colors.ENDC}")


def ask_requirement_path():
    backup_file_path = input(f"{Colors.QUESTION}Enter the path where requirement the back up file is stored: {Colors.ENDC}")
    while True:
        if backup_file_path == 'b':
            return False
        elif os.path.exists(backup_file_path):
            return backup_file_path
        else:
            print(f"{Colors.WARNING}File path '{backup_file_path}' does not exits!{Colors.ENDC}")
            backup_file_path = input(f"{Colors.QUESTION}Enter the path where requirement the back up file is stored: {Colors.ENDC}")


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
    path = input(f"{Colors.QUESTION}Enter the path where you want to store the back up file: {Colors.ENDC}")
    while True:
        if path == 'b':
            return False
        elif os.path.exists(path):
            return path
        else:
            print(f"{Colors.WARNING}Path '{path}' does not exits!{Colors.ENDC}")
            path = input(f"{Colors.QUESTION}Enter the path where you want to store the back up file: {Colors.ENDC}")


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
