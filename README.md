# portScanner Tool
# Aim
PortScanner python module scan all ports of given target and show us all open ports. 

It also shows the services running on the port, if there is. And mac changer module is added. 

It change the exist mac address with given one. So that we can see vullnerable ports and increase the anonimity with changed mac address.

# Methodology
Program take inputs from command line by using optParse library.

According to inputs, program go into mac changer or port scanner module.

At the mac changer module, subprocess library used to execute many linux commands in python at once.

At the port scanner module all ports are scanning with for loop (1-65536). And IPy library used to convert domain name to ip address.

IPy library provide, target can be domain name or ip address.

# Requirements

```bash
>apt install python3-pip
>pip install IPy
``` 

# Usage

```bash
 root@kali:/# python3 portScanner.py -h     or    python3 portScanner.py -help
 root@kali:/# python3 portScanner.py -t 192.168.1.1
 root@kali:/# python3 portScanner.py -t www.shiftdelete.net
 root@kali:/# python3 portScanner.py -m 00:22:44:22:22:00
```                                           
# Examples
For metasploitable machine obtained results below 
```bash
root@kali:~/Desktop# python3 portScanner.py -t 192.168.127.155
[--> Scanning Target] 192.168.127.155
[--> Open Port 21 : 220 (vsFTPd 2.3.4)
[--> Open Port 22 : SSH-2.0-OpenSSH_4.7p1 Debian-8ubuntu1
[--> Open Port 23
[--> Open Port 25 : 220 metasploitable.localdomain ESMTP Postfix (Ubuntu)
[--> Open Port 53
[--> Open Port 80
[--> Open Port 111
[--> Open Port 139
[--> Open Port 445
[--> Open Port 512
[--> Open Port 513
[--> Open Port 514 : 
[--> Open Port 1099
[--> Open Port 1524 : root@metasploitable:/# 
[--> Open Port 2049
[--> Open Port 2121
[--> Open Port 3306
[--> Open Port 3632
[--> Open Port 5432
[--> Open Port 5900 : RFB 003.003
[--> Open Port 6000
[--> Open Port 6667
[--> Open Port 6697 : :irc.Metasploitable.LAN NOTICE AUTH :*** Looking up your hostname...
[--> Open Port 8009
[--> Open Port 8180
[--> Open Port 8787                                                                                                      
[--> Open Port 37996                                                                                                     
[--> Open Port 42607                                                                                                     
[--> Open Port 46887                                                                                                     
[--> Open Port 55443                                                                                                     

```   
For Github scanning 
```bash
root@kali:~/Desktop# python3 portScanner.py -t www.github.com
[--> Scanning Target] 140.82.121.4
[--> Open Port 22
[--> Open Port 443
```
As we see program automatically convert domain name to ip address both usage (domain name, ip address) is available

Let's see how can we change mac address of Linux.
```bash
root@kali:~/Desktop# python3 portScanner.py -m 00:00:11:22:22:22
mac changer started
new macc address : 00:00:11:22:22:22
```
# References

https://pypi.org/project/IPy/

https://docs.python.org/3/library/subprocess.html

https://www.tutorialspoint.com/python_penetration_testing/python_penetration_testing_network_scanner.htm

# Demo video 
https://youtu.be/zZos7xMuIBQ
