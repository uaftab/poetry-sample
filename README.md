# Readme

    pip3 install poetry --user
    export PATH=$PATH:~/.local/bin

    # Let poetry setup the deps + env
    poetry install

    # Update existing deps
    poetry update

    # Is everything working ?
    poetry run hello

    #To add a package
    poetry add <package name>
