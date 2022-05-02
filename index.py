import sys
import signal
from components.generate_ssh_keys import generate_key_default, generate_key_custom
from components.install_projects import install_projects
from components.run_projects import run_projects


def sigint_handler(signal, frame):
    print('\nScript is terminated')
    sys.exit(0)


signal.signal(signal.SIGINT, sigint_handler)

if(len(sys.argv) == 2):
    if(sys.argv[1] == '--generate-ssh-key-default'):
        generate_key_default()
    elif(sys.argv[1] == '--generate-ssh-key-custom'):
        generate_key_custom()
    elif(sys.argv[1] == '--install-project'):
        install_projects()
    elif(sys.argv[1] == '--run-project'):
        run_projects()
else:
    print('Invalid argument')
