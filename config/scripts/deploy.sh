#!/bin/bash

# Use: sh deploy.sh
# Flags: sh deploy.sh update/clean

# Config elements
PROJECT='eventup'
COMMAND=$1

BASE_NAME=$(basename $0)
BASE_PATH=$(dirname $(readlink -f $0))
BASE_PATH_NAME="$BASE_PATH/$BASE_NAME"

echo "Script path with name: $BASE_PATH_NAME"

# Inside the project
export COMPOSE_FILE=production.yml

# Stop Services
sudo supervisorctl stop $PROJECT
sudo docker-compose down

# Remove all
if [ "$COMMAND" = 'clean' ]; then
sudo docker rm -vf $(sudo docker ps -a -q)
sudo docker rmi -f $(sudo docker images -a -q)
sudo docker system prune -f
sudo docker volume prune -f
fi

# Get new changes &&  Build new changes Get Pull
# git clean
git checkout master
git reset --hard origin/master
git fetch --all
git pull origin master | sudo docker-compose build

# Migrations
if [ "$COMMAND" = 'clean' ]; then
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc" -delete
sudo docker-compose run --rm django python manage.py makemigrations
sudo docker-compose run --rm django python manage.py migrate
fi

# Up new services and Active auto services
sudo docker-compose up --force-recreate -d && sudo supervisorctl start $PROJECT && sudo supervisorctl restart all
