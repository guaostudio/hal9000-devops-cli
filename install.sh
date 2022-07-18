#!/bin/sh

sudo apt update
sudo apt install -y python3
sudo apt install -y python3-pip
pip install -r requirements.txt
mkdir ~/.deploy
touch .env
echo "CLI_PATH=~/.deploy/CLI/" >> .env
echo "alias deploy='python3 ~/.deploy/CLI/index.py'" >> ~/.bashrc
echo "alias update_cli='sh ~/.deploy/CLI/update.sh'" >> ~/.bashrc
sudo cp -r ~/CLI ~/.deploy
cd ~
source .bashrc
sudo rm -rf ~/CLI
