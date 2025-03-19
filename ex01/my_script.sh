#!/bin/bash

pip --version

rm -rf local_lib

# https://pypi.org/project/path.py/
git clone https://github.com/jaraco/path local_lib

cd local_lib
pip install -e . >../path_install.log 2>&1
cd ..

if [ $? -eq 0 ]; then
    echo "Installation succeeded."
    python3 my_program.py
else
    echo "Installation failed. See path_install.log for details."
    exit 1
fi
