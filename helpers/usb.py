import re
from sys import path
import time
from PyQt5 import QtCore
import sys
import subprocess

if sys.platform == "win32":
    import wmi

class USB(QtCore.QObject):

    def __init__(self,parent=None):
        super(USB,self).__init__(parent)
        self.status=None
        self.path=None
        self.usb_ports_refresh()

    def usb_ports_refresh(self):
        if sys.platform == "win32":
            ports = self.usb_ports_refresh_win()
        else:
             ports = self.usb_ports_refresh_linux()
        return ports

    def usb_ports_refresh_linux(self):
        device_re = re.compile(b"Bus\s+(?P<bus>\d+)\s+Device\s+(?P<device>\d+).+ID\s(?P<id>\w+:\w+)\s(?P<tag>.+)$", re.I)
        df = subprocess.check_output("lsusb")
        devices = []
        for i in df.split(b'\n'):
            if i:
                info = device_re.match(i)
                if info:
                    dinfo = info.groupdict()
                    dinfo['device'] = '/dev/bus/usb/%s/%s' % (dinfo.pop('bus'), dinfo.pop('device'))
                    devices.append(dinfo)
        return devices

    def usb_ports_refresh_win(self):
        c = wmi.WMI()
        flash_drive_list = []
        self.path=None
        for disk in c.Win32_LogicalDisk():
            if disk.Description== "Removable Disk":
                flash_drive_list.append(disk.Name)
        return flash_drive_list

    def built_str(self,n):
        init_str="\x14\x22\x16\x14"
        data=""
        for i in range(0,n):
            data+=init_str
        return(data)
    
    def change_path(self):
        self.path=None

    def Wspeed_test(self,path,data):
        d=data
        try:
            with open(path,"w") as file:
                file.write("")
                start = time.time()
                #for i in range(0,n):
                file.write(d)
                stop=time.time()
                file.close()
            self.status=("OK  Speed: "+str((round(12/(stop-start),3)))+" Mb/s")
        except Exception as e:
            if str(e)[1:8]=="Errno 2":
                self.status=("Drive Not Found")
            else:
                self.status=("Please add a USB Path")

# if __name__ == "__main__":
#     usb=USB()
#     print(usb.usb_ports_refresh_win())