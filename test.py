##################################################
###	Title   - Ping in Python
###	Author – Zac Huron
###	Date – 2/21/22
###     Description
###         This script will ping a given address
###			and output to a file the results if failed
##################################################  

import os
import datetime
from time import sleep


'''
This block takes user inputs as variables 
'''

file_name = input("Enter a filename (without extension): ")
directory = input("Enter a directory to save the file in: ")
ping_count = int(input("Enter the number of pings to send: "))
ping_delay = float(input("Enter the delay between pings (in seconds): "))
hostaddr = input("Enter the IP address to ping: ")

'''
Change cwd to input from user
'''
os.chdir(directory)

'''
Check if file name exists and delete it
if it already does
'''

if os.path.exists(file_name):
    os.remove(file_name)
    
'''
the [with open] statement will open the file
named by the user.  Using this statement allows
the file to be open and not have to be explicity
closed with a file.close() 
'''
	
with open(file_name,"a") as file:
  for i in range(1,ping_count):
    current_time = datetime.datetime.now()
    file.write(f'Ping started at {current_time}' + '\n')
    print(current_time = datetime.datetime.now())
    ping_string = f"ping -n 4 " + hostaddr
    response = os.system(ping_string)
    if response==1:    #failed ping
        current_time = datetime.datetime.now()
        formatted_time= str(current_time.strftime("%m/%d/%Y %H:%M:%S"))
        out_string = str("Ping failed at " + formatted_time + "\n")
        file.write(out_string)
        print ("Failed ping")
    else:
        out_string = str(f'Successful ping \#{i}')
        file.write(out_string)
        print("Successful ping")
		
	
    sleep(ping_delay)
	
current_time = datetime.datetime.now()
file.write(f'Ping ended at {current_time}')
print('Ping Ended')