import os
import sys
import signal
from dotenv import load_dotenv

from components.generate_ssh_keys import generate_key_default
from components.install_projects import install_projects
from components.run_projects import run_projects
from components.generate_nginx_configuration import nginx_config

load_dotenv()

OS = os.getenv('OS')


def sigint_handler(signal, frame):
    print('\nScript is terminated')
    sys.exit(0)


signal.signal(signal.SIGINT, sigint_handler)

if(len(sys.argv) == 2):
    if(sys.argv[1] == '--generate-ssh-key'):
        generate_key_default()
    elif(sys.argv[1] == '--install-project'):
        install_projects()
    elif(sys.argv[1] == '--run-project'):
        run_projects()
    elif(sys.argv[1] == '--nginx-config'):
        nginx_config()
    elif(sys.argv[1] == '--help'):
        print('\nUsage:')
        print('\t--generate-ssh-key')
        print('\t--install-project')
        print('\t--run-project')
        print('\t--nginx-config')
        print('\t--help')
        print('\n')
else:
    print('\nUsage:')
    print('\t--generate-ssh-key')
    print('\t--install-project')
    print('\t--run-project')
    print('\t--nginx-config')
    print('\t--help')
    print('\n')
