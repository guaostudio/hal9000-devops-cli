import os


def run_command_project(path_project, commands):
    folder_path = ("cd " + path_project +
                   " &&") if commands['install_modules'] != "" else ""
    install_command = (
        commands['install_modules'] + " &&") if commands['install_modules'] != "" else ""
    build_command = (
        commands['build_project'] + " &&") if commands['build_project'] != "" else ""
    migration_command = ""
    if('migration_project' in commands):
        migration_command = (commands['migration_project'] +
                             " &&") if commands['migration_project'] != "" else ""
    run_command = (commands['run_project']
                   ) if commands['run_project'] != "" else ""
    additional_command = (
        " && " + commands['additional_command']) if commands['additional_command'] != "" else ""

    os.system(
        f"{folder_path} {install_command} {build_command} {migration_command} {run_command} {additional_command}")
