#!/bin/bash

cd $(dirname $0)

if [ -f "/bin/python3" ] && [ -f "/bin/pip3" ]
then
	echo "Python3 and Pip3 installed"
	rm -vrf export/*
	mkdir -p export/
	pip3 install pyinstaller pyqt5
	pyinstaller --distpath export/ -F -n visual-idur src/init.py
else
	echo "Install python3 or/and python3-pip"
fi
