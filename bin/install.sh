#!/usr/bin/env bash

# Change cwd to the script folder cwd
cd $(dirname $0)

stderrecho() {
    >&2 echo "${1:-A sample standard error message}"
}

error() {
    stderrecho $1
    exit 1
}

confirm() {
    # call with a prompt string or use a default
    read -r -p "${1:-Are you sure? [y/N]} " response
    case "$response" in
        [yY][eE][sS]|[yY]) 
            true
            ;;
        *)
            false
            ;;
    esac
}

stderrecho "This program uses sudo to create files and folders in /opt"
stderrecho "Check the source code of this script in ..."

if [ -d /opt/copier ]; then
    if confirm "Already exists /opt/copier, delete it? [y/N]"; then
        sudo rm -rf /opt/copier
    else
        error "Already exists /opt/copier, the user not delete the folder"
    fi
fi

if [ -f /usr/bin/copier ]; then
    if confirm "Already exists /usr/bin/copier, delete it? [y/N]"; then
        sudo rm /usr/bin/copier
    else
        echo "Already exists /usr/bin/copier, the user not delete the file"
    fi
fi

mkdir .copier-install-tmp
cd .copier-install-tmp

if [ -f .copier-install-error ]; then
    rm .copier-install-error
fi

printf "Downloading the copier source code..."
git clone https://github.com/AlphaTechnolog/copier.git copier-src > /dev/null 2> .copier-install-error
status_code=$?

if ! status_code; then
    cd ..
    rm -rf .copier-install-tmp
    error "FAILURE... An error was ocurred when I download copier: " $(cat .copier-install-error)
fi

printf "OK.\nMoving the source code to /opt/copier"
sudo mv ./copier-src /opt/copier
sudo chmod -R 777 /opt/copier /opt/copier/*
printf "OK.\nCreating the symbolic link to execute it on your \$PATH..."
sudo ln -s /opt/copier/copier.py /usr/bin/copier
sudo chmod -R 777 /usr/bin/copier
echo "OK. type \"copier\" to start!"