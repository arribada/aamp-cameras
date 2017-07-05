#!/bin/bash

export DBUS_SYSTEM_BUS_ADDRESS=unix:path=/host/run/dbus/system_bus_socket

sleep 5

ifconfig wlan1 down

sleep 2

ifconfig wlan1 up

sleep 5

python ./activate_connection.py echo $ACCESS_POINT_NAME

modprobe v4l2_common && python cam-single-photo.py &
cd /data
python -m SimpleHTTPServer 80
