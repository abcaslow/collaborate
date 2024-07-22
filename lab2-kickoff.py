# import the netmiko and re libraries
import netmiko
import re
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

print('\nThe original NETMIKO command that establised a connection to a network device. Feel free to copy & paste.')
print("\nnetmiko.ConnectHandler(ip='172.16.14.214',username='admin',password='password',device_type='arista_eos')\n")
print('===============================================================')
print('\nThe final output of Lab1: a listoflistsofstr that originiated from a CLI command run via SSH.\n')
print(listoflistsofstr)
