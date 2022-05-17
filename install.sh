#!/bin/sh

sudo apt install python3
mkdir ~/.deploy
echo "alias deploy='python3 ~/.deploy/deploy_script/index.py'" >> ~/.bashrc
echo "alias deploy_update_script='sh ~/.deploy/deploy_script/update.sh'" >> ~/.bashrc
source ~/.bashrc
mv ~/deploy_script ~/.deploy