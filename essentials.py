import os
def check_who_am_i():

	os.system("whoami > user.txt")
	f=open("user.txt","r")
	user = f.read().strip()
	f.close()
	return user

def check_or_switch():
	
	x = check_who_am_i()
	if x == 'root':
		print("Root Account")
	else:
		print("Please enter password for root account to enable configuration=")
		os.system("su")
	os.system("rm -f user.txt")
check_or_switch()
