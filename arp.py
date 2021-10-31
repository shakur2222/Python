from netmiko import ConnectHandler  
import getpass                         
import sys    
import re

##### device connection section #####


ip = input("IP\Hostname of switch: ")

device= {                             
        'device_type': 'cisco_ios',
        'ip': ip,
        
        }
        


print ("Please enter your credentials") 

device['username']=input("Username: ")  
device['password']=getpass.getpass()    


conn = ConnectHandler(**device)

##### end of device connection section #####



##### grabbing IP of device from user input #####
##### d_ip = input("Enter IP of Device: ")


##### Taking the user input, making the command and sending the command to the switch #####
##### arp = conn.send_command('show ip arp {d_ip}'.format(d_ip=d_ip))



##### taking the output and splitting it into a list #####
##### l_arp = arp.split()


##### setting a variable to call on the length of the above list #####
##### a = len(l_arp)





    

##### making an if statement saying if the length of the list we made is not empty pull the 12th item
##### of the list (lists start at 0 for item 1)  and saves it to a variable. Then we make a new list 
##### and a for loop to say, take the items in the list "mac" and put it in the new list "com" with 
##### the show command. Then we make another for loop and tell it for every item in the list "com"
##### send that as a command to the switch. #####

##### we then make more for loops to take the info from the show mac add command, strip out the port
##### and then make a show run int command with that so we can see the port info. The else statement 
##### prints off the "No IP Found" if the original is empty so we dont pull any errors for trying to
##### print an item from an empty list #####

def script():
    d_ip = input("Enter IP of Device: ")
    arp = conn.send_command('show ip arp {d_ip}'.format(d_ip=d_ip))
    l_arp = arp.split()
    a = len(l_arp)
    if a > 0:
        mac =[l_arp[11]]
        com = []
        pic = []
        for item in mac:
            com.append(' show mac add | i {item}'.format(item=item))
            for item in com:
                print(conn.send_command(item))
                port = conn.send_command(item)
                l_port = port.split()
                pi=[l_port[3]]
                for item in pi:
                    pic.append('show run int {item}'.format(item=item))
                    for item in pic:
                        print(conn.send_command(item))
    
    else:
        print('No IP Found')
    
##### making a function that will repeat since True is always True. place the Scripting function at the top 
##### so it will repeat. it will then ask if you have another IP. if "n" the function is broken out of.
##### If "y" then it will repeat the script. also had a section if user enters something besides y or n #####


def main():
    while True:
        script()
        again = input("Another IP? Enter y/n: ")

        if again == "n":
            print ("All done!")
            return
        elif again == "y":
            print ("From The Top!")
            
        else:
            print ("You should enter either \"y\" or \"n\".")


##### Calling the repeating function #####
main()

##### closing the connection to the switch #####
conn.disconnect()



    
       



    

