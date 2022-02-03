#!/bin/sh
#edit sudo ./transceiver -a (clock arfcn) 
#!!!!!!!!!!!!!!! use -2 key if u have 2 or more phones !!!!!!!!!!!!!!!!!!!!!!!
cd /usr/src/CalypsoBTS
echo "CLOCK"
sudo ./transceiver -a 606 
read e 
