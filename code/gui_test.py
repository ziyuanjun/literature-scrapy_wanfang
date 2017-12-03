#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui, QtCore


def run():
    print('Hello World!')

app = QtGui.QApplication(sys.argv)
widget = QtGui.QWidget()
widget.resize(250, 150)
widget.setGeometry(300, 300, 250, 150)
widget.setWindowTitle(u'欢迎使用')
quit = QtGui.QPushButton('执行', widget)
quit.setGeometry(10, 10, 60, 35)
quit.clicked.connect(run)
widget.show()

sys.exit(app.exec_())
