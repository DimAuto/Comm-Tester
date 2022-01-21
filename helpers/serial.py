import serial
import time
import serial.tools.list_ports
from PyQt5 import QtCore


class Test(QtCore.QObject):

    statusChange=QtCore.pyqtSignal(str)
    
    def __init__(self,port1_485=None,port2_485=None,port_232=None,parent=None):
        super(Test,self).__init__(parent)
        self.portList=[]
        self.Port1_485=port1_485
        self.Port2_485=port2_485
        self.Port_232=port_232
        self.status=None

    def listPorts(self):
        self.portList=[]
        plist=[]
        plist= serial.tools.list_ports.comports()
        for port in plist:
            print (port)
            self.portList.append(port.name)
        return(self.portList)


    def RS485_Test(self,Speed=57600):
        try:
            ser1 = serial.Serial(self.Port1_485, Speed, timeout=0, parity=serial.PARITY_EVEN, rtscts=False)
            ser2 = serial.Serial(self.Port2_485, Speed, timeout=0, parity=serial.PARITY_EVEN, rtscts=1)
        except Exception as e:
            self.status=str(e)
            #return(self.status)

        ser1.setRTS(True)
        ser1.setDTR(False)

        test_string=b"qwerty123456"

        resp=b""
        if ser1.is_open and ser2.is_open:
            try:
                ser1.write(test_string)
            except Exception as e:
                print(str(e))
            time.sleep(.1)    
            resp=ser2.read(12)   
            if  resp==test_string:
                self.status="RS485 PORT OK"
            else:
                self.status="RS485 PORT FAILED"
        else:
            self.status="RS485 PORT FAILED"

        ser1.close
        ser2.close

        return(self.status)

    def commRunning(self):
        self.status="Communication Running"
        self.statusChange.emit(self.status)


    def RS485_Continuous(self,Speed=57600):
        c=0
        try:
            ser1 = serial.Serial(self.Port1_485, Speed, timeout=0, parity=serial.PARITY_EVEN, rtscts=False)
            ser2 = serial.Serial(self.Port2_485, Speed, timeout=0, parity=serial.PARITY_EVEN, rtscts=1)
        except Exception as e:
            self.status=str(e)
            return(self.status)

        ser1.setRTS(True)
        ser1.setDTR(False)

        test_string=b"qwerty123456"
        resp=b""
        self.commRunning()
        time.sleep(0.5)
        while(c<200):
            if ser1.is_open and ser2.is_open:
                try:
                    ser1.write(test_string)
                    time.sleep(.1)
                    resp=ser2.read(12)
                except Exception as e:
                    print("Serial Error"+ str(e))
                    break
                if resp!=test_string:
                    break
            else:
                self.status="serial problem"
                break
            c+=1
        self.status="Communication Stopped"
        ser1.close
        ser2.close
        return(self.status)


    def RS232_Test(self,Speed=9600):
        try:
            ser=serial.Serial(self.Port_232, Speed, timeout=0,bytesize=8, parity=serial.PARITY_NONE, xonxoff=1)
        except Exception as e:
            self.status=str(e)
            ser=None
            return(self.status)
        if ser==None:
            return(0)
        resp=b""
        test_string=b'qwerty123456'
        if ser.is_open:
            try:
                ser.write(test_string)
            except Exception as e:
                print("Serial Error"+ str(e))
            time.sleep(.1)

            if ser.inWaiting()>0:
                resp=ser.read(12)
                
            if  resp==test_string:
                self.status="RS232 PORT OK"
            else:
                self.status="RS232 PORT FAILED"
        else:
            self.status="RS232 PORT FAILED"
        ser.close
        return(self.status)



    def RS232_Continuous(self,Speed=9600):
        c=0
        try:
            ser = serial.Serial(self.Port_232, Speed, timeout=0, parity=serial.PARITY_EVEN, xonxoff=1)
        except Exception as e:
            self.status=str(e)
            #return(self.status)
        test_string=b"qwerty123456"
        resp=b""
        self.commRunning()
        while(c<200):
            if ser.is_open:
                try:
                    ser.write(test_string)
                    time.sleep(.1)
                    resp=ser.read(12)
                except Exception as e:
                    print("Serial Error"+ str(e))
                    break
        
                if resp!=test_string:
                    break
            else:
                self.status="Serial problem"
                break
            c+=1
        self.status="Communication Stopped"
        ser.close
        return(self.status)

if __name__=="__main__":
    t=Test("COM10","COM7")
    print (t.listPorts())
    print(t.RS485_Test())
