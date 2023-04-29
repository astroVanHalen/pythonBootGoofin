##################################################
###	Title   - Lab 12
###	Author – Zac Huron
###	Date – 2023 04 16
###	Description – Build GUI for connecting to Network
### Devices
##################################################  

from netmiko import ConnectHandler as connect
import ipaddress

# Define the device parameters for netmiko
device = {
    'device_type' : 'cisco_ios'
    ,'ip' : '10.10.20.172'
    ,'username' : 'cisco'
    ,'password' : 'cisco'
}

def configure_device():
    '''
    This function asks for user input to specify the device to be configured
    '''
    while True:
        device = input("Which device do you want to configure? (Edge-sw01, Dist-sw01, Dist-sw02) ")
        if device in ['Edge-sw01', 'Dist-sw01', 'Dist-sw02']:
            # your code to configure the device goes here
            break
        else:
            print("Invalid device selection. Please select one of the following devices: Edge-sw01, Dist-sw01, Dist-sw02")


def set_vlan_ip():
    '''
    This function creates and sets an ip address for a vlan interface on the selected device. It also checks
    whether the subnet for the vlan contains the IP address for the SSH connection (hardcoded into this function)
    An error is returned if the vlan subnet contains the SSH IP.
    User input:
        IP Network address for vlan

    Hardcoded currently:
        vlan number
        SSH IP address

    '''
    while True:
        vlan_ip = input("Enter the IP address in x.x.x.x/yy format: ")
        ssh_address = ipaddress.IPv4Address('10.10.20.172')
        # After way to long of testing and research, I decided to store commands in a list, and use the list variable to pass
        # into the send_config_set method
        config_commands = [
            "interface vlan 42",
            "!",
            f"ip address {ip_address} {ip_network.prefixlen}",
            "!",
            "no shutdown"
        ]
        try:
            ip_network = ipaddress.IPv4Network(vlan_ip)
            ip_address = ip_network.network_address + 1
        except ValueError:
            print("Invalid IP address format. Please try again.")
            continue
        if ssh_address in ip_network:
            print("The IP address should not be in the same subnet as SSH access for the device. Please try again.")
            continue
        # This is the code to set the VLAN.  For proof of concept, 42 is hardcoded
        output = net_connect.send_config_set(config_commands)
        break


# Establish SSH connection to the device
# NOTE switch must also be configured for SSH connection

with connect(**device) as net_connect:
    # Send command to retrieve the running-config
    output = net_connect.send_command('show running-config')
    print(output)



   # Set up for CLI menu     
   # \n keeps it neat by starting with a CR|LF     
    while True:
        print("\nSelect an option:")
        print("1. Configure a device")
        print("2. Set an IP address on a VLAN")
        print("3. Do nothing")
        print("4. Do nothing")
    
        choice = input("Enter your choice: ")
    
        if choice == '1':
            configure_device()
        elif choice == '2':
            set_vlan_ip()
        elif choice == '3' or choice == '4':
            pass
        else:
            print("Invalid choice")




