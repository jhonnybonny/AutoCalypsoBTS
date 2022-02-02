#!/bin/sh

echo -e "\e[30;41m
Installing Auto CalypsoBTS       
\e[0m"
sleep 4
pip3 install pyautogui >/dev/null 2>&1
sleep 3
sudo cp smS.py /usr/src/CalypsoBTS
sudo cp sub.py /usr/src/CalypsoBTS
echo -e "\e[32m
Done !
\e[0m"

echo -e "\e[30;41m
If u wanna open AutoCalypsoBTS 
Use : cd autocalypsobts && sudo python3 autobts.py     
\e[0m"
