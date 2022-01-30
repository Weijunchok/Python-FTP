# -*- coding: utf-8 -*-
from ftplib import FTP
import os
basepath = os.path.dirname(__file__)
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__)))
#If you want to download the file to the upper folder where the Py script is located, use os.pardir
#datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
ftpfolder = datapath + "/ftpfile"
#Connecting to FTP Server,default ftp mode is positive  
def ftpconnect(host,port, username, password):
    ftp = FTP()
    ftp.set_debuglevel(2)
    ftp.set_pasv(False)            #Passive or Positive Mode
    ftp.connect(host, port)
    ftp.login(username, password)
    return ftp
#Download file from FTP remotepath to localpath 
def downloadfile(ftp, remotepath, localpath):
    bufsize = 1024
    fp = open(localpath, 'wb')
    ftp.retrbinary("RETR " + remotepath, fp.write, bufsize)
    fp.close()
#ftpconnect: FTP Server Host,Port,Username,Password
ftp = ftpconnect("host", 21,"user", "password")
#FTP Current Path
pwd_path = ftp.pwd()
print("FTP Current Path:", pwd_path)
pwd_fold = pwd_path
ftp.cwd(pwd_fold)
remotepath = pwd_fold + "/test.txt"     
localpath = ftpfolder + "/test.txt"
downloadfile(ftp, remotepath,localpath)
#Disconnect FTP Server
ftp.quit()
