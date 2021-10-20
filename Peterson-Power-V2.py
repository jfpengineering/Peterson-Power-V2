# Import statements, allows for more commands to be used
import os
from time import sleep

# Installing termcolor package
os.system("echo 'ENTER-PASSWORD' | sudo -S apt install -y python-termcolor")
sleep(.1)
os.system('clear')

# Importing termcolor
from termcolor import colored, cprint

# Declaring a statement that allows me to print in GREEN!
print_green = lambda x: cprint(x, 'green', attrs=['bold'])

# Declaring an integer to use later
num = 0

# Declaring a function to replace a certain line of text
def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num-1] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()

# Declaring a function to locate a certain line of text
def locate_line(text):
	global num
	file = open(text)
	content = file.readlines()
	the_num = int(content[1])
	num = the_num

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
os.system("echo 'ENTER-PASSWORD' | sudo -S apt install -y firefox")
print_green("\nDisabling the Root Account\n")
sleep(1.5)
os.system("echo 'root:1234' | sudo chpasswd")
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
print_green("\nSecuring LightDM\n")
sleep(1.5)
os.system("echo -e '\nallow-guest=false' | sudo tee -a /etc/lightdm/lightdm.conf")
print_green("\nEnabling Automatic Updates\n")
sleep(1.5)
os.system('sudo rm /etc/apt/apt.conf.d/10periodic')
sleep(.1)
os.system('sudo touch /etc/apt/apt.conf.d/10periodic')
sleep(.1)
os.system("echo 'APT::Periodic::Update-Package-Lists \"1\";\nAPT::Periodic::Download-Upgradeable-Packages \"1\";\nAPT::Periodic::AutocleanInterval \"7\";\nAPT::Periodic::Unattended-Upgrade \"1\";' | sudo tee -a /etc/apt/apt.conf.d/10periodic")
print_green("\nChanging Password Policies\n")
sleep(1.5)
os.system('sudo chmod 666 /etc/login.defs')
sleep(.1)
os.system("grep -n 'PASS_MAX_DAYS' /etc/login.defs | cut -d: -f1 > temp.txt")
sleep(.1)
locate_line('temp.txt')
sleep(.1)
replace_line("/etc/login.defs", num, "PASS_MAX_DAYS	15\n")
sleep(.1)
replace_line("/etc/login.defs", num+1, "PASS_MIN_DAYS	7\n")
sleep(.1)
replace_line("/etc/login.defs", num+2, "PASS_WARN_AGE	8\n")
sleep(.1)
os.system('sudo rm temp.txt')
sleep(.1)
os.system('sudo chmod 644 /etc/login.defs')