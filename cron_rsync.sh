#!/bin/bash

# ping the basestation 13d77c3.local to see if the network is up
ping -c4 13d77c3.local > /dev/null
 
if [ $? != 0 ] 

  echo "Basestation not reachable just yet"

then

  echo "Looks good, starting rsync"
  
fi
