import netmiko
from netmiko import ConnectHandler
import re
import json
import pandas 

# FROM LESSON 1

# establish an SSH session with a network device
e1=netmiko.ConnectHandler(ip='172.16.14.214',username='admin',password='password',device_type='arista_eos')
# run an SSH CLI command to collect a raw single string of data. We will call it rawstring.
rawstring=e1.send_command('show ip interface brief | begin 1500')
# convert the raw string into a list of strings with a Python string split method.
listofstr=rawstring.split('\n')
# convert the list of strings into a list of lists of strings using list comprehension
listoflistsofstr=[re.split(r' +', i) for i in listofstr]
# remove or pop off the last line of the list because it is completely blank
listoflistsofstr.pop(-1)
# print out the listoflistsofstr from Lab1 to be the visual starting point to begin Lab2

# FROM LESSON 2

listoflistsofstrjson=json.dumps(listoflistsofstr) #convert listoflistsofstr into json for PANDAS ingestion
pandasdf=pandas.read_json(listoflistsofstrjson) # ingest listoflistsofstrjson into PANDAS
pandasdf = pandasdf[[0,1,2,4]]  # remove unwanted columns from our PANDAS dataframe
column_headings=['Interface','IP Address','State','MTU']   # create column headings
pandasdf.columns=column_headings  # apply column headings to our dataframe
listofdictsjson=pandasdf.to_json(orient='records')   # convert PANDAS dataframe back into JSON
listofdicts=json.loads(listofdictsjson)  #convert JSON object into a Python list of dictionaries

print('\nThe final output of Lesson1 Lab2; a listofdicts generated by PANDAS:')
print(json.dumps(listofdicts[0:2], indent=4))  # print a small sample of Lab2 listofdicts output


# INTRODUCING AN I-M-P-O-R-T-A-N-T BUILDING BLOCK TOPIC: PYTHON FUNCTIONS

one_command=['show ip interface brief | include 1500']
many_commands=['show ip interface brief','show vrf','show arp vrf mgmt','show ip route']

arista={ "ip": "172.16.14.214", "username": "admin", "password": "password", "device_type": "arista_eos"}

def first_function(device_info, commands):
    print(device_info)
    print('\n')
    with ConnectHandler(**device_info) as ssh:
        output = ""
        for command in commands:
            print(command) 
            output += ssh.send_command(command) + "\n"
        return output.split('\n')

def nouppercase (object_name):
   return [i for i in dir(object_name) if re.match(r'^[a-z,0-9]+(_[a-z]+)?$', i)]

def underscoreinthemiddle (object_name):
   return [i for i in dir(object_name) if re.match(r'^[a-z]+(_[a-z]+)?$', i) and re.match(r'^\w+_\w+?$', i)]

ticket1='[i for i in listofstrs]'
ticket2= 'for i in listofdicts: print (i[0])'
