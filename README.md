# PYPG

Generate a python package within seconds

## Installation

git clone the repository and run the following command in the root directory of the repository

```bash
pip install .
``` 

## Usage

```bash
python -m PYPG -n <package_name>
```

```
usage: __main__.py [-h] -n NAME [-p PATH] [-v VERSION] [-a AUTHOR] [-e EMAIL] [-d DESCRIPTION]

Python package generator

optional arguments:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  Package name
  -p PATH, --path PATH  Package path (default: current directory)
  -v VERSION, --version VERSION
                        Package version
  -a AUTHOR, --author AUTHOR
                        Package author
  -e EMAIL, --email EMAIL
                        Author email
  -d DESCRIPTION, --description DESCRIPTION
                        Package description
```