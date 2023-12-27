import socket


clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(('127.0.0.1', 49999))
clientName = input("Enter client's username here: ")
clientSocket.sendall(clientName.encode('utf-8'))


def recv_all(clientSocket):
    data_user = b''
    while True:
        data = clientSocket.recv(4096)
        data_user += data
        print(data.decode('utf-8'))
        if data.endswith(b'\x00'):
            break
    return data_user


while True:

    try:
        print("1- Display All arrived flights")
        print("2- Display All delayed flights")
        print("3- Display All flights from a specific city")
        print("4- Display Details of a particular flight")
        print("5- Quit ")
        option = input("\nEnter a option number [1-5]: \n")
        print()

        clientSocket.sendall(option.encode('utf-8'))
        if   option == '1':
            data = recv_all(clientSocket)
            print(data.decode('utf-8'))

        elif option == '2':
            data = recv_all(clientSocket) 
            print(data.decode('utf-8'))

        elif option == '3':
            city_iata = input("Enter the city (IATA) here: ")
            clientSocket.sendall(city_iata.encode('utf-8'))          
            data = recv_all(clientSocket) 
            print(data.decode('utf-8'))

        elif option == '4':
            flight_iata = input("Enter the flight (IATA) here: ")
            clientSocket.sendall(flight_iata.encode('utf-8'))
            data = recv_all(clientSocket) 
            print(data.decode('utf-8'))
        
        elif option == '5':
            data = clientSocket.recv(8192)
            print(data.decode('utf-8'))
            print()
            clientSocket.close()
            break

        else:
            print("\n Invalid option, Please enter a number from 1 to 5 only: ")
            print()
        
    except:
        print("Unexpected error. Please try again.")
        break
