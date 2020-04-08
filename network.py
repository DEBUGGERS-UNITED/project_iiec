import file_package as fp
import os
import os.path
import socket
import menu as men
import essentials

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
	essentials.check_or_switch()
	#print('Require root access for configuring yum')
	fp.yum_config()
	#print('Require root access for installing httpd')
	fp.yum_install('httpd')
	#print('Enabling web server will require root password. Sorry for troubling again and again.\n')
	#os.system('su -c "systemctl enable httpd"')
	os.system("systemctl enable httpd")
	file_add()
	print("Web server configured successfully at port 80\n")
	take1 = input('Do you want to check your website?(y/n)')
	if take1 is 'y':
		personalised_link()

#function to get ip address of host system
def get_ip():
	#hostname=socket.gethostname()
	#ip_addr=socket.gethostbyname(hostname)
	#return ip_addr
	os.system("hostname -I > check.txt")
	f = open("check.txt","r")
	s = f.read().split(' ')
	f.close()
	return s[0]


#function to open we page using curl command
def personalised_link():
	print("")
	print("Enter file name of your webpage: ",end="")
	web=input()
	val=os.path.isfile("/var/www/html/{}".format(web))
	if val==True:
		ip_add=get_ip()
		os.system("curl http://{}/{}".format(ip_add,web))
	elif val==False:
		print("File name not found!! Try Again")
		personalised_link()
	while True:
		print("\nDo you wish to see more web files?(yes/no): ",end='')
		ch=input()
		if ch=='yes':
			personalised_link()
		elif ch=='no':
			men.home_screen()
		else:
			print("Invalid Input!!Try again")

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
		print("Do you wish to add more file(y/n): ",end='')
		inp=input()
		while True:
			if inp=='y' or inp=='Y':
				file_add()
			elif inp=='n' or inp=='N':
				personalised_link()

			else:
				print("Invalid Input, Try Again!!")
				input("press enter to continue....")

#functions for ssh server
def create_ssh_server():
    fp.yum_config()
    fp.yum_install('sshd')

def run_ssh_command():
    ip = input('Enter the ip of the remote system: ')
    command = input('Enter the command to perform: ')
    os.system('ssh {} {}'.format(ip,command))

def upload_file():
    ip = input('Enter the ip of the remote system: ')
    location = input('Enter the location where you want to upload the file')
    filename = input('Enter the file name on your system: ')
    os.system('scp {} {}{}'.format(filename,ip,location))

def download_file():
    ip = input('Enter the ip of the remote system: ')
    mylocation = input('Enter the location where you want to download the file: ')
    remloc = input('Enter the location of file that you want to download: ')
    os.system('scp -r {}{} {}'.format(ip,remloc,mylocation))


			
