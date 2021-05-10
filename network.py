#!/usr/bin/env python
import subprocess
import os
from pexpect import pxssh
import getpass


FNULL = open(os.devnull, 'w')

def Network():
        network = raw_input('Enter network [ex :192.168.5.0]: ')[0:-1]   # the subnet to scan 
        first_ip = raw_input('First IP: ') 	# first ip of the subnet
        ending_ip = raw_input('Ending IP: ')	# the last ip of the subnet

        for i in range(int(first_ip), int(ending_ip)):

            try:
                subprocess.check_call(['ping', '-c', '1', network + str(i)], stdout=FNULL,stderr=FNULL)

            except (OSError, subprocess.CalledProcessError):

                print "[-] DOWN {}{}".format(network,i)    # screen the host down
            else:

                print "[+] UP {}{}".format(network,i)     # screen the host up

path = '/home/rooty/my_app/network/ip.txt'  
FNULL = open(path,'r')      # write the host up in the file ip.txt

Network()


try:
    s = pxssh.pxssh()
    hostname = raw_input('please enter the ip [ex :192.168.5.0]: ')
    username = raw_input('username: ')
    password = getpass.getpass('password: ')
    s.login (hostname, username, password)
    s.sendline ('apt-get upgrade -y;df -h ')   #  command to run
    s.prompt()             # match the prompt
    print s.before          # print the result 
    s.logout()              
except pxssh.ExceptionPxssh, e:
    print "pxssh failed on login."
    print str(e)
