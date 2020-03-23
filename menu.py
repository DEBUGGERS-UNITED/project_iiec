import os

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
	else:
		print("INVALID CHOICE!! TRY AGAIN!!")
		home_screen()
		
		
#the yum_config aims to configure the repo file required for installation of a software using yum		
def yum_config():
    os.system('cp hello.repo /etc/yum.repos.d/')

# the yum install will install any software whose name is passed to it
def yum_install(software):
    os.system('yum install {}'.format(software))




def rhel_essentials():
	#write your code here
	print("rhel_essentials")

def file_manager():
	#write your code here
	print("file and package manager")

def network():
	#write your code here
	print("network and security")

def docker():
	#write your code here
	print("docker services")
		

def other():
	#write your code here
	print("other services")
		
			
#code for test run
home_screen()	
		
	
		

