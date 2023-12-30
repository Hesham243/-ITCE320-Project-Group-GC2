import socket
from tabulate import tabulate

class Client:
    def __init__(self, host, port):
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port


    def connect_to_server(self):
        try:
            self.clientSocket.connect((self.host, self.port))
        except Exception as e:
            print(f"\n>>>>> Error connecting to the server: {e}\n")
            exit()


    def send_username(self):
        client_name = input("\nEnter client's username here: ")
        self.clientSocket.sendall(client_name.encode('utf-8'))


    def recv_all(self):
        data = b''
        while True:
            try:
                part = self.clientSocket.recv(4096)
                if not part:
                    raise Exception("\n>>>>> Connection closed by the server.")
                data += part
                if len(part) < 4096:
                    break
            except Exception as e:
                print(f"\n>>>>> Error receiving data: {e}")
                break
        return data
    

    def menu(self):
        while True:
            try:
                print("1- Display All arrived flights")
                print("2- Display All delayed flights")
                print("3- Display All flights from a specific city")
                print("4- Display Details of a particular flight")
                print("5- Quit ")
                option = input("\nEnter a Option Number [1-5]: \n")
                print()
                self.clientSocket.sendall(option.encode('utf-8'))

                if option == '1':
                    data = self.recv_all()
                    try:
                        print(data.decode('utf-8'))
                    except Exception as e:
                        print(f"\n>>>>> Error displaying table: {e}\n")
                

                elif option == '2':
                    data = self.recv_all()
                    try:
                        print(data.decode('utf-8'))
                    except Exception as e:
                        print(f"\n>>>>> Error displaying table: {e}\n")


                elif option == '3':
                    while True:
                        user_input = input("\nEnter the city (iata) here: ").upper()
                        print()
                        if len(user_input) >= 3:  # check the validity of the input
                            break
                        else:
                            print("\n>>>>> Invalid city iata entered. Please enter a valid code.")
                    self.clientSocket.sendall(user_input.encode('utf-8'))
                    data = self.recv_all()
                    decoded_data = data.decode('utf-8')

                    try:
                        if not decoded_data.strip():
                            print("\n>>>> No data found. Please try again.\n")
                        else:
                            print(decoded_data)
                    except Exception as e:
                        print(f"\n>>>>> Error displaying table: {e}\n")
                

                elif option == '4':
                    while True:
                        user_input = input("\nEnter the flight (iata) here: ").upper()
                        print()
                        if len(user_input) >= 3:  # check the validity of the input
                            break
                        else:
                            print("\n>>>>> Invalid flight iata entered. Please enter a valid code.")
                    
                    self.clientSocket.sendall(user_input.encode('utf-8'))
                    data = self.recv_all()
                    decoded_data = data.decode('utf-8')

                    try:
                        if not decoded_data.strip():
                            print("\n>>>>> No data found. Please try again.\n")
                        else:
                            print(decoded_data)
                    except Exception as e:
                        print(f"\n>>>>> Error displaying table: {e}\n")
                

                elif option == '5':
                    data = self.clientSocket.recv(8192)
                    print(data.decode('utf-8'))
                    print()
                    self.clientSocket.close()
                    break

                else:
                    print("\n>>>>> Invalid option entered, Please enter a option from 1 to 5 only: ")
                    print()

            except Exception as e:
                print(f"\n>>>>> Unexpected error: {e}\n")
                break


if __name__ == "__main__":
    client = Client('127.0.0.1', 49999)
    client.connect_to_server()
    client.send_username()
    client.menu()
