# Python template project

This is a sample Python project with no extra dependencies.

## About this template

Hi, I created this template to help you get started with a new project in the WESCO organisation

Some decisions I have made while creating this template are:

- Create a project structure that is as modular as possible.
- Keep it simple and easy to maintain.
- Allow for a lot of flexibility and customizability.
- Low dependency (this template doesn't have dependencies)

Note: After creating the repo please use the rename the sample to your desired project name and please do the change of the name in `Makefile` and `setup.py` file.

## Future Support

- Other template such as flask, fastapi and etc to be added into make init support

## Structure

Lets take a look at the structure of this template:

```text
├── Containerfile                   # The file to build a container using buildah or docker
├── docs                            # Documentation site (add more .md files here)
│   └── index.md                    # The index page for the docs site we are using mkdocs visit [mkdocs.org](https://www.mkdocs.org)
├── .github                         # Github metadata for repository
│   ├── PULL_REQUEST_TEMPLATE.md    # Pull request template going to be used while raising a request
│   └── workflows                   # The CI pipeline for Github Actions
├── .gitignore                      # A list of files to ignore when pushing to Github
├── CHANGELOG.md                      # Auto generated list of changes to the project
├── Makefile                        # A collection of utilities to manage the project
├── mkdocs.yml                      # Configuration for documentation site
├── sample                          # The main python package for the project, make sure to rename this and do the same in setup.py and Makefile as well.
│   ├── base.py                     # The base module for the project
│   ├── __init__.py                 # This tells Python that this is a package
│   ├── __main__.py                 # The entry point for the project
├── README.md                       # The main readme for the project
├── setup.py                        # The setup.py file for installing and packaging the project
├── requirements.txt                # An empty file to hold the requirements for the project
├── requirements-test.txt           # List of requirements for testing and devlopment
├── setup.py                        # The setup.py file for installing and packaging the project
└── tests                           # Unit tests for the project (add mote tests files here)
    ├── conftest.py                 # Configuration, hooks and fixtures for pytest
    ├── __init__.py                 # This tells Python that this is a test package
    └── test_base.py                # The base test case for the project
```

## FAQs

Frequent asked questions.

### Why this template is not using [Poetry](https://python-poetry.org/) ?

Peotry is an awesome tool for mananging python dependencies but it seems for the base project it would not be fare to add an underlyning dependency manager and restrict other contributors,
if you want to switch to poetry, you can run `make switch-to-poetry`.

Setuptools is the most simple and well supported way of packaging a Python project,
it doesn't require extra dependencies and is the easiest way to install the project.

### Why the `requirements.txt` is empty ?

This template is a low dependency project, so it doesn't have any extra dependencies.
You can add new dependencies as you will or you can use the `make init` command to
generate a `requirements.txt` file based on the template you choose `flask, fastapi, click etc`.

### Why there is a `requirements-test.txt` file ?

This file lists all the requirements for testing and development,
I think the development environment and testing environment should be as similar as possible.

Except those tools that are up to the developer choice (like ipython, ipdb etc).

People automating CI for your project will be grateful for having a setup.py file

### Why isn't this template made as a cookiecutter template?

I really like [cookiecutter](https://github.com/cookiecutter/cookiecutter) and it is a great way to create new projects, But for this approach where we are using a git hub app to create new repo with a user selection template, this would be the best way possible.

Also, to use this template doesn't require to install extra tooling such as cookiecutter.

### Why `VERSION` is kept in a static plain text file?

I used to have my version inside my main module in a `__version__` variable, then
I had to do some tricks to read that version variable inside the setuptools
`setup.py` file because that would be available only after the installation.

I decided to keep the version in a static file because it is easier to read from
wherever I want without the need to install the package.

e.g: `cat project_name/VERSION` will get the project version without harming
with module imports or anything else, it is useful for CI, logs and debugging.

### Why to include `tests`, `CHANGELOG` and `Dockerfile` as part of the release?

The `Dockerfile` file is used to create docker image which will be later on used to deploy into our kubernetes clustor.

The `CHANGELOG` file is used to create a release/change log history template, please follow the [https://keepachangelog.com/en/1.0.0/](guidelines)

The `tests` are for adding any test case which are been tested by pytest utility.

### Why conftest includes a go_to_tmpdir fixture?

When your project deals with file system operations, it is a good idea to use
a fixture to create a temporary directory and then remove it after the test.

Before executing each test pytest will create a temporary directory and will
change the working directory to that path and run the test.

So the test can create temporary artifacts isolated from other tests.

After the execution Pytest will remove the temporary directory.

### Why this template is using [pre-commit](https://pre-commit.com/) ?

pre-commit is an excellent tool to automate checks and formatting on your code.

### Is there a Linting and auto formatter in place ?

Yes, I have set up a linter and formatter with help of tools such [https://pypi.org/project/flake8/](flake8) and [https://github.com/psf/black](Black).Checks and formatting as simple commands on the [Makefile](Makefile)
makes it easier to undestand and change.Just run `make lint` and `make formatt`

### Why the CLI is not using click?

I wanted to provide a simple template for a CLI application on the project main entry point
click and typer are great alternatives but are external dependencies and this template
doesn't add dependencies besides those used for development.

### Why this doesn't provide a full example of application using Flask or Django?

as I said before, I want it to be simple and multipurpose, so I decided to not include
external dependencies and programming design decisions.

It is up to you to decide if you want to use Flask or Django and to create your application
the way you think is best.

This template provides utilities in the Makefile to make it easier to you can run:

```bash
$ make init
Make init does not support any template for now this will be part of future releases for now reuse the repo as per your need but don't change the CICD or the project initial structure.
```

Then the above will download the Flask template and apply it to the project.

## The Makefile

All the utilities for the template and project are on the Makefile

```bash
❯ make
Usage: make <target>

Targets:
help:             ## Show the help.
install:          ## Install the project in dev mode.
formatt:              ## Format code using black & isort.
lint:             ## Run pep8, black, mypy linters.
test:             ## Run tests and generate coverage report.
watch:            ## Run tests on every change.
clean:            ## Clean unused files.
virtualenv:       ## Create a virtual environment.
release:          ## Create a new tag for release.
docs:             ## Build the documentation.
switch-to-poetry: ## Switch to poetry package manager.
init:             ## Initialize the project based on an application template.
```
