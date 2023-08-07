#		AIRBNB clone - The console :city_sunrise:

## Project Description:


Welcome to the exciting Airbnb clone project! In this initial phase, we have developed the backend and a console application in Python using the `cmd` and `json` modules.
Data is stored as Python objects and saved in JSON format for easy management. Our replica offers basic functionalities such as searching and booking accommodations,
as well as interacting with users. This project lays the foundation for future enhancements and expansions.


## Description of the command interpreter:speech_balloon:

The command interpreter is a Bash-like interface specifically designed for the Airbnb clone project. It accepts a limited
number of predefined commands created especially for the usage of the Airbnb website. It functions as the frontend of the
web application, allowing users to interact with the Python-based backend using object-oriented programming (OOP).

Some of the commands available are:floppy_disk:
- show
- create
- update
- destroy
- all
- quit - exit
- help

Command Interpreter Description:computer:
__________________________________________________
| Command            | Description                        |
|____________________|____________________________________|
| help               | Displays help page                 |
----------------------------------------------------
| quit / EOF         | Exits the console                  |
----------------------------------------------------
| all                | Prints all instances               |
|                    | based on the class name            |
----------------------------------------------------
| create <class>     | Creates a new instance            |
|                    | of a given class with a unique ID  |
|                    | and saves it to a JSON file        |
----------------------------------------------------
| show <class> <id>  | Prints the string representation  |
|                    | of a class instance                |
|                    | based on the class name and ID     |
----------------------------------------------------
| update             | Updates an instance based on       |
|                    | class name and id by adding or     |
|                    | updating attributes and saves      |
|                    | changes to a JSON file             |
----------------------------------------------------
| destroy <class>    | Deletes an instance based on       |
| <id>               | class name and id and saves it     |
|                    | to a JSON file                     |
----------------------------------------------------


## How to start:book::computer:

Download the project from the GitHub repository.
Navigate to the root directory of the project.
launch the command interpreter `python ./console`
Utilize the provided commands to efficiently manage AirBnB objects and perform various operations with ease.

## EXAMPLES

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

## Authors:pencil12:

- **Juan Ramirez**  <@gmail.com> 
- **Oscar Morales** <omoralespj@gmail.com> 