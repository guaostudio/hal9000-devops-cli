from os import system, path, name
from .helpers.folders_name import folders_name


ssh_path = path.expanduser('~/.ssh')
permissions = ("" if name == 'nt' else 'sudo')


def generate_ssh_key():
    folder_name = input('Name project: ')

    if(folder_name == ''):
        return print("Name project is empty")

    name_ssh = folders_name()
    fileValidation = path.exists(ssh_path + '/config')

    system(f'mkdir {ssh_path}/{folder_name}')
    system(f'{permissions} eval `ssh-agent -s`')

    if fileValidation == False:
        system(
            f'touch {ssh_path}/config && {permissions} chmod 700 {ssh_path}/config')

    for key in name_ssh:
        system(f'ssh-keygen -f {ssh_path}/{folder_name}/{key} -P ""')

        with open(f'{ssh_path}/config', "a") as config_file:
            config_file.write(f"""
            Host {key}-{folder_name}
                HostName github.com
                IdentityFile {ssh_path}/{folder_name}/{key}
            """)

        system(f'ssh-add {ssh_path}/{folder_name}/{key}')

    for public_key in name_ssh:
        print(f'PUBLIC SSH KEY ({public_key}): ')
        print(f'SSH KEY => {key}-{folder_name}')
        system(f'cat {ssh_path}/{folder_name}/{public_key}.pub')
        print('\n')
