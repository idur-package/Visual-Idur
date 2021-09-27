cd $(dirname 0)

pyuic5 -x design/main.ui -o src/mainDesign.py
pyuic5 -x design/input.ui -o src/inputDesign.py
pyuic5 -x design/message.ui -o src/messageDesign.py
