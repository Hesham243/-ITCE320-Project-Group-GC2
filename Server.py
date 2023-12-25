import socket
import threading
#import requests
#import json


def start_connection(sock_a):
    name = sock_a.recv(1024).decode('ascii')
    names.append(name)
    print("The Client <",name,"> connect to the Server successfull!")
    
    while True:
        try:
            Option = sock_a.recv(1024).decode('ascii')
            

            if Option == '1':
                msg ="one"
                sock_a.sendall(msg.encode('ascii'))
                print(name, ' >>>> Selected Option', Option)


            elif Option == '2':
                msg ="two"
                sock_a.sendall(msg.encode('ascii'))
                print(name, ' >>>> Selected Option', Option)


            elif Option == '3':
                msg ="three"
                sock_a.sendall(msg.encode('ascii'))
                print(name, ' >>>> Selected Option', Option)
            

            elif Option == '4':
                msg ="four"
                sock_a.sendall(msg.encode('ascii'))
                print(name, ' >>>> Selected Option', Option)


            elif Option == '5':
                msg ="You quit. Thanks for your participating."
                sock_a.sendall(msg.encode('ascii'))
                print(name, ' >>>> Selected Option', Option)
                break
                
        except:
            print("The Client '", name, "' Disconnected from the Server ! ")
            name.remove
            break
    


ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind (('127.0.0.1',49999))
ss.listen(3)
print ('<<<<<<<<<  server is online  >>>>>>>>')


threads=[]
names=[]
while True:
    sock_a, sockName = ss.accept()
    t = threading.Thread( target=start_connection, args=(sock_a,) )
    threads.append(t)
    t.start()
    # if len(threads)>5:
    #     break


ss.close()