import file_package as fp
import os
import os.path
import socket
import menu as men

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
	fp.yum_config()
	print('Require root access for installing httpd')
	fp.yum_install('httpd')
	print('Enabling web server will require root password. Sorry for troubling again and again.\n')
	os.system('su -c "systemctl enable httpd"')
	file_add()
	print("Web server configured successfully at port 80\n")
	take1 = input('Do you want to check your website?(y/n)')
	if take1 is 'y':
		personalised_link()

#function to get ip address of host system
def get_ip():
	hostname=socket.gethostname()
	ip_addr=socket.gethostbyname(hostname)
	return ip_addr

#function to open we page using curl command
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
		print("Do you wish to add more files:If yes,enter 1 else enter 0 to go back to home screen: ",end='')
		inp=int(input())
		if inp==1:
			file_add()

			
