from ast import Num
from optparse import Option
from os import remove
import socket
import threading
#import requests
#import json

thread=[]
name=[]

def Online():
    name = ss.recv(1024).decode('utf-8')
    name.append(name)
    print(name,' is Online')
    
    while True:
        try:
            Option = ss.recv(1024).decode('utf-8')
            if Option == 1:
                SS.sendall('one')
            elif Option == 2:
                SS.sendall('two')
            elif Option == 3:
                SS.sendall('three')
            elif Option == 4:
                SS.sendall('four')
            elif Option == 5:
                SS.sendall('five')
                
        except:
            print(name,' is Offline')
            name.remove
            break
    


SS = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SS.bind (('127.0.0.1',49999))
SS.listen(3)
print ('<<<<<<<<<  server is online  >>>>>>>>')


while True:
    ScAdd, ScName = SS.accept()
    ST = threading.Thread( target=Online, args=(ScAdd,len(thread)+1) )
    thread.append(ST)
    ST.start()
    if len(thread)>10:
        break


ss.close()