#!/usr/bin/env bash

# Change cwd to the script folder cwd
cd $(dirname $0)

stderrecho() {
    >&2 echo "${1:-A sample standard error message}"
}

stderrecho "This program use sudo to create files and folders in /opt"
stderrecho "Check the source code of this script in https://github.com/AlphaTechnolog/copier/blob/master/bin/install.sh"

if [ -d /opt/copier ]; then
    stderrecho "Already exists /opt/copier, removing it..."
    sudo rm -rf /opt/copier
fi

if [ -L /usr/bin/copier ]; then
    stderrecho "Already exists /usr/bin/copier, removing it..."
    sudo rm /usr/bin/copier
fi

if [ -d .copier-install-tmp ]; then
    rm -rf ./.copier-install-tmp
fi

mkdir -p .copier-install-tmp
cd .copier-install-tmp

if [ -f .copier-install-error ]; then
    rm .copier-install-error
fi

printf "Downloading the copier source code... "
git clone https://github.com/AlphaTechnolog/copier.git copier-src > /dev/null 2> .copier-install-error
status_code=$?

if [[ $status_code != 0 ]]; then
    cd ..
    rm -rf .copier-install-tmp
    error "FAILURE... An error was ocurred when I download copier: " $(cat .copier-install-error)
fi

printf "OK.\nMoving the source code to /opt/copier... "
cd ./copier-src
python3 -m pip install -r ./requirements.txt
cd ..
sudo mv ./copier-src /opt/copier
sudo chmod -R 777 /opt/copier /opt/copier/*
cd ..
rm -rf ./.copier-install-tmp
printf "OK.\nCreating the symbolic link to execute it on your \$PATH... "
sudo ln -s /opt/copier/copier.py /usr/bin/copier
sudo chmod -R 777 /usr/bin/copier
echo "OK. type \"copier\" to start!"
