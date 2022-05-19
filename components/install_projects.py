from os import system, path, name
import json


def install_projects(PATH_DATA):
    user_path = input(
        "Use other path ? (default: /home/user/): ") or path.expanduser('~')

    resume = "y"
    folder_path_slash = ('\\' if name == 'nt' else '/')
    data_projects_path = PATH_DATA + folder_path_slash + "data_projects.json"

    try:
        while resume == "y" or resume == "Y":
            system('cls' if name == 'nt' else 'clear')

            api_url_repository = ""
            page_url_repository = ""
            admin_url_repository = ""

            project_name = input('Name project: ')
            project_path = user_path + \
                folder_path_slash + project_name

            fileValidation = path.exists(project_path)

            if fileValidation == False:
                system(f'mkdir {project_path}')

            api_folder = input(
                ' Do you have api folder in your project ? (y/n): ')

            if('y' in api_folder or 'Y' in api_folder):
                api_url_repository = input('Enter api url repository: ')
                ssh_key_api = input(
                    'Do you have a specific ssh key in your project ? (y/n): ')

                if('y' in ssh_key_api or 'Y' in ssh_key_api):
                    api_url_repository = api_url_repository.replace(
                        'github.com', 'api')
                system(
                    f'cd {project_path} && git clone {api_url_repository} api')

            page_folder = input(
                ' Do you have page folder in your project ? (y/n): ')

            if('y' in page_folder or 'Y' in page_folder):
                page_url_repository = input('Enter page url repository: ')
                ssh_key_page = input(
                    'Do you have a specific ssh key in your project ? (y/n): ')
                if('y' in ssh_key_page or 'Y' in ssh_key_page):
                    page_url_repository = page_url_repository.replace(
                        'github.com', 'page')
                system(
                    f'cd {project_path} && git clone {page_url_repository} page')

            admin_folder = input(
                ' Do you have admin folder in your project ? (y/n): ')

            if('y' in admin_folder or 'Y' in admin_folder):
                admin_url_repository = input('Enter admin url repository: ')
                ssh_key_admin = input(
                    'Do you have a specific ssh key in your project ? (y/n): ')
                if('y' in ssh_key_admin or 'Y' in ssh_key_admin):
                    admin_url_repository = admin_url_repository.replace(
                        'github.com', 'admin')
                system(
                    f'cd {project_path} && git clone {admin_url_repository} admin')

            data_project = {
                "projects": [{
                    "project_name": project_name,
                    "api": {
                        "folder_path": f'{project_path}{folder_path_slash}api',
                        "url_repository": api_url_repository
                    },
                    "page": {
                        "folder_path": f'{project_path}{folder_path_slash}page',
                        "url_repository": page_url_repository
                    },
                    "admin": {
                        "folder_path": f'{project_path}{folder_path_slash}admin',
                        "url_repository": admin_url_repository
                    }
                }]
            }

            fileValidation = path.exists(data_projects_path)
            file = ""

            if(fileValidation == False):
                file = open(data_projects_path, "w")
                file.write(json.dumps(data_project))
                file.close()

            elif(fileValidation == True):
                with open(data_projects_path, "r") as jsonFile:
                    file_data = json.load(jsonFile)

                file_data["projects"] = file_data["projects"] + \
                    data_project["projects"]

                with open(data_projects_path, "w") as jsonFile:
                    json.dump(file_data, jsonFile)

            resume = input('Do you want repository to other project ? (y/n): ')
        print('Projects installed successfully!')
    except Exception as e:
        print("Error: ", e)
