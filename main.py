# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from helpers.serial import Test
from helpers.usb import USB
from threading import Timer
from PyQt5.QtCore import QTimer


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
                

    def setupUi(self, Form):
        try:
            if self.sc_dpi[0]!=self.sc_dpi[1]:
                m=1.5
            else:
                m=1
        except:
            m=1
        Form.setObjectName("Form")
        Form.resize(int(316*m), 418)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(int(70*m), 370,int(221*m), 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 370, int(61*m), int(16*m)))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox_3 = QtWidgets.QComboBox(Form)
        self.comboBox_3.setGeometry(QtCore.QRect(30, 160, int(81*m), int(22*m)))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.currentIndexChanged.connect(self.set_port_232)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(int(120*m), 160, int(71*m), int(21*m)))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(int(210*m), 190, int(71*m), 31))
        self.pushButton_4.setToolTipDuration(1)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.pressed.connect(self.cont_test_232)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(int(210*m), 150, int(71*m), 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.pressed.connect(self.test_232)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(30, 40, int(81*m), int(22*m)))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.currentIndexChanged.connect(self.set_port1_485)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(int(120*m), 70, int(71*m), int(21*m)))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(int(120*m), 40, int(71*m), int(21*m)))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(int(210*m), 70, int(71*m), 31))
        self.pushButton_2.setToolTipDuration(1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.pressed.connect(self.cont_test_485)
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(30, 70, int(81*m), int(22*m)))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.currentIndexChanged.connect(self.set_port2_485)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(int(210*m), 30, int(71*m), 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.pressed.connect(self.test_485)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(int(150*m), 10, int(41*m), int(21*m)))
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(int(150*m), 130, int(41*m), int(21*m)))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(int(150*m), 250, int(41*m), int(21*m)))
        self.label_7.setObjectName("label_7")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(int(210*m), 280, int(71*m), 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.pressed.connect(self.test_usb)
        self.comboBox_4 = QtWidgets.QComboBox(Form)
        self.comboBox_4.setGeometry(QtCore.QRect(30, 290,int( 81*m), int(20*m)))
        self.comboBox_4.setObjectName("combobox_4")
        #self.comboBox_4.currentIndexChanged.connect(self.set_usb_path)
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(int(120*m), 290, int(71*m), int(21*m)))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(10, 240, int(301*m), int(16*m)))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(10, 350, int(301*m), int(16*m)))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(10, 120, int(301*m), int(16*m)))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.ts.statusChange.connect(lambda: self.line_refresh())
        self.timer.timeout.connect(self.list_coms)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "HUB TEST"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:8pt;\">STATUS</span></p></body></html>"))
        self.label_5.setText(_translate("Form", "PORT_232"))
        self.pushButton_4.setWhatsThis(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">Send data continuously until communication brakes</span></p></body></html>"))
        self.pushButton_4.setText(_translate("Form", "CONNECT"))
        self.pushButton_4.setStyleSheet('QPushButton {font: 7pt "MS Shell Dlg 2";}')
        self.pushButton_3.setText(_translate("Form", "TEST PORTS"))
        self.pushButton_3.setStyleSheet('QPushButton {font: 7pt "MS Shell Dlg 2";}')
        self.label_4.setText(_translate("Form", "PORT2_485"))
        self.label_3.setText(_translate("Form", "PORT1_485"))
        self.pushButton_2.setWhatsThis(_translate("Form", "Send data continuously until communication brakes"))
        self.pushButton_2.setText(_translate("Form", "CONNECT"))
        self.pushButton_2.setStyleSheet('QPushButton {font: 7pt "MS Shell Dlg 2";}')
        self.pushButton.setText(_translate("Form", "TEST PORTS"))
        self.pushButton.setStyleSheet('QPushButton {font: 7pt "MS Shell Dlg 2";}')
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:11pt;\">RS485</span></p></body></html>"))
        self.label_6.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:11pt;\">RS232</span></p></body></html>"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:11pt;\">USB</span></p></body></html>"))
        self.pushButton_5.setText(_translate("Form", "TEST PORT"))
        self.pushButton_5.setStyleSheet('QPushButton {font: 7pt "MS Shell Dlg 2";}')
        self.label_8.setText(_translate("Form", "Select USB Drive"))
        self.list_coms()

    

    def list_coms(self):
        self.usb_ports=self.usb.usb_ports_refresh()
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
        if isinstance(self.usb_ports,dict):
            for port in self.usb_ports:
                self.comboBox_4.addItem(port["tug"])
        QApplication.processEvents()
        for port in self.usb_ports:
                self.comboBox_4.addItem(port)
        QApplication.processEvents()

    def change_usb_path(self):
        #self.usb_path=self.comboBox_4.currentText()
        pass
    
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
