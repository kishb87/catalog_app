# CAR CATALOG APP

This project was built as the final project for the Full Stack Foundations course
which is part of the Full Stack Nanodegree Program.

It was built using the Python based Flask Web Framework with PostgreSQL for the
database. It follows a model-view-template design pattern.

## To execute program:

### BOOT VIRTUAL ENVIRONMENT:
1. For this step Vagrant must be installed. From commaned line, go to catalog_app
folder and enter "vagrant up" in terminal.
2. Once the vagrant machine is installed, enter "vagrant ssh" into command line to connect to vm.


### CREATE DATABASE SCHEMA AND LOAD DATA:
1. Type "sudo su - postgres" to switch to postgres username
2. Type "cd /vagrant/catalog_app" to enter directory.
3. type "psql" to open Postgres Terminal
4. Type "CREATE DATABASE catalog;"
5. Exit Postgres terminal with "CRTL + Z"
6. Enter "python database_setup.py" from terminal
7. Then enter "python data_load.py" from terminal

### TO RUN APPLICATION:
1. Run "python catalog.py" from terminal

### TO DROP DATABASE:
1. run "python drop_db.py" from terminal

