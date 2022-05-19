# hal9000-devops-cli

CLI for deploy

## REQUIREMENTS

Python 3.*

## INSTALLATION

git clone https://github.com/guaostudio/hal9000-devops-cli.git CLI && cd CLI && sh install.sh

## UPDATE script

sh update.sh or deploy_update_script alias

## USAGE

Steps for use this script:

1. First need install project with the command:
    * deploy --install-project

2. Then create a commands for run the project:
    * deploy --run-project
      (option 1)

3. Run projects
    * deploy --run-project
      (option 2)

## ADITIONAL commands

* deploy --generate-ssh-key
    * Command for create ssh keys
* deploy --nginx-config
    * Command for create nginx config file in 1 (page.com/admin) or 3(admin.page.com) files and run certbot

for more information --help
