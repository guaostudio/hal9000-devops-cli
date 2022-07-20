import os
import sys
import signal
import os
from dotenv import load_dotenv

from components.generate_ssh_keys import generate_ssh_key
from components.install_projects import install_projects
from components.run_projects import run_projects
from components.generate_nginx_configuration import nginx_config
from components.info_project import get_info_project

from components.helpers.handle_errors import handle_parameters_errors

load_dotenv()
HOME_PATH = os.path.expanduser('~') + "/.deploy" + "/CLI"

PATH_DATA = os.getenv('CLI_PATH')
PATH_DATA = HOME_PATH if PATH_DATA else os.path.dirname(
    os.path.realpath(__file__))


def sigint_handler(signal, frame):
    print('\nScript is terminated')
    sys.exit(0)


signal.signal(signal.SIGINT, sigint_handler)

if(len(sys.argv) >= 2):
    if(sys.argv[1] == '--generate-ssh-key'):
        ssh_handle_errors = handle_parameters_errors("ssh_key", sys.argv[1:])
        if(ssh_handle_errors["success"] == True):
            generate_ssh_key(ssh_handle_errors["data"])
    elif(sys.argv[1] == '--install-project'):
        install_projects(PATH_DATA)
    elif(sys.argv[1] == '--run-project'):
        run_projects(PATH_DATA)
    elif(sys.argv[1] == '--nginx-config'):
        nginx_config(PATH_DATA)
    elif(sys.argv[1] == '--info'):
        get_info_project(PATH_DATA)
    elif(sys.argv[1] == '--help'):
        print('\nUsage:')
        print('\t--generate-ssh-key')
        print('\t--install-project')
        print('\t--run-project')
        print('\t--nginx-config')
        print('\t--help')
        print('\t--info')
        print('\n')
    else:
        print('Command is not valid \nUse --help for more information')
else:
    print('\nUsage:')
    print('\t--generate-ssh-key')
    print('\t--install-project')
    print('\t--run-project')
    print('\t--nginx-config')
    print('\t--help')
    print('\n')
