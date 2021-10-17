# Import statements, allows for more commands to be used
import os
from time import sleep

# Installing termcolor package
os.system("echo 'ENTER-PASSWORD' | sudo -S apt install -y python3")
sleep(.1)
os.system('sudo apt install -y python-pip')
sleep(.1)
os.system('pip install termcolor')
sleep(.1)
os.system('clear')

# Importing termcolor
from termcolor import colored, cprint

# Declaring a statement that allows me to print in GREEN!
print_green = lambda x: cprint(x, 'green', attrs=['bold'])

# Peterson Power Version 2!
print_green("---------------------------------")
print_green("|	PETERSON POWER V2	|")
print_green("---------------------------------")

# Print statement, sleep for 1.5 seconds, and then run the command
print_green("\nEditing where updates are installed from")
sleep(1.5)
os.system('sudo cp "sources.list" "/etc/apt/sources.list"')
print_green("\nUpdating repositories\n")
sleep(1.5)
os.system('sudo apt update -y')
print_green("\nUpgrading repositories\n")
sleep(1.5)
os.system('sudo apt upgrade -y')
print_green("\nUpgrading Firefox to Latest Version\n")
sleep(1.5)
os.system('sudo apt install -y firefox')
print_green("\nDisabling the Root Account\n")
sleep(1.5)
os.system("echo -e '0000\n0000' | sudo passwd root")
sleep(.1)
os.system('sudo passwd -l root')
print_green("\nEnabling and Configuring the Firewall\n")
sleep(1.5)
os.system('sudo apt install -y ufw')
sleep(.1)
os.system('sudo ufw enable')
sleep(.1)
os.system('sudo ufw default reject incoming')
sleep(.1)
os.system('sudo ufw default allow outgoing')