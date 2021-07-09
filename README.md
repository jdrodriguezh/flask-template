# Flask template for backend REST APIs (mostly) made with :heart: and :coffee:

![License](https://img.shields.io/github/license/jdrodriguezh/flask-template.svg) ![Issues](https://img.shields.io/github/issues/jdrodriguezh/flask-template.svg) ![forks](https://img.shields.io/github/forks/jdrodriguezh/flask-template) ![stars](https://img.shields.io/github/stars/jdrodriguezh/flask-template) ![size](https://img.shields.io/github/repo-size/jdrodriguezh/flask-template)

This is a template to start developing [Flask](https://flask.palletsprojects.com/en/2.0.x/) projects. The project includes sample tests with Python's built-in testing framework [unittest](https://docs.python.org/3/library/unittest.html), how the project folders should be structured and good practices of Python and Flask.

## Motivation :question:

Since a long time ago, I wanted to learn Python. I decided to start developing simple REST APIs to get going and this led me to this project!

## Installation :inbox_tray:


```bash

> git clone https://github.com/jdrodriguezh/flask-template

>  cd  flask-template

> pipenv shell

> pipenv install

> py ./run.py

```

## Bugs :bug:

This project is getting upgrades in my free time if there is a problem please create a bug report in the issues section.

## License :scroll:

- Licensed under [MIT License](https://github.com/jdrodriguezh/flask-template/blob/master/LICENSE)

## Available Scripts :scroll:

On the project root directory, you can run:

### `py ./run.py`

Runs the project in the development mode.

### `flask db init`

Adds the ```migrations``` folder to your project. This needs to be run only once, when running your first migration.

### `flask db migrate`

Generates the migration script.

### `flask db upgrade`

Applies the migration to the database.

**IMPORTANT:** Only ```flask db migrate``` and ```flask db upgrade``` need to be run every time the models change.

### `py -m unittest -v`

Runs all the tests in our ```/test``` folder.
