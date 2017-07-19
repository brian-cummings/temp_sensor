#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script

cd /
cd home/pi/python/temp_sensor
# Wait for network to be up (pinging Google)
while ! ping -c 1 -W 1 8.8.8.8; do
    sleep 1
done
sudo apt-get update
sudo apt-get -y dist-upgrade
sudo reboot
