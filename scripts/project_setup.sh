#!/bin/bash

read -p "Project's folder (EMPTY to install in current folder): " project_folder </dev/tty ;

read -p "Project name (required - letters, numbers underscore): " project_name </dev/tty ;

if [ -n "$project_folder" ]; then
    mkdir $project_folder; cd $project_folder;
fi

if virtualenv venv; then
    source venv/bin/activate
    pip install django
    django-admin startproject --template=https://github.com/lesh1k/django-project-template/archive/master.zip $project_name
    pip install -r $project_name/requirements/development.txt
else
    exit 1
fi