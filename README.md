# WebJump Automation Project

To develop it, I've used these tools:

- Windows 10
- Python 3.7
- RobotFramework
- Chrome 80.0.3987.149
- Chrome WebDrive 80.0.3987.149

This project has the goal of automate webjump test plataform with structure using Robotframework in Python, also has
implementation of the design pattern page objects.

The project uses BDD to write test scenarios and it's structure was constructed to be similar with Cucumber implementation.

## Requirements

You'll need to install the following:

- Python: 3.x
    - Invoke Python Library
- Git

## Installation

You can install the project after having installed python 3.x using pip or invoke.

Using pip:
Run the the following command line in the project root path:

Using invoke:
First you will need to install invoke:

```python
$ pip install invoke
```

```python
$ pip install -r requirements.txt
```

Run the following command line in the project root path:

```python
$ invoke build
```

**This command should install all the libraries needed to run the project, if you got an error while trying to install the automationsetup then contact one of the owners or administrators of this project.**

To run the tests, you just need to run the following command:

```python
$ invoke robot -i webjump
```
