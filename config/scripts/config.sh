#!/bin/bash

# Use: sh deploy.sh
# Flags: sh deploy.sh update/clean
sudo chmod +x ./config.sh
sudo chmod +x ./deploy.sh
# PATH
BASE_NAME=`basename $0`
BASE_PATH=$(dirname $(readlink -f $0))
BASE_PATH_NAME="$BASE_PATH/$BASE_NAME"
# echo "Script path with name: $BASE_PATH_NAME"

# Config elements
COMMAND=$1 || ''

# # Update all
# if [ -n "$COMMAND" && $COMMAND = 'update' ]; then
#     sudo apt-get update -y && sudo apt-get upgrade -y
# fi

# Permissions Git
ROUTE=/home/ubuntu/backend/
cd `${ROUTE}.git/objects`
pwd
ls
sudo chown -R "${USER:-$(id -un)}" .

# Inside the project
ROUTE_FILE=`$BASE_PATH/deploy.sh`
sudo rm -rf $ROUTE_FILE
sudo cp $ROUTE_FILE `${ROUTE}deploy.sh`
sudo chmod +x `${ROUTE}deploy.sh`
cd $ROUTE
pwd
ls
# sh deploy.sh $COMMAND
