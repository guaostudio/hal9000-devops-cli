from os import name, path
import json


def get_info_project(home_path):
    folder_path_slash = ('\\' if name == 'nt' else '/')
    data_projects_path = home_path + folder_path_slash + "data_projects.json"
    dash = ('-' * 50)

    fileValidation = path.exists(data_projects_path)
    data_project = f"""         INFO\n
HOME PATH: {home_path}
COMMANDS PATH: {home_path + folder_path_slash + "commands"}
DATA PROJECTS PATH: {data_projects_path}
    """
    if(fileValidation == False):
        data_project += f"\nPROJECTS: You don't have any project"
        return print(data_project)
    else:
        data_project += f"\nPROJECTS:"

    with open(data_projects_path, "r") as jsonFile:
        file_data = json.load(jsonFile)

    for project in file_data["projects"]:
        data_project += f"""
\n{dash}
Project name: {project["project_name"]}
    API: {True if project["api"]["url_repository"] else False}
    PAGE: {True if project["page"]["url_repository"] else False}
    ADMIN: {True if project["admin"]["url_repository"] else False}
{dash}\n"""
    return print(data_project)
