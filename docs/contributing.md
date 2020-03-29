# Contributing guide

This section was prepared to act as a guide for those who wants to understand this project structure and patterns.

## Installation

You can install the project after having installed python 3.x using pip or invoke.

Using pip:
Run the the following command line in the project root path:

```python
$ pip install -r requirements.txt
```

Using invoke:
First you will need to install invoke:

```python
$ pip install invoke
```

Run the following command line in the project root path:

```python
$ invoke build
```

**This command should install all the libraries needed to run the project, if you got an error while trying to install the automationsetup then contact one of the owners or administrators of this project.**

If you want to see the task list that you can use with invoke follow the command bellow:

Invoke tasks list:

```python
$ invoke --list
```

## Standards

Please make sure you follow the bellow standards:

### Code conventions

We decided to use the [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/) for Python Code.

This project also use robotframework as the automation framework, use the [default documentation](https://robotframework.org/#documentation) to help [writting good test cases](https://github.com/robotframework/HowToWriteGoodTestCases/blob/master/HowToWriteGoodTestCases.rst) and also use [robotframework code conventions](https://www.slideshare.net/pekkaklarck/robot-framework-dos-and-donts).

## Work flow

To start the automation of a new feature:

- Feature should be already tested manually and has no bug opened related to it.
- Should has an opened ticket (story) to automate the target feature.
- Should has the test cases created on zaphyr and with automation fields filled properly and with the correct prioritization on it.
- The feature should be implemented using git flow as description on this guide.
- The feature should be automated inside its correct folder structure of the product it belongs.

To do maintenance on a existent feature:

- Feature should be already automated.
- Should has an opened ticket (story) to maintain the current feature.
- Feature should be receiving failed on its tests inside the Master branch. If a feature is failing just on the develop branch then it could be caused due to some new feature or fix added to develop branch. Please, always consider this.

To bring a new feature to automationsetup:

- Work in progress (please contact the owners or admininstrators of this project).

### Git flow

#### Branching model

- development: develop
  - The integration branch used for development. Feature branches are merged back into this branch
- production: master
  - The branch used for deploying releases. Typically, this branches from the development branch and changes are merged back into the development branch
- bugfix: bugfix/
  - Typically used for fixing bugs against a release branch
- features: feature/
  - Used for specific feature work. Typically, this branches from and merges back into the development branch
- hotfixes: hotfix/
  - Typically used to quickly fix the production branch (master)
- releases: release/
  - Used for release tasks and long-term maintenance. Typically, this branches from the development branch and changes are merged back into the development branch

#### Branch permissions

- master: production branch [protected]
- develop: default branch for merging and tests [protected]
  \*\*protected - prevent changes without pull request/ prevent from delete

#### Commits

Good commits messages can help the automation team and whoever has the necessity of maintain your code, a simple reference can be found on [erlang github repository](https://github.com/erlang/otp/wiki/writing-good-commit-messages).

#### Pull Requests

The only branches that requires pull requests for changes are master and develop, so, ensure you have tested your work on your branch and everything is working properly before opening a PR.

## Best Practices

To see our list of best practices and standards to this project, please, follow the link bellow.

Make sure to follow this guide so that everyone can work and collaborate together with less effort.

[Best Practices guide](./best_practices.md)
