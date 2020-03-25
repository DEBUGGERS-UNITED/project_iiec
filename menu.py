import os
import os.path
import socket
import sys
import network as net

def default():
	os.system("clear")
	os.system("tput setaf 1")
	print("\t\t\tWelcome to Terminal User Interface(TUI)")
	print("\t\t\t---------------------------------------")
	print("\t\t\t\tTUI makes your life easier.")
	os.system("tput setaf 7")

def home_screen():
	default()
	print("")
	os.system("tput setaf 5")
	print("\t\tHOME SCREEN")
	print("\t\t-----------")
	os.system("tput setaf 7")
	print("""PRESS 1: RHEL ESSENTIALS\t\tPRESS 2: FILE AND PACKAGE MANAGEMENT
PRESS 3: NETWORK AND SECURITY\t\tPRESS 4: DOCKER SERVICES
PRESS 5: OTHER SERVICES\t\t\tPRESS 0: EXIT""")
	print("")
	print("ENTER CHOICE: ",end='')
	ch=int(input())
	print("\nYour Choice: ",ch)
	if ch==1:
		rhel_essentials()
	elif ch==2:
		file_manager()
	elif ch==3:
		network()
	elif ch==4:
		docker()
	elif ch==5:
		other()
	elif ch==0:
		print("THANKS FOR USING OUR SERVICES!!")
		sys.exit()
	else:
		print("INVALID CHOICE!! TRY AGAIN!!")
		home_screen()

def network():
	default()
	os.system("tput setaf 5")
	print("\tNETWORK SERVICES")
	print("\t----------------")
	os.system("tput setaf 7")
	print("")
	print("PRESS 1: Create new web server\t\t\tPRESS 2: Configure existing web server\nPRESS 3: To see IP\t\t\t\tPRESS 4: To go back to home screen")
	print("\nEnter Choice: ",end='')
	ch=int(input())
	if ch==1:
		net.create_web_server()
		home_screen()
	elif ch==2:
		file_add()
		net.personalised_link()
		home_screen()
	elif ch==3:
		print(net.get_ip())
		while True:
			print("Press y to continue: ",end='')
			ch2=input()
			if ch2=='y' or ch2=='Y':
				network()
	elif ch==4:
		home_screen()
	else:
		while True:
			print("Invalid Choice!!Try Again")
			print("\nPress y to continue: ",end="")
			x=input()
			if x=='y':
				network()
				
