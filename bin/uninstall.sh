# Change cwd to the script folder cwd
cd $(dirname $0)

stderrecho() {
    >&2 echo "${1:-A sample standard error message}"
}

error () {
    stderrecho "$1"
    exit 1
}

stderrecho "This program use sudo to delete files and folders in /opt and in /usr/share/copier"
stderrecho "Check the source code of this script in https://github.com/AlphaTechnolog/copier/blob/master/bin/install.sh"

if [ ! -d /opt/copier ]; then
    error "/opt/copier does not exists, first run the copier install.sh script"
fi

if [ ! -L /usr/bin/copier ]; then
    error "/usr/bin/copier does not exists, first run the copier install.sh script"
fi

printf "Removing folder /opt/copier... "
sudo rm -rf /opt/copier
printf "OK.\nRemoving file /usr/bin/copier... "
sudo rm /usr/bin/copier
echo "OK, copier is uninstalled."