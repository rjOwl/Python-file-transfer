#!/usr/bin/python
# This is client file
"""
Reference:
	http://eli.thegreenplace.net/2011/05/18/code-sample-socket-client-thread-in-python
	https://docs.python.org/2/library/threading.html
"""

import socket, threading
from time import sleep
from ftp_parent import MAIN
from os.path import exists
from os import system
from os.path import basename

# Global Stuff
#serverIP = socket.gethostbyname(socket.gethostname())
serverIP = 'chat.001www.com' # public ip
serverPort, buffer =\
 5004,1024 #Bytes
path = ""

class client(MAIN): #inherit from MAIN
	''' Constructor to Establish Connection once client is up'''
	def __init__(self, serverIP, serverPort, sock):	# Connect Tcp
		global buffer
		#self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #tcp
		#sock = self.sock
		try:
			sock.connect((serverIP, serverPort))
			print("[+] Connected Successfully")
		except Exception as e:
			print("[Connecting to Server]", e)

def main():
	global serverIP, serverPort, sock, path, fileName

	sock = socket.socket() #tcp
	localGlobal = str(input("1- Global\n2- Local\n>> "))
	if(localGlobal == "1"):
		choice = str(input("1- 'chat.001www.com'\n 2- '192.168.1.6'\n>> "))
		if (choice == "1"):
			serverIP = "chat.001www.com"
		elif(choice == "2"):
			serverIP = "192.168.1.6"
		else:
			system("clear")
		clientObj = client(serverIP, serverPort, sock) # object of class client
	elif(localGlobal == "2"):
		print("1- open hotspot in your phone\n2- Connect your PC to it.\n3- Get the ip of your PC using 'ifconfig' or 'ip addr'.\n4- Input ip when done.")
		serverIP = input("Ip: ")
		clientObj = client(serverIP, serverPort, sock) # object of class client
	else:
		system("clear")
	print("Current Ip:", serverIP)

	# For android; making a folder for downloaded files
	if(exists("/sdcard/")):
		if(not exists("/sdcard/Python_Downloads")):
			system("mkdir /sdcard/Python_Downloads")
	path = "/sdcard/Python_Downloads/"

	while True:
		chooz = input("Input:\n1- To Upload.\n2- To Download.\n>> ") # input = int
		if chooz == "1":# Upload
			fileUpload = input("File to upload: ")
			if not exists(fileUpload):
				print("""[-] Path isn't right""")
				continue

			fileName = basename(fileUpload)
			sock.send(str(chooz).encode("UTF-8")) # covnert it from string into byte streams to be in proper format.

			clientObj.upload(fileUpload, sock, fileName)
			continue
		elif chooz == "2":# Download
			sock.send(str(chooz).encode("UTF-8")) # covnert it from string into byte streams to be in proper format.
			# name = input("Rename the file: ") # raw_input = string

			name = "{}{}".format(path, fileName)
			clientObj.download(name, sock)
			continue
		else:
			print("Choose \"1\" or \"2\"")

# testing
if  __name__ == "__main__":
	main()
