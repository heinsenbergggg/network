This is a very useful Python script for network administrators to monitor the devices on a network by pinging  IP address on a subnet , and to update the package , displays the size of the disk space , on Debian with remote connection.


You need four Python modules - subprocess , pxssh , pexpect and getpass. 

At first, the program asks the user to input a network address. After the programs asks the first and the last ip of the network to ping. It’s will display the ip who are up and down , the ip who are up will be write on file “ip.txt”. Now we will update the package and display the size of the disk space with ssh connection. The program asks who user to intput the ip , and the program will update the package and displays the size of the disk space.
