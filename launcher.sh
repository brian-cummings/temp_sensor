#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python scrip$

cd /
cd home/pi/python/temp_sensor
python send_ip.py
python3 temp_sensor.py
