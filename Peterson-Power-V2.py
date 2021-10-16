# Import statements, allows for more commands to be used
import os
from time import sleep
from termcolor import colored, cprint

# Declaring a statement that allows me to print in GREEN!
print_green = lambda x: cprint(x, 'green', attrs=['bold'])

# Peterson Power Version 2!
print_green("---------------------------------")
print_green("|	PETERSON POWER V2	|")
print_green("---------------------------------")

# Print statement, sleep for 3 seconds, and then run the command
print_green("\nUpdating repositories\n")
sleep(3)
os.system('sudo apt update')
print_green("\nUpgrading repositories\n")
sleep(3)
os.system('sudo apt upgrade')
print_green("\nUpgrading Firefox to Latest Version\n")
sleep(3)
os.system('sudo apt install -y firefox')