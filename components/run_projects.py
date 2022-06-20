import json
import os

from .helpers.run_command_project import run_command_project

path_user = os.path.expanduser('~')
folder_path_slash = ('\\' if os.name == 'nt' else '/')


def clearConsole(): return os.system(
    'cls' if os.name in ('nt', 'dos') else 'clear')


def run_projects(PATH_DATA):
    file_commands = PATH_DATA + folder_path_slash + "commands_projects.json"
    data_projects_file = PATH_DATA + folder_path_slash + "data_projects.json"

    resume = "y"
    option_status = "off"

    while resume == "y" or resume == "Y":
        print("Select a option to continue: ")
        print("1. Add project")
        print("2. Run project")
        print("3. Exit")

        option = input(": ")

        if(option == "1"):
            option_status = "add_project"
            resume = "n"
            clearConsole()
        elif(option == "2"):
            option_status = "run_project"
            clearConsole()
            resume = "n"
        elif(option == "3"):
            option_status = "n"
            clearConsole()
            resume = "n"

    while option_status == "add_project":
        data = ""
        project_name = ""

        with open(data_projects_file, 'r') as f:
            data = json.load(f)

        print("Select a project: ")
        for idx, x in enumerate(data['projects']):
            projects_name = x["project_name"]
            print(f'{idx}.- {projects_name}')

        print("99.- exit")

        option = int(input(": "))

        if(option == 99):
            option_status = "off"
            return

        if(option < len(data['projects'])):
            project_name = data['projects'][option]["project_name"]
            commands = get_commands(project_name)
            get_project_folders(project_name, commands,
                                data_projects_file, file_commands)
        else:
            clearConsole()

        continue_add_projects = input(
            "do you want to continue with other projects? (y/n): ")

        if(continue_add_projects == "n" or continue_add_projects == "N"):
            option_status = "off"

    while(option_status == "run_project"):
        data = ""
        project_name = ""

        with open(file_commands, 'r') as f:
            data = json.load(f)

        print("Projects with existing commands:")
        for idx, x in enumerate(data['projects']):
            projects_name = x["project_name"]
            print(f'{idx}.- {projects_name}')

        print("99.- exit")

        option = int(input(": "))

        if(option == 99):
            option_status = "off"
            return

        if(option < len(data['projects'])):
            project_name = data['projects'][option]["project_name"]
            folders_to_init(project_name, file_commands)
        else:
            clearConsole()

        continue_add_projects = input(
            "do you want to continue with other projects? (y/n): ")

        if(continue_add_projects == "n" or continue_add_projects == "N"):
            option_status = "off"


def get_project_folders(project_name, commands_json, data_projects, file_commands):
    data = ""
    project_json_commands = {
        "project_name": project_name,
        "project_commands": {
            "api": {},
            "page": {},
            "admin": {}
        }
    }

    with open(data_projects, 'r') as f:
        data = json.load(f)
    project = find_project(data['projects'], project_name)
    keys = list(project.keys())
    keys.remove("project_name")
    print("keys:", keys)
    for x in keys:
        project_json_commands["project_commands"][x] = {
            "path": project[x]['folder_path'],
            "url": project[x]['url_repository'],
            "commands": commands_json[project_name][x]
        }
    fileValidation = os.path.exists(file_commands)
    file = ""
    if(fileValidation == False):
        file = open(file_commands, "w")
        file.write(json.dumps({"projects": [project_json_commands]}))
        file.close()

    elif(fileValidation == True):
        with open(file_commands, "r") as jsonFile:
            file_data = json.load(jsonFile)

        file_data["projects"] = file_data["projects"] + [project_json_commands]

        with open(file_commands, "w") as jsonFile:
            json.dump(file_data, jsonFile)
    return project_json_commands


def get_commands(name_project):
    resume = "y"
    commands_json = {
        name_project: {
            "api": {},
            "page": {},
            "admin": {}
        }
    }
    while resume == "y" or resume == "Y":
        api_status = input("Do you add commands to api ? (y/n): ")
        if(api_status == "y" or api_status == "Y"):

            api_additional = ""
            api_install_modules_command = input(
                "Write command for install modules: ")
            api_build_project_command = input(
                "Write command for build project: ")
            api_migration_project_command = input(
                "Write command for migration project: ")
            api_run_project_command = input("Write command for run project: ")
            api_additional_command = input(
                "Do you have a aditional command? (y/n):")

            if(api_additional_command == "y" or api_additional_command == "Y"):
                api_additional = input("Write command: ")

            commands_json[name_project]["api"] = {
                "install_modules":      api_install_modules_command,
                "build_project":        api_build_project_command,
                "migration_project":    api_migration_project_command,
                "run_project":          api_run_project_command,
                "additional_command":   api_additional
            }

        page_status = input("Do you add commands to page ? (y/n): ")
        if(page_status == "y" or page_status == "Y"):
            page_additional = ""

            page_install_modules_command = input(
                "Write command for install modules: ")
            page_build_project_command = input(
                "Write command for build project: ")
            page_run_project_command = input("Write command for run project: ")

            page_additional_command = input(
                "Do you have a aditional command? (y/n):")
            if(page_additional_command == "y" or page_additional_command == "Y"):
                page_additional = input("Write command: ")

            commands_json[name_project]["page"] = {
                "install_modules": page_install_modules_command,
                "build_project": page_build_project_command,
                "run_project": page_run_project_command,
                "additional_command": page_additional
            }
        admin_status = input("Do you add commands to admin ? (y/n): ")
        if(admin_status == "y" or admin_status == "Y"):
            admin_additional = ""

            admin_install_modules_command = input(
                "Write command for install modules: ")
            admin_build_project_command = input(
                "Write command for build project: ")
            admin_run_project_command = input(
                "Write command for run project: ")

            admin_additional_command = input(
                "Do you have a aditional command? (y/n):")

            if(admin_additional_command == "y" or admin_additional_command == "Y"):
                admin_additional = input("Write command: ")

            commands_json[name_project]["admin"] = {
                "install_modules": admin_install_modules_command,
                "build_project": admin_build_project_command,
                "run_project": admin_run_project_command,
                "additional_command": admin_additional
            }
        print("\n**COMMANDS ADDED SUCCESSFULLY**\n")
        resume = "n"
    return commands_json


def folders_to_init(project_name, file_commands):
    resume = "y"

    while resume == "y" or resume == "Y":
        data = ""
        values_remove = []

        with open(file_commands, 'r') as f:
            data = json.load(f)

        project = find_project(data['projects'], project_name)
        keys = list(project['project_commands'].keys())

        clearConsole()

        for x in keys:
            if(len((project['project_commands'][x]['commands']).keys()) == 0):
                values_remove.append(x)

        for value_to_delete in values_remove:
            keys.remove(value_to_delete)

        for idx, x in enumerate(keys):
            print(f'{idx}.- {x}')

        print("\n98.- All")
        print("99.- Exit\n")

        folder_init = int(input("Select project to init: "))

        if(folder_init == 98):
            for x in keys:
                project_data = project['project_commands'][x]
                commands = project_data['commands']
                run_command_project(project_data['path'], commands)
                print("All repositories is running")

        elif(folder_init == 99):
            resume = "n"
            return

        if(folder_init < len(keys)):
            project_data = project['project_commands'][keys[folder_init]]
            commands = project_data['commands']
            run_command_project(project_data['path'], commands)

        continue_add_projects = input(
            "do you want to continue with other projects? (y/n): ")
        if(continue_add_projects == "n" or continue_add_projects == "N"):
            resume = "n"


def find_project(json_object, name):
    for dict in json_object:
        if dict['project_name'] == name:
            return dict
