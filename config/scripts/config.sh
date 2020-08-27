#!/bin/bash

# Use: sh deploy.sh
# Flags: sh deploy.sh update/clean

# Config elements
COMMAND=$1

BASE_NAME=`basename $0`
BASE_PATH=$(dirname $(readlink -f $0))
BASE_PATH_NAME="$BASE_PATH/$BASE_NAME"

echo "Script path with name: $BASE_PATH_NAME"

# Update all
if [ -n "$COMMAND" && $COMMAND = 'update' ]; then
    sudo apt-get update -y && sudo apt-get upgrade -y
fi

# Permissions Git
cd /home/ubuntu/backend/
cd .git/objects
sudo chown -R "${USER:-$(id -un)}" .

# Inside the project
cp `$BASE_PATH/deploy.sh` /home/ubuntu/backend/
cd /home/ubuntu/backend/
sh deploy.sh $COMMAND
