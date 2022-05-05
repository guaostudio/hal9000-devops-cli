from os import system, path

name_ssh = ['api','page','admin']
ssh_path = path.expanduser('~/.ssh')

def generate_key_default():
    folder_name = input('Name project: ')
    fileValidation = path.exists(ssh_path + '/config')

    system(f'mkdir {ssh_path}/{folder_name}')
    system('eval `ssh-agent -s`')

    if fileValidation == False: system(f'touch {ssh_path}/config && chmod 700 {ssh_path}/config')

    for key in name_ssh:
        system(f'ssh-keygen -f {ssh_path}/{folder_name}/{key} -P ""')
        with open(f'{ssh_path}/config', "a") as config_file:
            config_file.write(f"""
            Host {key}
                HostName github.com
                IdentityFile {ssh_path}/{folder_name}/{key}
            """)
        system(f'ssh-add {ssh_path}/{folder_name}/{key}')

    for private_key in name_ssh:
        print(f'PRIVATE SSH KEY ({private_key}): ')
        system(f'cat {ssh_path}/{folder_name}/{private_key}.pub')
        print('\n\n\n')

def generate_key_custom():
    print('hi')
