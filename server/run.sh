#!/usr/bin/bash
source venv/bin/activate
cd flask

if [ "$1" == "development" ] || [ "$1" == "production" ]; then
    export FLASK_ENV=$1
    postfix=""
elif [ "$1" == "dev" ]; then
    export FLASK_ENV=development
    postfix=""
elif [ "$1" == "prod" ]; then
    export FLASK_ENV=production
elif [ "$1" == "" ]; then
    export FLASK_ENV=development
    postfix="by default";
else
    export FLASK_ENV=development
    postfix="because \"$1\" is neither \"development\" nor \"production\" "
fi
echo " - FLASK_ENV is set to \"$FLASK_ENV\" $postfix"
echo
export FLASK_APP=main.py

flask run
cd ..
deactivate
