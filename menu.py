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
    os.system('su -c "yum install {}"'.format(software))


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
		
			
#code for test run
if net_connect():
	print("internet working")
else:
	print("internet not working")	
	
default()
print('''\tWHAT DO YOU WANT TO DO?
\t1. Set up Web server''')

take = int(input("\nEnter your choice: "))
	
if take is 1:
	if net_connect():
		if mount_check():
			yum_config()
			yum_install('httpd')
			print('Enabling web server will require root password. Enter below.\n')
			os.system('su -c "systemctl enabling httpd"')
			file_add()
			print("Web server configured successfully at port 80\n")
			take1 = input('Do you want to check your website?(y/n)')
			if take1 is 'y':
				personalised_link()
			
