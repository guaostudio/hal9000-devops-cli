#!/bin/sh

sudo apt install python3
sudo apt install python3-pip
pip install -r requirements.txt
mkdir ~/.deploy
touch .env
echo "CLI_PATH=~/.deploy/CLI/" >> .env
echo "alias deploy='python3 ~/.deploy/CLI/index.py'" >> ~/.bashrc
echo "alias update_cli='sh ~/.deploy/CLI/update.sh'" >> ~/.bashrc
mv ~/CLI ~/.deploy
cd ~
source .bashrc
