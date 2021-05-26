#!/bin/bash

#Check root
if [ "$EUID" -ne 0 ]
	then echo "Run as root!"
	exit
fi

#----------
# Variables
#----------
# Help APT to know when apt update was performed
APT_UPDATED=0

# Get & store kernel codename
LINUX_CODENAME=$(dpkg --status tzdata|grep Provides|cut -f2 -d'-')

# Check & store if is ARM or x86 system
LINUX_RUNNING_ARM=$(if [ $(uname -m | grep 'armv7') ]; then echo "arm"; else echo "x86"; fi) # Only support ARMv7 or x86

if [ $# -eq 0 ]; then
	INSTALL_DIR='/opt/BrunoNatali/'
else 
	INSTALL_DIR=$1
fi
echo "App will be installed into: $INSTALL_DIR"
echo "Press ctrl + C to abort ... "
COUNTER=0
TEMP_C=10
while [  $COUNTER -lt 10 ]; do
    echo -n "${TEMP_C} "
    sleep 1
    let COUNTER=COUNTER+1 
    let TEMP_C=TEMP_C-1
done

echo " "
if [ ! -d "$INSTALL_DIR" ]; then
    mkdir -p "$INSTALL_DIR" 2> /dev/null
    chmod -R 777 "$INSTALL_DIR" 2> /dev/null # This is not secure, but work 
fi

if [ ! -f "INSTALL.path" ] || [ $INSTALL_DIR != $(<INSTALL.path)]; then
    sh -c "echo $INSTALL_DIR > INSTALL.path" 
fi

# Check if program is installed & install if necessary
check_app_installed()
{
    echo -n "$1 ... "

    printf "$INSTALLED_APPS" | grep $1 > /dev/null 2>&1
    if [ $? -eq 0 ]; then 
        echo "OK"
    else 
        if [[ $APT_UPDATED == 0 ]]; then
            echo -n "Updating apt: "
            apt update 1> /dev/null 2> /tmp/install-web.error
            if [[ $? != 0 ]]; then 
                echo "FAIL"
                cat /tmp/install-web.error
                exit 1
            fi
            echo -n "OK ... "
            sleep 2
            APT_UPDATED=1
        fi

        if [[ "${1: -1}" == "-" ]]; then
            echo -n "Last ver: "
            APP_AVAILABLE_VERSION_FULL=$(apt-cache policy "${1}*" 2> /tmp/install-web.error | head -1) 
            APP_AVAILABLE_VERSION=$(echo "${APP_AVAILABLE_VERSION_FULL: ${#1}}" | awk -F- '{print $1}')
            echo -n "$APP_AVAILABLE_VERSION ... "
        else 
            APP_AVAILABLE_VERSION=""
        fi

        echo -n "Installing: "

        export DEBIAN_FRONTEND=noninteractive
        apt install -y "${1}${APP_AVAILABLE_VERSION}" 1> /dev/null 2> /tmp/install-web.error
        if [ $? -eq 0 ]; then 
            echo "OK"
            FORCE_SERVICE_RESTART=1
        else
            echo "FAIL"
            cat /tmp/install-web.error
            unset DEBIAN_FRONTEND
            exit 1
        fi
        unset DEBIAN_FRONTEND
    fi
}

echo "Verifying installed apps ..."
INSTALLED_APPS=$(dpkg -l | grep -E '^ii')
REQUIRED_APPS=(\
'python3.9' \
'python3-pip' \
'python3-venv' \
'nodejs' \
'npm' \
)
for i in "${REQUIRED_APPS[@]}"; do
    check_app_installed $i
done

echo ""
echo "APPs version:"
python3 -V
echo -n "Node "
nodejs -v
echo ""