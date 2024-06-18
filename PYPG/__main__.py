# Python package generator
# Generate a python package within seconds
# Github: https://www.github.com/0x4248/python_package_generator
# Licence: GNU General Public Licence v3.0
# By: 0x4248

import os
import sys
import argparse


def main():
    parser = argparse.ArgumentParser(description='Python package generator')
    parser.add_argument('-n', '--name', help='Package name', required=True, type=str)
    parser.add_argument('-p', '--path', help='Package path (default: current directory)', default=os.getcwd(), type=str)
    parser.add_argument('-v', '--version', help='Package version', type=str, default="0.1.0")
    parser.add_argument('-a', '--author', help='Package author', default="", type=str)
    parser.add_argument('-e', '--email', help='Author email', default="", type=str)
    parser.add_argument('-d', '--description', help='Package description', default="", type=str)

    args = parser.parse_args()

    setup_py = f"""from setuptools import setup

setup(
    name='{args.name}',
    version='{args.version}',
    author='{args.author}',
    author_email='{args.email}',
    description='{args.description}',
    packages=['{args.name}'],
    install_requires=[],
)
"""
    folders = ["docs", "tests", args.name, "scripts"]
    files = ["LICENSE", "requirements.txt"]

    for folder in folders:
        os.makedirs(os.path.join(args.path, folder), exist_ok=True)

    for file in files:
        open(os.path.join(args.path, file), "w").close()
    
    with open(os.path.join(args.path, "setup.py"), "w") as f:
        f.write(setup_py)

    with open(os.path.join(args.path, args.name, "__init__.py"), "w") as f:
        f.write("")

    with open(os.path.join(args.path, "README.md"), "w") as f:
        f.write(f"# {args.name}\n\n{args.description}")

if __name__ == "__main__":
    main()