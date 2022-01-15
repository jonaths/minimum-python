# Minimal Python Project

## Note

This is simply a fork of https://github.com/jonaths/minimum-python except with documentation and comments translated into English, to make my life a little easier.  All kudos should go to @jonaths, though!

## Contents

1. tests directory configured to read and test files stored in the app directory 
2. onfig.py file that reads environment variables from the .env file stored in the project root directory
3. Fully populated .gitignore file
4. requirements.txt with modules required to process environment variables and rich logging to console
5. Dockerfile to build a container that install the required modules and configures virtualenv

## Installation
1. Create virtualenv `virtualenv env --python=python3`
2. Install requirements `pip install -r requirements.txt`
3. Create .env file and add the environment variable `STORAGE_LOGS`

    `STORAGE_LOGS = '/home/ropetin/minimum-python/app/common/storage/logs'`
   
## Demo

Run the application in app `python cmd_hello_world.py --message "hello world"`
