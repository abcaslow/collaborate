from devices_cloudmylab import *
from netmiko import ConnectHandler

def read_commands_from_file(filename):
    with open(filename, 'r') as file:
        return file.readlines()

def run_commands_on_device(device_info, commands):
    print(device_info, commands)
    with ConnectHandler(**device_info) as ssh:
       ssh.enable()  # Enter privileged mode
       output = ""
       for command in commands:
           output += ssh.send_command(command) + "\n"
       return output

if __name__ == "__main__":

    device_details = [arista, iosxe]
    commands = read_commands_from_file('commands.txt')

    for device in device_details:
        device_output = run_commands_on_device(device, commands)
        if device_output:
            print(f"Device: {device['host']}")
            print("=" * len(device['host']))
            print(device_output)
        else:
            print(f"Failed to retrieve output for device: {device['host']}")

