# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_test.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QFileDialog, QDialog
from PyQt4.QtCore import QDir
import os

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_Dialog(QtGui.QWidget):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(430, 242)
        self.horizontalLayoutWidget = QtGui.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 391, 71))
        self.horizontalLayoutWidget.setObjectName(
            _fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.txt_netfile = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.txt_netfile.setObjectName(_fromUtf8("txt_netfile"))
        self.horizontalLayout.addWidget(self.txt_netfile)
        self.btn_browseNetfile = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btn_browseNetfile.setObjectName(_fromUtf8("btn_browseNetfile"))
        self.horizontalLayout.addWidget(self.btn_browseNetfile)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(Dialog)
        self.horizontalLayoutWidget_2.setGeometry(
            QtCore.QRect(20, 80, 391, 71))
        self.horizontalLayoutWidget_2.setObjectName(
            _fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(
            self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.txt_download_dir = QtGui.QLineEdit(self.horizontalLayoutWidget_2)
        self.txt_download_dir.setObjectName(_fromUtf8("txt_download_dir"))
        self.horizontalLayout_2.addWidget(self.txt_download_dir)
        self.btn_browsepdfdir = QtGui.QPushButton(
            self.horizontalLayoutWidget_2)
        self.btn_browsepdfdir.setObjectName(_fromUtf8("btn_browsepdfdir"))
        self.horizontalLayout_2.addWidget(self.btn_browsepdfdir)
        self.horizontalLayoutWidget_3 = QtGui.QWidget(Dialog)
        self.horizontalLayoutWidget_3.setGeometry(
            QtCore.QRect(20, 150, 341, 41))
        self.horizontalLayoutWidget_3.setObjectName(
            _fromUtf8("horizontalLayoutWidget_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(
            self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(self.horizontalLayoutWidget_3)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.isName = QtGui.QCheckBox(self.horizontalLayoutWidget_3)
        self.isName.setObjectName(_fromUtf8("isName"))
        self.horizontalLayout_3.addWidget(self.isName)
        self.isYear = QtGui.QCheckBox(self.horizontalLayoutWidget_3)
        self.isYear.setObjectName(_fromUtf8("isYear"))
        self.horizontalLayout_3.addWidget(self.isYear)
        self.btn_run = QtGui.QPushButton(Dialog)
        self.btn_run.setGeometry(QtCore.QRect(310, 200, 99, 27))
        self.btn_run.setObjectName(_fromUtf8("btn_run"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.btn_run.clicked.connect(self.run)
        self.btn_browseNetfile.clicked.connect(self.btn_browseNetfile_clicked)
        self.btn_browsepdfdir.clicked.connect(self.btn_browsepdfdir_clicked)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "欢迎使用", None))
        self.label.setText(_translate("Dialog", "题录文件", None))
        self.btn_browseNetfile.setText(_translate("Dialog", "浏览", None))
        self.label_2.setText(_translate("Dialog", "保存路径", None))
        self.btn_browsepdfdir.setText(_translate("Dialog", "浏览", None))
        self.label_3.setText(_translate("Dialog", "文件名前缀：", None))
        self.isName.setText(_translate("Dialog", "姓名", None))
        self.isYear.setText(_translate("Dialog", "年份", None))
        self.btn_run.setText(_translate("Dialog", "执行", None))

    def btn_browseNetfile_clicked(self):
        # absolute_path is a QString object
        absolute_path = QFileDialog.getOpenFileName(self, 'Open file',
                                                    '.', "Net files (*.Net)")
        if absolute_path:
            self.txt_netfile.setText(absolute_path)
            print(relative_path)

    def btn_browsepdfdir_clicked(self):
        cwd = os.getcwd()
        absolute_path = QFileDialog.getExistingDirectory(self, '选择路径', '.')
        if absolute_path:
            self.txt_download_dir.setText(absolute_path)

    def run(self):
        print(self.txt_netfile.text())
        print(self.txt_download_dir.text())
        print(self.isName.isChecked())
        print(self.isYear.isChecked())

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
