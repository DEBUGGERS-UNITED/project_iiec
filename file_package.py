import os


#the yum_config aims to configure the repo file required for installation of a software using yum		
def yum_config():
    os.system('su -c "cp hello.repo /etc/yum.repos.d/" > check_config.txt 2> check_config.txt')

# the yum install will install any software whose name is passed to it
def yum_install(software):
    os.system('su -c "yum install {}" > check_install.txt 2> check_install.txt'.format(software))

