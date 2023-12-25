import socket


CS = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
CS.connect(("127.0.0.1", 49999))
CName = input("Enter client's username here: ")
CS.sendall(CName.encode('utf-8'))


while True:

    try:
        print("1- Display All arrived flights")
        print("2- Display All delayed flights")
        print("3- Display All flights from a specific city")
        print("4- Display Details of a particular flight")
        print("5- Quit ")
        option = input("\nEnter a option number [1-5]: \n")
        print()

         
        if   option == 1:
            CS.sendall(option.encode('utf-8'))
            
            data = CS.recv(8192) 
            print(data.decode('utf-8'))

        elif option == 2:
            CS.sendall(option.encode('utf-8'))
            data = CS.recv(16384) 
            print(data.decode('utf-8'))

        elif option == 3:
            CS.sendall(option.encode('utf-8'))
            city_iata = input("Enter the city (IATA) here: ")
            CS.sendall(city_iata.encode('utf-8'))          
            data = CS.recv(8192) 
            print(data.decode('utf-8'))

        elif option == 4:
            CS.sendall(option.encode('utf-8'))
            flight_iata = input("Enter the flight (IATA) here: ")
            CS.sendall(flight_iata.encode('utf-8'))
            data = CS.recv(8192) 
            print(data.decode('utf-8'))
        
        elif option == 5:
            CS.sendall(option.encode)
            print("You quit. Thanks for your participating.")
            CS.close()
            break

        else:
            print("\n Invalid option, Please enter a number from 1 to 5 only: ")
            print()
        
    except:
        print("Unexpected error. Please try again.")
        break
