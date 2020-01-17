

# pylint: disable=unused-wildcard-import
import sys
import math
import random
import time
import zlib
from socket import *

def sendPackets():
	serverIP = 'localhost' # DESIRED DESTINATION IP ADDRESS
	serverPort = 27015 # DESIRED DESTINATION PORT NUMBER
	clientSocket = socket(AF_INET, SOCK_DGRAM)
	print('Socket Established, destination: ' + serverIP + ' : Port ' + str(serverPort))

	data = bytes(str(int(random.uniform(0,1000))), 'ascii')
	macAddr = b'9D-4D-89-77-93-5F'
	packet = b'{\n	"macAddr":"'+ macAddr +b'",\n	"Data":' + data + b'\n}'


	clientSocket.sendto(packet, (serverIP, serverPort))
	while(1):
		time.sleep(1)
		data = bytes(str(int(random.uniform(0,1000))), 'ascii')
		packet = b'{\n	"macAddr":"'+ macAddr + b'",\n	"Data":' + data + b'\n}'
		clientSocket.sendto(packet, (serverIP, serverPort))
		print('Packet sent! Data: %d', data)

	clientSocket.close()

def main():
	sendPackets()

main()
