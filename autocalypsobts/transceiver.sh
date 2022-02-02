#!/bin/sh
#edit sudo ./transceiver -a (clock arfcn) 

cd /usr/src/CalypsoBTS
echo "CLOCK"
sudo ./transceiver -a 606
read e 
