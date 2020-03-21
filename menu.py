import os
os.system("clear")
os.system("tput setaf 1")
print("\t\t\tWelcome to Terminal User Interface(TUI)")
print("\t\t\t---------------------------------------")
print("\t\t\t\tTUI makes your life easier.")
os.system("tput setaf 7")
while True:
	print("""PRESS 1:To see date
PRESS 2:To see calendar
PRESS 3:To create new user
PRESS 4:To see network configurations
PRESS 5:To exit""")
	print("")
	print("Enter your choice: ",end="")
	ch=input()
	c=int(ch)
	if c==1:
		os.system("date")
		print("")
	elif c==2:
		os.system("cal")
		print("")
	elif c==3:
		username=input("Enter a username: ",end='')
		os.system("useradd {}".format(username))
		print("")
	elif c==4:
		os.system("ifconfig")
		print("")
	elif c==5:
		break
	else:
		print("Invalid Choice! Try again.")
		print("")
