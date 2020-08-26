#!/bin/bash

# Use: sh deploy.sh
# Flags: sh deploy.sh update clean

# Config elements
UPDATESYSTEM=$1
REMOVEDATA=$2
# ORIGIN=$3 || 'master'

# Update all
if [ -n "$UPDATESYSTEM" ]; then
    if [ $UPDATESYSTEM = 'update' ]; then
        sudo apt-get update -y && sudo apt-get upgrade -y
    fi
fi

# Inside the project
cd /home/ubuntu/backend/

# Stop Services
sudo supervisorctl stop eventup
sudo docker-compose -f production.yml down

# Remove all
if [ -n "$REMOVEDATA" ]; then
    if [ "$REMOVEDATA" = 'clean' ]; then
        # Remove images
        sudo docker rmi -f $(sudo docker images -a -q)
    # else
        # # Remove all containers and images
        # sudo docker rm -vf $(sudo docker ps -a -q)
    fi
fi

# Get new changes &&  Build new changes Get Pull
# git clean
git checkout master
git reset --hard origin/master
git fetch --all
git pull origin master | sudo docker-compose -f production.yml build

# Up new services and Active auto services
sudo docker-compose -f production.yml up --force-recreate -d && sudo supervisorctl start eventup && sudo supervisorctl restart all
