import subprocess
import socket
from IPy import IP
import subprocess
import optparse


# ------------------------------------------------------PORT SCANNER--------------------------------------------------------------
def scan_port(ipaddress, port):
    try:
        # socket descriptor,
        sck = socket.socket()  # socket library aloows us to make a connection over internet
        sck.settimeout(
            0.1)  # some ports will take a longer time to connect to and some ports will take less time to connect
        # this is (0.1) a price to want to pay in order to scan the target faster
        sck.connect((ipaddress, port))
        try:
            portInfo = sck.recv(1024)  # 1024 byte           #below for  clean output
            print('[--> open port ' + str(port) + ' : ' + str(portInfo.decode().strip('\n')))
        except:
            print('[--> open port ' + str(port))
    except:
        pass


def convert_ip(ip):  # this functon about converting domain name to ip address so that
    # usage of program will be allowed with domain name or ip, without any error
    try:
        IP(ip)
        return (ip)
    except ValueError:
        return socket.gethostbyname(ip)


# -----------------------------------------------------MAC CHANGER------------------------------------------------------------------

def mac_changer(user_mac_address):
    print("mac changer started")

    # subprocess library provide execution of linux commands in python scripts.
    # So that we can execute many linux commands at once in python.

    subprocess.call(["ifconfig", "eth0", "down"])
    subprocess.call(["ifconfig", "eth0", "hw", "ether", user_mac_address])
    subprocess.call(["ifconfig", "eth0", "up"])
    print("new macc address : " + user_mac_address)


# ----------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":

    # optParse library provide get inputs, arguments from command line
    # usage structure of program  defined below.

    # usage -->  python3  netScanner.py -m 00:10:10:20:20:30
    # usage2 --> python3  netScanner.py -t 192.168.1.1
    # usage3 --> python3  netScanner.py -t www.shiftdelete.net

   
    parse_object = optparse.OptionParser()
    parse_object.add_option("-t", dest="ip", help= "-t option usage: python3  netScanner.py -m 00:10:10:20:20:30")
    parse_object.add_option("-m", dest="mac_address", help= "-m option usage: python3  netScanner.py -t 192.168.1.1")
    
    '''
    parse_object.add_option("-a", dest="arp_poison", help= "")
    parse_object.add_option("-s", dest="show_network_users", help= "")    
    '''
    (inputs, arguments) = parse_object.parse_args()

    if (inputs.ip):
        new_ip = convert_ip(inputs.ip)
        print('\n\n' + '[--> Scanning Target] ' + str(new_ip))
        for port in range(1, 65536):
            scan_port(new_ip, port)

    if (inputs.mac_address):
        user_mac_address = inputs.mac_address
        mac_changer(user_mac_address)
