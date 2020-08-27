#!/bin/bash

# Use: sh deploy.sh
# Flags: sh deploy.sh update/clean

# Config elements
COMMAND=$1

# Update all
if [ -n "$COMMAND" && $COMMAND = 'update' ]; then
    sudo apt-get update -y && sudo apt-get upgrade -y
fi

# Inside the project
cd /home/ubuntu/backend/
export COMPOSE_FILE=production.yml

# Stop Services
sudo supervisorctl stop eventup
sudo docker-compose down

# Remove all
if [ -n "$COMMAND" && "$COMMAND" = 'clean' ]; then
    # Remove Data
    sudo docker rm -vf $(sudo docker ps -a -q)
    sudo docker rmi -f $(sudo docker images -a -q)\
    sudo docker system prune -f
    sudo docker volume prune -f
fi

# Get new changes &&  Build new changes Get Pull
# git clean
git checkout master
git reset --hard origin/master
git fetch --all
git pull origin master | sudo docker-compose build

# Remove all
if [ -n "$COMMAND" && "$COMMAND" = 'clean' ]; then
    # Migrations
    find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
    find . -path "*/migrations/*.pyc"  -delete
    sudo docker-compose run --rm django python manage.py makemigrations
    sudo docker-compose run --rm django python manage.py migrate
fi

# Up new services and Active auto services
sudo docker-compose up --force-recreate -d && sudo supervisorctl start eventup && sudo supervisorctl restart all
