import socket


clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(('127.0.0.1', 49999))
clientName = input("Enter client's username here: ")
clientSocket.sendall(clientName.encode('ascii'))


while True:

    try:
        print("1- Display All arrived flights")
        print("2- Display All delayed flights")
        print("3- Display All flights from a specific city")
        print("4- Display Details of a particular flight")
        print("5- Quit ")
        option = input("\nEnter a option number [1-5]: \n")
        print()

         
        if   option == '1':
            clientSocket.sendall(option.encode('ascii'))
            data = clientSocket.recv(8192) 
            print(data.decode('ascii'))

        elif option == '2':
            clientSocket.sendall(option.encode('ascii'))
            data = clientSocket.recv(16384) 
            print(data.decode('ascii'))

        elif option == '3':
            clientSocket.sendall(option.encode('ascii'))
            city_iata = input("Enter the city (IATA) here: ")
            clientSocket.sendall(city_iata.encode('ascii'))          
            data = clientSocket.recv(8192) 
            print(data.decode('ascii'))

        elif option == '4':
            clientSocket.sendall(option.encode('ascii'))
            flight_iata = input("Enter the flight (IATA) here: ")
            clientSocket.sendall(flight_iata.encode('ascii'))
            data = clientSocket.recv(8192) 
            print(data.decode('ascii'))
        
        elif option == '5':
            clientSocket.sendall(option.encode('ascii'))
            data = clientSocket.recv(8192)
            print(data.decode('ascii'))
            print()
            clientSocket.close()
            break

        else:
            print("\n Invalid option, Please enter a number from 1 to 5 only: ")
            print()
        
    except:
        print("Unexpected error. Please try again.")
        break
