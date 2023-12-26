import json
print('start')
Data_Api= json.load(open('Group2.json'))

for Arrived in Data_Api['data']:
    if Arrived ['flight_status'] == 'landed':
        print('landed is working!')
        Data_user =str(['landed >> IATA: ',Arrived['flight']["iata"],', Airport: ',Arrived['departure']['airport'],
        ', Estimated: ',Arrived['arrival']['estimated'],', Number: ',Arrived['flight']['number'],
        ', Terminal: ',Arrived['arrival']['terminal'],', Gate: ',Arrived['arrival']['gate']
        ])
        print(Data_user)
    elif Arrived ['flight_status'] == 'scheduled':
        Data_user =str(['scheduled >> IATA: ',Arrived['flight']["iata"],', Airport: ',Arrived['departure']['airport'],
        ', Estimated: ',Arrived['arrival']['estimated'],', Number: ',Arrived['flight']['number'],
        ', Terminal: ',Arrived['arrival']['terminal'],', Gate: ',Arrived['arrival']['gate']
        ])
        
        print(Data_user)
