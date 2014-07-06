"""
 Copyright (C) 2014 Maruf Maniruzzaman
 Website: http://cosmosframework.com
 Author: Maruf Maniruzzaman
 License :: OSI Approved :: MIT License
"""

import os
import sys
import logging
import getpass
import createproject

from cosmos.dataservice.objectservice import *

class CommandHandler():
    def __init__(self, *args, **kwargs):
        self.db = kwargs.get("db", None)

    def handle_command(self, *args, **kwarg):
        current_directory = args[0]
        command = args[1]
        command_args = args[2]

        print command

        if command == "new-admin":
            self.create_admin_user()
            return
        if command == "add-herokusettings":
            add_heroku_settings(current_directory)
            sys.exit(0)
        elif command == "new-project":
            project_type = command_args.get("arg0", None)
            createproject.new_project(current_directory, project_type)
            sys.exit(0)
        else:
            print_usage()
            sys.exit(0)

    def get_input(self, prompt):
        input = None
        while not input or len(input)==0:
            input = raw_input(prompt).strip()

        return input

    def _admin_user_created(self, result, error):
        if error:
            logging.error("Admin user creation failed.")
            logging.error(error)
        else:
            logging.info("Admin user was created successfully.")

        sys.exit(0)

    def create_admin_user(self):
        username = self.get_input('Enter admin username: ')
        password = getpass.getpass('Enter admin password: ')
        password_re = getpass.getpass('Repeat admin password: ')
        if password != password_re:
            print "Password mismatch"
            sys.exit(1)

        email = self.get_input('Enter admin email: ')
        data = {"username":username, "password":password, "email":email, "roles":[ADMIN_USER_ROLE_SID]}
        object_service = ObjectService()
        object_service.save(SYSTEM_USER, self.db, COSMOS_USERS_OBJECT_NAME, data, self._admin_user_created)

def print_usage():
    print "Unknown command.\ncosmosadmin new-admin\ncosmosadmin new-project [angular]\ncosmosadmin add-heroku-settings\n"

def add_heroku_settings(current_directory):
    proc_file_path = os.path.join(current_directory, "Procfile")
    with open(proc_file_path, 'w') as procfile:
            procfile.write("web: python cosmosmain.py start-service $PORT")
    req_file_path = os.path.join(current_directory, "requirements.txt")

    with open(req_file_path, 'w') as req_file:
            req_file.write("cosmos")


def admin_main():
    current_directory = os.getcwd()
    if len(sys.argv) < 1:
        print_usage()
        return
    else:
        command = sys.argv[1].strip()
        arg0=None
        arg1=None
        arg2=None
        try:
            arg0 = sys.argv[2]
            arg1 = sys.argv[3]
            arg2 = sys.argv[4]
        except:
            pass

        handler = CommandHandler()
        handler.handle_command(current_directory, command, {"arg0":arg0, "arg1":arg1, "arg2":arg2})

    tornado.ioloop.IOLoop.instance().start()