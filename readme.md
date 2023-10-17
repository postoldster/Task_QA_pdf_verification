Project description
    The development contains a method for the input of which a PDF file is submitted, and the output returns data in the form of a dictionary.
    As well as methods for checking pdf files for the presence of all elements and compliance with the structure

Installation
    create and activate venv.
    run command to install required packeges:
        pip install -r requirements.txt
    Required installation Zbar library. Follow instruction for you OS:
        https://pypi.org/project/pyzbar/

    Tip for MacOS:
        fix error: 'Unable to find zbar shared library'
        mkdir ~/lib
        ln -s $(brew --prefix zbar)/lib/libzbar.dylib ~/lib/libzbar.dylib

Run test
    execute command to run tests:
        pytest

