# AirBnB Clone 
![HBnB Logo](./image/hbnb_logo.png)


### Contents

- [Description](#Description)
- [Environment](#Environment)
- [Requirements](#Requirements)
- [Repo Contents](#Repo)
- [Installation](#Installation)
- [Usage](#Usage)
- [Acknowledgements](#Acknowledgements)

## Description
This repository represents the initial phase of a four-part project aimed at creating a fundamental clone of the AirBnB web application. The first phase introduces a basic console built using the Cmd Python module. This console is designed to manage objects throughout the entire project, providing functionality to implement methods such as create, show, update, all, and destroy for the existing classes and subclasses.

## Environment
The console was developed in Ubuntu 20.04 LTS using Python (version 3.11.5).
For further information on python version, and documentation visit [python.org](https://www.python.org/).

## Requirements
To effectively use and contribute to this project, you should have knowledge in Python3, familiarity with command line interpreters, and a computer running Ubuntu 14.04 with Python3 and a PEP8 style corrector.

## Repo Contents
This repository constains the following files:


| **File**                                             | **Description**                                   |
| ----------------------------------------------------- | ------------------------------------------------- |
| [AUTHORS](./AUTHORS)                                  | Contains information about the authors of the project |
| [base_model.py](./models/base_model.py)              | Defines the BaseModel class (parent class) and methods |
| [user.py](./models/user.py)                           | Defines the User subclass                        |
| [amenity.py](./models/amenity.py)                     | Defines the Amenity subclass                     |
| [city.py](./models/city.py)                           | Defines the City subclass                        |
| [place.py](./models/place.py)                         | Defines the Place subclass                       |
| [review.py](./models/review.py)                       | Defines the Review subclass                      |
| [state.py](./models/state.py)                         | Defines the State subclass                        |
| [file_storage.py](./models/engine/file_storage.py)   | Creates a new instance of a class, serializes and deserializes data |
| [console.py](./console.py)                            | Creates, retrieves, updates, and destroys objects |
| [test_base_model.py](./tests/test_models/test_base_model.py) | Unit tests for base_model                    |
| [test_user.py](./tests/test_models/test_user.py)     | Unit tests for user                              |
| [test_amenity.py](./tests/test_models/test_amenity.py) | Unit tests for amenity                         |
| [test_city.py](./tests/test_models/test_city.py)      | Unit tests for city                              |
| [test_place.py](./tests/test_models/test_place.py)    | Unit tests for place                             |
| [test_review.py](./tests/test_models/test_review.py)  | Unit tests for review                           |
| [test_state.py](./tests/test_models/test_state.py)    | Unit tests for state                            |
| [test_file_storage.py](./tests/test_models/test_engine/test_file_storage.py) | Unit tests for file_storage           |
| [test_console.py](./tests/test_console.py)            | Unit tests for the console                        |


## Installation
Clone the repository and run the console.py
```
$ git clone https://github.com/------/AirBnB_clone.git
```

## Usage

|   **Method**   |   **Description**   |
| -------------- | --------------------- |
|[create](./console.py) | Creates an object of the given class. |
|[show](./console.py) | Prints the string representation of an instance based on the class name and id. |
|[all](./console.py) | Prints all string representation of all instances based or not on the class name. |
|[update](./console.py) | Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). |
|[destroy](./console.py)| Deletes an instance based on the class name and id (save the change into the JSON file). |
|[count](./console.py)| Retrieve the number of instances of a class. |
|[help](./console.py)| Prints information about specific command. |
|[quit/ EOF](./console.py)| Exit the program. |

###### Example No.1

```
░▒▓    ~/ALX/AirBnB_clone  ./console.py
(hbnb) create User
0997878d-87ac-4327-b80d-b88e015aca22
(hbnb) show User 0997878d-87ac-4327-b80d-b88e015aca22
[User] (0997878d-87ac-4327-b80d-b88e015aca22) {'id': '0997878d-87ac-4327-b80d-b88e015aca22', 'created_at': datetime.datetime(2023, 12, 12, 1, 9, 34, 638003), 'updated_at': datetime.datetime(2023, 12, 12, 1, 9, 34, 638033)}
(hbnb) all User
["[User] (744fe833-e004-4011-ad8d-601516c237fe) {'id': '744fe833-e004-4011-ad8d-601516c237fe', 'created_at': datetime.datetime(2023, 12, 12, 1, 9, 0, 724627), 'updated_at': datetime.datetime(2023, 12, 12, 1, 9, 0, 724662)}", "[User] (0997878d-87ac-4327-b80d-b88e015aca22) {'id': '0997878d-87ac-4327-b80d-b88e015aca22', 'created_at': datetime.datetime(2023, 12, 12, 1, 9, 34, 638003), 'updated_at': datetime.datetime(2023, 12, 12, 1, 9, 34, 638033)}"]
(hbnb) update User 0997878d-87ac-4327-b80d-b88e015aca22 name Betty
(hbnb) all User
["[User] (744fe833-e004-4011-ad8d-601516c237fe) {'id': '744fe833-e004-4011-ad8d-601516c237fe', 'created_at': datetime.datetime(2023, 12, 12, 1, 9, 0, 724627), 'updated_at': datetime.datetime(2023, 12, 12, 1, 9, 0, 724662)}", "[User] (0997878d-87ac-4327-b80d-b88e015aca22) {'id': '0997878d-87ac-4327-b80d-b88e015aca22', 'created_at': datetime.datetime(2023, 12, 12, 1, 9, 34, 638003), 'updated_at': datetime.datetime(2023, 12, 12, 1, 9, 34, 638033), 'name': 'Betty'}"]
(hbnb) destroy User 0997878d-87ac-4327-b80d-b88e015aca22
(hbnb) all User
["[User] (744fe833-e004-4011-ad8d-601516c237fe) {'id': '744fe833-e004-4011-ad8d-601516c237fe', 'created_at': datetime.datetime(2023, 12, 12, 1, 9, 0, 724627), 'updated_at': datetime.datetime(2023, 12, 12, 1, 9, 0, 724662)}"]
(hbnb) destroy User 744fe833-e004-4011-ad8d-601516c237fe
(hbnb) all User
[]
(hbnb) show User
** instance id missing **
(hbnb)

```

###### Example No.2

```
░▒▓    ~/ALX/AirBnB_clone  ./console.py 
(hbnb) User.create()
daa82102-ef67-4863-b7f4-7a45d8923514
(hbnb) User.all()
["[User] (daa82102-ef67-4863-b7f4-7a45d8923514) {'id': 'daa82102-ef67-4863-b7f4-7a45d8923514', 'created_at': datetime.datetime(2023, 12, 12, 1, 15, 59, 666742), 'updated_at': datetime.datetime(2023, 12, 12, 1, 15, 59, 666772)}"]
(hbnb) User.show()
** instance id missing **
(hbnb) User.show(daa82102-ef67-4863-b7f4-7a45d8923514)
[User] (daa82102-ef67-4863-b7f4-7a45d8923514) {'id': 'daa82102-ef67-4863-b7f4-7a45d8923514', 'created_at': datetime.datetime(2023, 12, 12, 1, 15, 59, 666742), 'updated_at': datetime.datetime(2023, 12, 12, 1, 15, 59, 666772)}
(hbnb) User.update("daa82102-ef67-4863-b7f4-7a45d8923514", "name", "Betty")
(hbnb) User.all()
["[User] (daa82102-ef67-4863-b7f4-7a45d8923514) {'id': 'daa82102-ef67-4863-b7f4-7a45d8923514', 'created_at': datetime.datetime(2023, 12, 12, 1, 15, 59, 666742), 'updated_at': datetime.datetime(2023, 12, 12, 1, 15, 59, 666772), 'name': 'Betty'}"]
(hbnb) User.destroy(daa82102-ef67-4863-b7f4-7a45d8923514)
(hbnb) User.all()
[]
(hbnb) quit
░▒▓    ~/ALX/AirBnB_clone 

```

### Acknowledgements
Thanks to all the peers who contributed their knowledge.

### Authors
* Mohamed AMEZZANE <[MedAmezzane](https://github.com/MedAmezzane)>
* Abdelouahed OUARRAR <[ouarrar](https://github.com/ouarrar)>
