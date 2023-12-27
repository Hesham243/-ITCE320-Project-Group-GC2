import socket
import threading
import requests
import json


def api_response(ICAO):
    params = {
                'access_key': '0e5eb992a53abb61b4ec5423713fc090',
                'arr_icao': ICAO,
                'limit': 100
            }
    
    print("Getting the data from the API. PLease wait... \n")
    api_result = requests.get('http://api.aviationstack.com/v1/flights', params)

    with open("Group2.json", "w") as file:
        json.dump(api_result.json(), file, indent=4)
    
    print("Data has been stored in the file [ Group 2.json ]\n")
    api_data = json.load(open('Group2.json'))
    return api_data

def start_connection(socketActive, api_data):
    clientName = socketActive.recv(1024).decode('utf-8')
    names.append(clientName)
    print("The Client [",clientName,"] connect to the Server successfully!!\n")
    
    while True:
        try:
            Option = socketActive.recv(1024).decode('utf-8')
            Data_Api= json.load(open('Group2.json'))

            if Option == 1:
                ####### start All_Arrived_Flights
                for Arrived in Data_Api['data']:
                    if Arrived ['flight_status'] == 'landed':
                        Data_user +=str([' Dlight IATA: ',Arrived['flight']["iata"],', Departure Airport: ',Arrived['departure']['airport'],
                        ', Arrival Time: ',Arrived['arrival']['estimated'],', Arrival Terminal Number: ',Arrived['flight']['number'],
                        ', Terminal: ',Arrived['arrival']['terminal'],', Gate: ',Arrived['arrival']['gate']
                        ])
                socketActive.sendall(Data_user.encode('utf-8'))
                print(clientName, ' >>>> Selected Option is [',Option,']')


            elif Option == 2:
                ####### start All_Delayed_Flights
                for Arrived in Data_Api['data']:
                    if Arrived ['flight_status'] == 'scheduled':
                        Data_user +=str(['flight IATA: ',Arrived['flight']["iata"],', Departure Airport: ',Arrived['departure']['airport'],
                        ', Original Departure Time: ',Arrived['departure']['timezone'],', Estimated Time of Arrival: ',Arrived['arrival']['estimated'],
                        ', Arrival Terminal: ',Arrived['arrival']['terminal'],', Delay: ',Arrived['arrival']['delay'],
                        ', Arrival Gate: ',Arrived['arrival']['gate']
                        ])
                socketActive.sendall(Data_user.encode('utf-8'))
                print(clientName, ' >>>> Selected Option is [',Option,']')


            elif Option == 3:
                Data_user ="three"
                socketActive.sendall(Data_user.encode('utf-8'))
                print(clientName, ' >>>> Selected Option is [',Option,']')
            

            elif Option == 4:
                Data_user ="four"
                socketActive.sendall(Data_user.encode('utf-8'))
                print(clientName, ' >>>> Selected Option is [',Option,']')


            elif Option == 5:
                Data_user ="You quit. Thanks for your participating."
                clientName.sendall(Data_user.encode('utf-8'))
                print(clientName, ' >>>> Selected Option is [',Option,']\n')
                print("The Client [",clientName,"] Disconnected from the Server ! \n")
                break
                
        except:
            print("The Client [",clientName,"] Disconnected from the Server ! \n")
            clientName.remove
            socketActive.close()
            break


serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind (('127.0.0.1', 49999))
serverSocket.listen(3)
print ('<<<<<<<<<  ----[Server is Online]----  >>>>>>>>\n')


threads=[]
names=[]

def valid_input(input_str):
    if len(input_str) >= 3:
        return True
    else:
        return False
   
while True:
    ICAO = input("Enter the airport code (ICAO): \n")
    if valid_input(ICAO): # check the validity of the airport code
        break

print("Chosen airport code (icao) is [",ICAO,"]\n")

api_data = api_response(ICAO)

while True:
    socketActive, socketName = serverSocket.accept()
    st = threading.Thread( target=start_connection, args=(socketActive, api_data) )
    threads.append(st)
    st.start()
    # if len(threads)>5:
    #     break


socketActive.close()