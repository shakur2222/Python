from netmiko import ConnectHandler  
import getpass                         
import sys    

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




##### setting up a user input variable to decide what if statement to run  #####

int_type = input(" Gi access ports? y/n: ")




##### new variable to send the show command #####

o1 = conn.send_command("show int status | inc notconnect|dis")




##### making a new variable that splits the show output int a list. fi and fo are list filters, it takes
##### the input, either Gi or Fa, and searches the list provided and filters them out leaving only items
##### that contain that value ##### 

interfaces = o1.split()
fi = (list(filter(lambda a: "Gi" in a, interfaces)))
fo = (list(filter(lambda a: "Fa" in a, interfaces)))
#print(fi, sep = '\n')

##### making a new list to use in an if statement, the if statement takes what was inputed by the user
##### above, if y then it runs the Gi version of show int and appends them to the list. if n it uses 
##### the Fa version instead #####

port = []
if int_type == 'y':
    for interfaces in fi:
        port.append('show int {interfaces} | inc Last input|Gi|Desc'.format(interfaces=interfaces))
        
else:
     for interfaces in fo:
         port.append('show int {interfaces} | inc Last input|Fa|Desc'.format(interfaces=interfaces))
         

#print(*port, sep = '\n')

##### for statement in which it takes every item in the list port that we created above, runs through 
##### and sends that command to the switch until the end of the list while putting two line breaks in
##### for readability #####

for line in port:
    print(conn.send_command(line),'\n','\n')



##### Disconnects from the switch #####

conn.disconnect() 