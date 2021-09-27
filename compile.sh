#!/bin/bash

cd $(dirname $0)

if [ -f "/bin/python3" ] && [ -f "/bin/pip3" ]
then
	echo "Python3 and Pip3 installed"
	rm -vrf bin/*
	mkdir -p bin/
	pip3 install pyinstaller pyqt5
	pyinstaller --distpath bin/ -F -n visual-idur src/init.py
	if [ $(uname -m) = "x86_64" ]
	then
		tar -cvzf bin/visual-idur-x86_64.tar.gz bin/visual-idur
	else
		tar -cvzf bin/visual-idur-i386.tar.gz bin/visual-idur
	fi
else
	echo "Install python3 or/and python3-pip"
fi
