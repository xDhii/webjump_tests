from invoke import task
import os
import logging

try:
    from AutomationSetup import AutomationSetup
    s = AutomationSetup()
except ImportError:
    print("AutomationSetup is not already installed")
    print("Installing...")
    os.system(
        "pip install git+https://github.com/xDhii/automationsetup.git")
    from AutomationSetup import AutomationSetup
    s = AutomationSetup()

@task(
    help={
        "tests": "Directory that contains all suite tests. By default: tests",
        "profile": "Profile name defined on profiles.yaml file that contains the execution parameters. By default: default.",
        "include": "Tag(s) to include on the execution. By default: None.",
        "headless": "To set headless execution, it just needs to use this parameter without any value",
        "args": "String of arguments to include in the execution parameters. By default: None. e.g.: --args '-v COUNTRY:Hungary'",
        "processes": "Number of browsers threads/processes that will be executed in parallel, it will depend on the number of suites you are running."
        }
)
def pabot(c, tests="tests", profile="default", include=None, args=None, headless=False, processes="6", no_run=False):
    """Runs the project using default parameters that can also be overridden and using pabot as its runner.
       Pabot runs the project in parallel using the number of processes you give or by default uses 8.
       The number of browser(s)/parallel execution will be determined by the number of suites and processes you are running.
       For pabot documentation follow the link: https://github.com/mkorpela/pabot
       --help for usage"""

    s.robot_options = profile
    command = "pabot --processes " + processes + " --pabotlib "
    command += s.robot_options
    if include is not None:
        command = include_tag(command, include)
    command += " " + args if args is not None else ""
    if headless:
        command += " -v HEADLESS:True"
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
    logging.info(f"Running robot with the following command: {command} {tests}")
    if not no_run: c.run(command + " " + tests)

@task(
    help={
        "tests": "Directory that contains all suite tests. By default: tests",
        "profile": "Profile name defined on profiles.yaml file that contains the execution parameters. By default: default.",
        "include": "Tag(s) to include on the execution. By default: None.",
        "headless": "To set headless execution, it just needs to use this parameter without any value",
        "args": "String of arguments to include in the execution parameters. By default: None. e.g.: --args '-v COUNTRY:Hungary'",
        "no_run": "Will not execute the tests and just give the command to execute the tests through robot with the given arguments"
        }
)
def robot(c, tests="tests", profile="default", include=None, args=None, headless=False, no_run=False):
    """Runs the project using default parameters that can also be overridden. --help for usage"""
    s.robot_options = profile
    command = f"robot {s.robot_options}"
    if include is not None:
        command = include_tag(command, include)
    command += " " + args if args is not None else ""
    if headless: command += " -v HEADLESS:True"
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
    logging.info(f"Running robot with the following command: {command} {tests}")
    if not no_run: c.run(command + " " + tests)

@task(
    help={
        "file": "File to the dependencies that needs to be installed. By default: requirements.txt",
        "upgrade": "Boolean to check if the build will upgrade already installed dependencies",
        "user": "Boolean to define if the installation should be on the current user path"
    }
)
def build(c, file="requirements.txt", upgrade=False, user=False):
    """Builds the project installing/upgrading required packages, libraries and sources. --help for usage"""
    command = "pip install -r " + file
    if upgrade:
        command += " --upgrade"

    if user:
        command += " --user"

    c.run(command)


@task
def init(c):
    """Creates or updates the folder and files structure of the project. If the folder or file doesn't exists on the project it will create it. --help for usage"""
    print("WORKING IN PROGRESS... \nNOT DEVELOPED YET.")
    # s.create_workspace()

def include_tag(command, include):
    if "-i" in command:
        if "-" in command[(command.index("-i") + 1):(len(command))]:
            aux = command[(command.index("-i") + 1):(len(command))]
            include_tag = aux[0:(aux.index("-") - 1)] + "AND" + include + " "
            command = command[0:(command.index("-i"))] + "-" + include_tag + aux[aux.index("-"):len(aux)]
        else:
            command += "AND" + include
    else:
        command += "-i " + include
    return command
