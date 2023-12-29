import socket
import threading
import requests
import json
from tabulate import tabulate


class Server:
    def __init__(self, host, port):
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverSocket.bind((host, port))
        self.serverSocket.listen(3)
        print('\n<<<<<<<<<  ----[Server is Online]----  >>>>>>>>>>')
        self.threads = []
        self.names = []


    def api_response(self, ICAO):
        params = {
            'access_key': '0e5eb992a53abb61b4ec5423713fc090',
            'arr_icao': ICAO,
            'limit': 100
        }


        print("\nGetting the data from the API. Please wait...")
        api_result = requests.get('http://api.aviationstack.com/v1/flights', params)

        with open("Group_2.json", "w") as file:
            json.dump(api_result.json(), file, indent=4)

        print("\nData has been stored in file called [ Group_2.json ]")
        api_data = json.load(open('Group_2.json'))
        return api_data
    

    def display_table(self, socket_active, headers, data):
        table = tabulate(data, headers=headers, tablefmt='grid')
        socket_active.sendall(table.encode('utf-8'))


    def start_connection(self, socket_active, api_data):
        client_name = socket_active.recv(1024).decode('utf-8')
        self.names.append(client_name)
        print("\nThe Client [", client_name, "] Connected To The Server Successfully.\n")

        while True:
            try:
                option = socket_active.recv(1024).decode('utf-8')
                data_api = json.load(open('Group_2.json'))

                if option == '1':
                    data_user = []
                    for arrived in data_api['data']:
                        if arrived['flight_status'] == 'landed':
                            data_user.append([arrived["flight"]["iata"],
                                             arrived["departure"]["airport"],
                                             arrived["arrival"]["estimated"],
                                             arrived["flight"]["number"],
                                             arrived["arrival"]["terminal"],
                                             arrived["arrival"]["gate"]])
                    
                    headers = ['Flight IATA', 'Departure Airport', 'Arrival Time', 'Arrival Terminal Number', 'Terminal', 'Gate']
                    self.display_table(socket_active, headers, data_user)
                    print('Client [' ,client_name, '] ==> Selected Option [', option, ']')
                

                elif option == '2':
                    data_user = []
                    for arrived in data_api['data']:
                        if arrived['flight_status'] == 'scheduled':
                            data_user.append([arrived["flight"]["iata"],
                                              arrived["departure"]["airport"],
                                              arrived["departure"]["timezone"],
                                              arrived["arrival"]["estimated"],
                                              arrived["arrival"]["terminal"],
                                              arrived["arrival"]["delay"],
                                              arrived["arrival"]["gate"]])
                    
                    headers = ['Flight IATA', 'Departure Airport', 'Original Departure Time', 'Estimated Arrival Time', 'Arrival Terminal', 'Delay', 'Arrival Gate']
                    self.display_table(socket_active, headers, data_user)
                    print('Client [' ,client_name, '] ==> Selected Option [', option, ']')


                elif option == '3':
                    data_user = []
                    iata = socket_active.recv(8192).decode('utf-8').upper()
                    if len(iata) < 3:
                        print(f"\nInvalid IATA code received from [ {client_name} ]. Disconnecting.\n")
                        socket_active.close()
                        break

                    for flight in data_api['data']:
                        if flight['departure']['iata'] == iata:
                            data_user.append([flight["flight"]["iata"],
                                             flight["departure"]["airport"],
                                             flight["departure"]["timezone"],
                                             flight["arrival"]["estimated"],
                                             flight["departure"]["gate"],
                                             flight["arrival"]["gate"],
                                             flight["flight_status"]])
                    
                    headers = ['Flight IATA Code', 'Departure Airport', 'Original Departure Time', 'Estimated Arrival Time', 'Departure Gate', 'Arrival Gate', 'Status']
                    self.display_table(socket_active, headers, data_user)
                    print('Client [' ,client_name, '] ==> Selected Option [', option, ']')
                

                elif option == '4':
                    data_user = []
                    flight_iata = socket_active.recv(8192).decode('utf-8').upper()
                    if len(flight_iata) < 3:
                        print(f"\nInvalid IATA code received from [ {client_name} ]. Disconnecting.\n")
                        socket_active.close()
                        break

                    for flight in data_api['data']:
                        if flight['flight']['iata'] == flight_iata:
                            data_user.append([flight["flight"]["iata"],
                                              flight["departure"]["airport"],
                                              flight["departure"]["gate"],
                                              flight["departure"]["terminal"],
                                              flight["arrival"]["airport"], 
                                              flight["arrival"]["gate"], 
                                              flight["arrival"]["terminal"],
                                              flight["flight_status"],
                                              flight["departure"]["scheduled"],
                                              flight["arrival"]["scheduled"]])
                    
                    headers = [ 'Flight IATA Code', 'Departure Airport', 'Departure Gate', 'Departure Terminal', 'Arrival Airport', 'Arrival Gate', 'Arrival Terminal', 'Status', 'Scheduled Departure Time', 'Scheduled Arrival Time']
                    self.display_table(socket_active, headers, data_user)
                    print('Client [' ,client_name, '] ==> Selected Option [', option, ']')


                elif option == '5':
                    data_user = "\nYou quit. Thanks For Your Participating."
                    socket_active.sendall(data_user.encode('utf-8'))
                    print('Client [' ,client_name, '] ==> Selected Option [', option, ']')
                    print("\nThe Client [" , client_name, "] Disconnected from the Server.\n")
                    break


            except Exception as e:
                print(f"\n>>>>> Error processing client request: {e}\n")
                print("\nThe Client [" ,client_name, "] Disconnected from the Server.\n")
                self.names.remove(client_name)
                socket_active.close()
                break


    def valid_input(self, input_str):
        return len(input_str) >= 3


    def run(self):
        while True:
            icao = input("\nEnter The Airport Code (ICAO): ")
            if self.valid_input(icao):  # check the validity of the airport code
                break

        print("\nChosen Airport Code (ICAO) is [" ,icao, "]")

        api_data = self.api_response(icao)

        while True:
            socket_active, socket_name = self.serverSocket.accept()
            st = threading.Thread(target=self.start_connection, args=(socket_active, api_data))
            self.threads.append(st)
            st.start()
            if len(self.threads) > 5:
                break

        socket_active.close()


if __name__ == "__main__":
    server = Server('127.0.0.1', 49999)
    server.run()
