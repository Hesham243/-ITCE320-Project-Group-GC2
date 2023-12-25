import socket

# Client socket has been created.
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Client socket has been connected to the server.
clientSocket.connect(("127.0.0.1", 49999))

# Obtaining the client's username. 
client_username = input("Enter client's username here: ")
# Obtain the username entered, then encode it in a variable.
clientUsername_encode = client_username.encode('utf-8')
# Send the username to the server as mentioned in the project description.
clientSocket.sendall(clientUsername_encode)


while True:

    try:
        print("1- Display All arrived flights")
        print("2- Display All delayed flights")
        print("3- Display All flights from a specific city")
        print("4- Display Details of a particular flight")
        print("5- Quit ")
        option = input("\nEnter a option number [1-5]: \n")
        print()


        if option == "1":
            # Send the option which is chosen by the client to the server.
            clientSocket.sendall(option.encode)
            # Receive the data from the server. Then decode it. Then print it.
            data = clientSocket.recv(8192) 
            data_decoded = data.decode('utf-8')
            print(data_decoded)

        
        elif option == "2":
            # Send the option which is chosen by the client to the server.
            clientSocket.sendall(option.encode)
            # Receive the data from the server. Then decode it. Then print it.
            data = clientSocket.recv(16384) 
            data_decoded = data.decode('utf-8')
            print(data_decoded)

        
        elif option == "3":
            # Send the option which is chosen by the client to the server.
            clientSocket.sendall(option.encode)
            # Plus request the specific city IATA and send it to the server as mentioned in the project description.
            city_iata = input("Enter the city (IATA) here: ")
            clientSocket.sendall(city_iata.encode())          
            # Receive the data from the server. Then decode it. Then print it.
            data = clientSocket.recv(8192) 
            data_decoded = data.decode('utf-8')
            print(data_decoded)

        
        elif option == "4":
            # Send the option which is chosen by the client to the server.
            clientSocket.sendall(option.encode)
            # Plus request the particular flight IATA and send it to the server as mentioned in the project description.
            flight_iata = input("Enter the flight (IATA) here: ")
            clientSocket.sendall(flight_iata.encode())
            # Receive the data from the server. Then decode it. Then print it.
            data = clientSocket.recv(8192) 
            data_decoded = data.decode('utf-8')
            print(data_decoded)

        
        elif option == "0":
            # Send the option which is chosen by the client to the server.
            clientSocket.sendall(option.encode)
            # Print this message to client before closing.
            print("You quit. Thanks for your participating.")
            clientSocket.close()
            break


        else:
            # This message appear when user enter an wrong option number.
            print("\n Invalid option, Please enter a number from 1 to 5 only: ")
            print()
        
    except:
        print("Unexpected error. Please try again.")
        break
