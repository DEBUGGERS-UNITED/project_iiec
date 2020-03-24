import os
import os.path
import socket
import sys

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
		create_web_server()
		home_screen()
	elif ch==2:
		file_add()
		personalised_link()
		home_screen()
	elif ch==3:
		print(get_ip())
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
		
		
		
		
#the yum_config aims to configure the repo file required for installation of a software using yum		
def yum_config():
    os.system('su -c "cp hello.repo /etc/yum.repos.d/" > check_config.txt 2> check_config.txt')

# the yum install will install any software whose name is passed to it
def yum_install(software):
    os.system('su -c "yum install {}" > check_install.txt 2> check_install.txt'.format(software))


#function to check internet connection
#this function stores the output of ping cmd in a file net.txt and if the ouput is a single line then no interent and if more than one line then internet is working. The fuction returns a boolean that is True if net is working and False if not working.
def net_connect():
	os.system("ping -c 3 google.com > net.txt 2> net.txt")
	f=open("net.txt","r")
	count=0
	for line in f:
		count=count+1
	if count>1:
		return True
	elif count==1:
		return False
	else:
		print("error try gain")
		
	f.close()
	os.system("rm -f net.txt")
	
#function to create web server
def create_web_server():
	print('Require root access for configuring yum')
	yum_config()
	print('Require root access for installing httpd')
	yum_install('httpd')
	print('Enabling web server will require root password. Sorry for troubling again and again.\n')
	os.system('su -c "systemctl enable httpd"')
	file_add()
	print("Web server configured successfully at port 80\n")
	take1 = input('Do you want to check your website?(y/n)')
	if take1 is 'y':
		personalised_link()
					
#Addition of web files					
def file_add():
	print("Enter complete location of your web file here:")
	web=input()
	val=os.path.isfile("{}".format(web))
	if val==False:
		print("Wrong Location")
		print("Please enter proper location!!")
		print("------------------------------")
		file_add()
	else:
		os.system("cp {} /var/www/html/".format(web))
		print("File added successfully!!")
		print("Do you wish to add more files:If yes,enter 1 else enter 0 to go back to home screen: ",end='')
		inp=int(input())
		if inp==1:
			file_add()

def get_ip():
	hostname=socket.gethostname()
	ip_addr=socket.gethostbyname(hostname)
	return ip_addr

def personalised_link():
	print("")
	print("Enter file name of your webpage: ",end="")
	web=input()
	ip_add=get_ip()
	os.system("curl http://{}/{}".format(ip_add,web))
	while True:
		print("\nDo you wish to see more web files?(yes/no): ",end='')
		ch=input()
		if ch=='yes':
			personalised_link()
		elif ch=='no':
			home_screen()
		else:
			print("Invalid Input!!Try again")
			
				
# driver code for testing dont add any functions below this add above this comment
home_screen()
