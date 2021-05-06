# python-linting-test
Test project structure to linting and formatting using python

## What it uses?
This project uses multiples packages for linting, formating and git hooks, a list of the packeges used can be seen below:

* [black](https://github.com/psf/black) - Formats Python code without compromise.
* [flake8](https://github.com/PyCQA/flake8) - Capable of detecting both logical and stylistic lint. It adds the style and complexity checks of pycodestyle to the logical lint detection of PyFlakes. It combines the following linters: *PyFlakes*, *pycodestyle* (formerly pep8), *Mccabe*
* [bandit](https://github.com/PyCQA/bandit) - Analyzes code to find common security issues.
* [isort](https://github.com/PyCQA/isort) - Formats imports by sorting alphabetically and separating into sections.
* [pre-commit](https://github.com/pre-commit/pre-commit) - A framework for managing and maintaining multi-language pre-commit hooks.
* [.editorconfig](https://editorconfig.org/) - EditorConfig helps maintain consistent coding styles for multiple developers working on the same project across various editors and IDEs.

## How to install?

### Using requirements text file

First of all, you need a virtualenv and after that just install the packages from `requirements-dev.txt`:
```bash
# Creating a virtualenv
$ python -m virtualenv venv
$ source venv/bin/activate
# Installing packages
$ pip install -r requirements-dev.txt
```
### *But why it's using requirements-dev.txt and not requirements.txt*?
It's easier to keep separated the dev requirements from the production requirements, this is not necessary if the project uses `setup.py` or `setup.cfg`.

### Using `setup.py` or `setup.cfg`
The `setup.py` can contain every devepencies and develop depedencies using the param `extras_require`, to install the projects depedencies using `setup.py` it's only necessary to run the pip command:
```bash
$ pip install -e .
```
*Ps: the `-e`/`--editable` allow to install all dependecies but install the current package as a editable package*

To install all dev depedencies:
```bash
$ pip install -e .[dev]
# Some systems a error can occour (i experencied in zsh), a workaround is using the bellow command:
$ pip install -e ."[dev]"
```

## Usage with VsCode

You need to configure VsCode to use all packages, this can be done in the `.vscode/settings.json` file. A exemple file can be seen below:
```json
{
    "python.linting.enabled": true,
    "python.pythonPath": "venv/bin/python",
    "editor.formatOnSave": true,

    // Flake8 Configuration
    "python.linting.flake8Enabled": true,
    "python.linting.flake8Path": "venv/bin/flake8",
    "python.linting.flake8Args": ["--config=.flake8"],

    // bandit Configurations
    "python.linting.banditEnabled": true,
    "python.linting.banditPath": "venv/bin/bandit",

    // black configuration
    "python.formatting.provider": "black",
    "python.formatting.blackPath": "venv/bin/black"
}
```

## Usage with PyCharm
// TODO

## How Flake8 is configured?
Flake uses a `.flake8` file. In this file, you can configure any rules and disable if necessary.
Some disabled rules are:
 - E203: `Whitespace before ':' (E203)`
 - E266: `Missing whitespace around arithmetic operator (E226)`
 - E5001: `Line too long (82 &gt; 79 characters) (E501)` - Removed because another package will handle that.
 - W503: `Line break occurred before a binary operator (W503)` - Removed because another package will handle that.

 ## How black is configured?
 Black uses the `pyproject.toml`. The only configuration necessary is the `line-length` and the `exclude` to only execute for the files we care about (the `.py` files in the project).

 ## How iSort is configured?
 iSort uses the same `pyproject.toml`, need to have the same `line-lenght` as black and Flake8.

 ## How it all comes together? The answer is `pre-commit`
It's necessary to configure the git hooks using the command below:
```bash
$ pre-commit install
```
It will run every command configured on the `.pre-commit-config.yaml` file, if the developer runs a `git commit` command, it will check all staged files for lint errors, if a error occour, the commit will not continue until all errors are fixed. It's possible to run the command using command below and will check all files for lint errors:
```bash
pre-commit run -a
```

## Examples
This project contains 2 files with lint errors and without format.
to test it, just clone the project and install the depedencies and open the `example.py` and `other_example.py` files.