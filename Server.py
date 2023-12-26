import socket
import threading
import requests
import json


def api_response(arr_icao):
    params = {
                'access_key': '0e5eb992a53abb61b4ec5423713fc090',
                'arr_icao': arr_icao,
                'limit': 100
            }
    
    print("Getting the data from the API. PLease wait... \n")
    api_result = requests.get('http://api.aviationstack.com/v1/flights', params)

    with open("Group2.json", "w") as file:
        json.dump(api_result.json(), file, indent=4)
    
    print("Data has been stored in the file [ Group 2.json ]\n")
    api_data = json.load(open('Group2.json'))
    return api_data



def start_connection(sock_a, api_data):
    name = sock_a.recv(1024).decode('ascii')
    names.append(name)
    print("The Client [",name,"] connect to the Server successfully!!\n")
    
    while True:
        try:
            Option = sock_a.recv(1024).decode('ascii')
            

            if Option == '1':
                msg ="one"
                sock_a.sendall(msg.encode('ascii'))
                print(name, ' >>>> Selected Option is [',Option,']')


            elif Option == '2':
                msg ="two"
                sock_a.sendall(msg.encode('ascii'))
                print(name, ' >>>> Selected Option is [',Option,']')


            elif Option == '3':
                msg ="three"
                sock_a.sendall(msg.encode('ascii'))
                print(name, ' >>>> Selected Option is [',Option,']')
            

            elif Option == '4':
                msg ="four"
                sock_a.sendall(msg.encode('ascii'))
                print(name, ' >>>> Selected Option is [',Option,']')


            elif Option == '5':
                msg ="You quit. Thanks for your participating."
                sock_a.sendall(msg.encode('ascii'))
                print(name, ' >>>> Selected Option is [',Option,']\n')
                break
                
        except:
            print("The Client [", name,"] Disconnected from the Server ! \n")
            name.remove
            break
    


ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind (('127.0.0.1',49999))
ss.listen(3)
print ('<<<<<<<<<  ----[Server is Online]----  >>>>>>>>\n')




threads=[]
names=[]

def valid_input(input_str):
    if len(input_str) >= 3:
        return True
    else:
        return False
while True:
    arr_icao = input("Enter the airport code (ICAO): \n")
    if valid_input(arr_icao): # check the validity of the airport code
        break

print("Chosen airport code (icao) is [",arr_icao,"]\n")

api_data = api_response(arr_icao)


while True:
    sock_a, sockName = ss.accept()
    t = threading.Thread( target=start_connection, args=(sock_a, api_data) )
    threads.append(t)
    t.start()
    # if len(threads)>5:
    #     break


sock_a.close()