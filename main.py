# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from helpers.serial import Test
from helpers.usb import USB
from threading import Timer
from PyQt5.QtCore import QTimer
import subprocess


class Ui_Form(QtCore.QObject):

    def __init__(self, parent=None):
        super(Ui_Form, self).__init__(parent)
        self.ts=Test()
        self.usb=USB()
        self.usb_path=self.usb.path
        self.timer=QTimer()
        screens=app.screens()
        self.sc_dpi=[dpi.logicalDotsPerInch() for dpi in screens]
        self.comPorts=[]
        self.update_flag = False
                

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(303, 354)
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.currentIndexChanged.connect(self.set_port1_485)
        self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.pressed.connect(self.test_485)
        self.gridLayout.addWidget(self.pushButton, 1, 3, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.currentIndexChanged.connect(self.set_port2_485)
        self.gridLayout.addWidget(self.comboBox_2, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setToolTipDuration(1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.pressed.connect(self.cont_test_485)
        self.gridLayout.addWidget(self.pushButton_2, 2, 3, 1, 1)
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 3, 0, 2, 4)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 2, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(Form)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.currentIndexChanged.connect(self.set_port_232)
        self.gridLayout.addWidget(self.comboBox_3, 5, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 2, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 5, 3, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setToolTipDuration(1)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.pressed.connect(self.cont_test_232)
        self.gridLayout.addWidget(self.pushButton_4, 6, 3, 1, 1)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 7, 0, 2, 4)
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 8, 2, 1, 1)
        self.comboBox_4 = QtWidgets.QComboBox(Form)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.currentTextChanged.connect(self.change_usb_path)
        self.gridLayout.addWidget(self.comboBox_4, 9, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 9, 2, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.pressed.connect(self.test_usb)
        self.gridLayout.addWidget(self.pushButton_5, 9, 3, 1, 1)
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 10, 0, 1, 4)
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 11, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 11, 1, 1, 2)

        self.ts.statusChange.connect(lambda: self.line_refresh())
        self.timer.timeout.connect(self.list_coms)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.list_coms()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "HUB TEST"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">RS485</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "PORT1_485"))
        self.pushButton.setText(_translate("Form", "TEST PORTS"))
        self.label_4.setText(_translate("Form", "PORT2_485"))
        self.pushButton_2.setWhatsThis(_translate("Form", "Send data continuously until communication brakes"))
        self.pushButton_2.setText(_translate("Form", "CONNECT"))
        self.label_6.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">RS232</span></p></body></html>"))
        self.label_5.setText(_translate("Form", "PORT_232"))
        self.pushButton_3.setText(_translate("Form", "TEST PORTS"))
        self.pushButton_4.setWhatsThis(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">Send data continuously until communication brakes</span></p></body></html>"))
        self.pushButton_4.setText(_translate("Form", "CONNECT"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">USB</span></p></body></html>"))
        self.label_8.setText(_translate("Form", "Select Flash Drive"))
        self.pushButton_5.setText(_translate("Form", "TEST PORT"))
        self.label.setText(_translate("Form", "STATUS:"))

    

    def list_coms(self):
        self.usb_ports=self.usb.usb_ports_refresh()
        self.update_flag = False
        self.comboBox_4.clear()
        self.update_flag = False
        self.set_usb_ports()
        if self.comPorts!=self.ts.listPorts():
            self.comPorts=self.ts.listPorts()
        #if self.comboBox.currentIndex()==-1:
            #ports=self.ts.listPorts()
            self.comboBox.clear()
            self.comboBox_2.clear()
            self.comboBox_3.clear()
            for p in self.comPorts:
                self.comboBox.addItem(p)
                self.comboBox_2.addItem(p)
                self.comboBox_3.addItem(p)
        self.timer.start(5000)
                

    def set_port1_485(self):
        self.ts.Port1_485=self.comboBox.currentText()

    def set_port2_485(self):
        self.ts.Port2_485=self.comboBox_2.currentText()

    def set_port_232(self):
        self.ts.Port_232=self.comboBox_3.currentText()

    def test_485(self):
        self.lineEdit.setText(" ")
        QApplication.processEvents()
        self.ts.RS485_Test()
        self.lineEdit.setText(self.ts.status)

    def test_232(self):
        self.lineEdit.setText(" ")
        QApplication.processEvents()
        self.ts.RS232_Test()
        self.lineEdit.setText(self.ts.status)

    def cont_test_485(self):
        self.lineEdit.setText(" ") 
        QApplication.processEvents()
        self.ts.RS485_Continuous()
        self.lineEdit.setText(self.ts.status)

    def cont_test_232(self): 
        self.lineEdit.clear()
        QApplication.processEvents()
        self.ts.RS232_Continuous()
        self.lineEdit.setText(self.ts.status)

    def line_refresh(self):	
        self.lineEdit.setText(self.ts.status)
        QApplication.processEvents()

    def set_usb_ports(self):
        if sys.platform != "win32":
            for port in self.usb_ports:
                self.comboBox_4.addItem(port["tag"].decode() + "@" + port["device"])
        else:
            for port in self.usb_ports:
                    self.comboBox_4.addItem(port)
            QApplication.processEvents()

    def change_usb_path(self):
        if sys.platform != "win32":
            self.usb_path=self.comboBox_4.currentText().rsplit("@",1)[1] + "newfile.txt"
            if self.update_flag == True:
                self.mount_usb_drive()
        else:
            self.usb_path=self.comboBox_4.currentText() + "newfile.txt"
        self.update_flag = True

    def mount_usb_drive(self, usb_path):
        mount_name = "usb_drive"
        try:
            subprocess.run([f"sudo mkdir /media/{mount_name}"], check = True)
            subprocess.run([f"sudo mount {usb_path} /media/{mount_name}"], check = True)
        except Exception as e:
            print (str(e))

    
    def test_usb(self):
        self.lineEdit.setText(" ")
        QApplication.processEvents()
        self.usb.Wspeed_test(self.usb_path,self.usb.built_str(375000))
        self.lineEdit.setText(self.usb.status)
            

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
