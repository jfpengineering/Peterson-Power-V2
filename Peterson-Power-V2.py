# Import statements, allows for more commands to be used
import os
from time import sleep

# Installing termcolor package
os.system('sudo apt install -y python3')
os.system('sudo apt install -y python-pip')
os.system('pip install termcolor')
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