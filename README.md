#		AIRBNB clone - The console :city_sunrise:

## Project Description:


Welcome to the exciting Airbnb clone project! In this initial phase, we have developed the backend and a console application in Python using the `cmd` and `json` modules.
Data is stored as Python objects and saved in JSON format for easy management. Our replica offers basic functionalities such as searching and booking accommodations,
as well as interacting with users. This project lays the foundation for future enhancements and expansions.


## Description of the command interpreter:speech_balloon:

The command interpreter is a Bash-like interface specifically designed for the Airbnb clone project. It accepts a limited
number of predefined commands created especially for the usage of the AirBnB website. It functions as the frontend of the
web application, allowing users to interact with the Python-based backend using object-oriented programming (OOP).

## Some of the commands available are:floppy_disk:

- quit - exit
- help
- create
- show
- destroy
- all
- update

## Command Interpreter Description:computer:
|Command| Description |
|--|--|
| **quit or EOF** | Exits the program |
| **Usage** | By itself |
| **-----** | **-----** |
| **help** | Provides a text describing how to use a command.  |
| **Usage** | By itself --or-- **help <command\>** |
| **-----** | **-----** |
| **create** | Creates a new instance of a valid `Class`, saves it (to the JSON file) and prints the `id`.  Valid classes are: BaseModel, User, State, City, Amenity, Place, Review. |
| **Usage** | **create <class name\>**|
| **-----** | **-----** |
| **show** | Prints the string representation of an instance based on the class name and `id`  |
| **Usage** | **show <class name\> <id\>** --or-- **<class name\>.show(<id\>)**|
| **-----** | **-----** |
| **destroy** | Deletes an instance based on the class name and `id` (saves the change into a JSON file).  |
| **Usage** | **destroy <class name\> <id\>** --or-- **<class name>.destroy(<id>)** |
| **-----** | **-----** |
| **all** | Prints all string representation of all instances based or not on the class name.  |
| **Usage** | By itself or **all <class name\>** --or-- **<class name\>.all()** |
| **-----** | **-----** |
| **update** | Updates an instance based on the class name and `id` by adding or updating attribute (saves the changes into a JSON file).  |
| **Usage** | **update <class name\> <id\> <attribute name\> "<attribute value\>"** ---or--- **<class name\>.update(<id\>, <attribute name\>, <attribute value\>)** --or-- **<class name\>.update(<id\>, <dictionary representation\>)**|


## How to start:book::computer:

- Download the project from the GitHub repository.

- Navigate to the root directory of the project.

- launch the command interpreter `python ./console`.

- Utilize the provided commands to efficiently manage AirBnB objects and perform various operations with ease.

## EXAMPLES

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  create  destroy  help  quit  show

Undocumented commands:
======================
all update

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

## Authors:pencil2:

- **Juan Ramirez**   <<juanRCoder@gmail.com>>
- **Oscar Morales**  <<omoralespj@gmail.com>>
