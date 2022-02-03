#!/bin/sh
#edit sudo ./osmocon -m c123xor -p /dev/ttyUSB1 -s /tmp/osmocom_l2.2 -c firmwares/compal_e88/trx.highram.bin
#MOBILE2
cd /usr/src/CalypsoBTS
echo "P R E S S   P O W E R   B U T T O N 2"
sudo ./osmocon -m c123xor -p /dev/ttyUSB1 -s /tmp/osmocom_l2.2 -c firmwares/compal_e88/trx.highram.bin
read e

