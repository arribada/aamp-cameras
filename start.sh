#!/bin/bash

# Start sshd if we don't use the init system
if [ "$INITSYSTEM" != "on" ]; then
  /usr/sbin/sshd -p 22 &
fi

export DBUS_SYSTEM_BUS_ADDRESS=unix:path=/host/run/dbus/system_bus_socket

# set -e

# Set host-name and enable-dbus
# sed -i -e "s@#enable-dbus=yes@enable-dbus=no@" -e "s@#host-name=foo@host-name=$(echo $RESIN_DEVICE_UUID | cut -c1-7)@" /etc/avahi/avahi-daemon.conf

# systemctl stop avahi-daemon &&

# avahi-daemon &

sleep 5

ifconfig wlan1 down

sleep 2

ifconfig wlan1 up

sleep 5

python ./activate_connection.py $ACCESS_POINT_NAME

sleep 5

# set more to BCM and then pull up pin 26
gpio -g mode 26 up

# Set the variable through command substitution
b=$(gpio -g read 26)

# Echo the value to the console so we know it's state
echo "$b"

if $b == "HIGH"
then

	echo "Entering debug mode"

	python cam_debug.py

else
	
	echo "Entering normal mode"

modprobe v4l2_common && python $CAMERA_MODE.py &
cd /data

#end by starting server
python -m SimpleHTTPServer 80

	.
fi
