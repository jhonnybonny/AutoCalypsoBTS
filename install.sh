#!/bin/sh

echo -e "\e[30;41m
Installing Auto CalypsoBTS       
\e[0m"
sleep 3
pip3 install pyautogui >/dev/null 2>&1
sleep 3
sudo cp smS.py /usr/src/CalypsoBTS
sudo cp sub.py /usr/src/CalypsoBTS
sudo chmod 777 autocalypsobts/console.sh autocalypsobts/nitb.sh autocalypsobts/osmobts.sh autocalypsobts/transceiver.sh autocalypsobts/trx.sh autocalypsobts/trx2.sh autocalypsobts/autobts.py
echo -e "\e[32m
Done !
\e[0m"

echo -e "\e[30;41m
If u wanna open AutoCalypsoBTS 
Use : cd autocalypsobts && sudo python3 autobts.py     
\e[0m"
