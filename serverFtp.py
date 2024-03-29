#!/usr/bin/python
from time import sleep, time
import socket, sys, threading
from os.path import exists, isfile
from os import system, makedirs, getcwd
from ftp_parent import MAIN
from sys import exit
import struct

# Global Stuff
global localhost, serverPort, conn, sock
serverPort = 5004
backlog = 5
credintials = [""]*3
APC_Downloads = ""
connectedOnce = False
totalConnections = 0
actionData = "0"
DOWNLOAD="1"
UPLOAD="2"
RECONNECT="3"
cwd = getcwd()

def initiatePath():
	from platform import platform
	if "linux" in platform().lower():#for linux
		APC_Downloads = cwd+"/APC-Downloads/"
	elif "darwin" in platform().lower():#for macos
		APC_Downloads = cwd+"/APC-Downloads/"
	elif "windows" in platform().lower():#for windows
		APC_Downloads = cwd+r'\ APC-Downloads\ '.replace(" ", "")
	else:
		APC_Downloads = "APC-Downloads"
		pass
	return APC_Downloads 

try:
	credintials = open("now-ip.txt", 'r').readlines()
except FileNotFoundError as e:
	print("FileNotFoundError: [Errno 2] No such file or directory: \'now-ip.txt\'")
	exit(0)

def getLocalIP():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("8.8.8.8", 80))
	ip = s.getsockname()[0]
	s.close()
	return ip

class server(MAIN):
	''' Constructor to Establish Bind server once an object made'''
	def __init__(self, localhost, serverPort):	# Connect Tcp
		global bcklog, count, sock
		self.servSock = socket.socket()#tcp
		#sock = self.servSock
		try:
			self.servSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			self.servSock.bind((localhost, serverPort))# bind((host,Port))
			#print count #testin a global variable
		except Exception as e:
			print("[Bind ]", e)
			sys.exit()

	def accept(self):
		global conn, addr, connectedOnce, totalConnections, actionData
		while True:
			try:
				self.servSock.listen(backlog)
				self.conn, self.addr = self.servSock.accept()
				conn = self.conn
				connectedOnce = True
				totalConnections +=1
				print("Client's added Successfully")
				#print("This is a connection: ", conn) #testing
				actionData = "0"
				main()
			except Exception as e:
				print("[conn Error ]", e)
				exit()
	def runThis(self):
		self.accept()
		
	def exit(self):
		self.conn.close()

	def down(self, name, conn):
		while True:
			MAIN.download(name, conn)

def main():
	buffer = 1024
	global localhost, serverPort, conn, sock, actionData, totalConnections
	while True:
		reset = 0
		print("Waiting an Action.. totalConnections=", totalConnections)

		# while (actionData != "1" and actionData != "2"):
		# 	if(actionData == "3"):
		# 		reset = 1
		# 		break
		while actionData == "0":
			try:
				print("Here")
				actionData = str(conn.recv(buffer).decode('utf-8'))
				if actionData == "1" or actionData != "2" or actionData != "3":
					continue
			except Exception as e:
				print("line 100"+e)
				actionData = "3"
		print("Action totalFilesReceived= "+actionData)
		if(actionData == "3"):
			conn.close()
			break
		# if actionData != "1" and actionData != "2":
		# 	print("line 104: "+ actionData)
		# 	actionData = "3"

		# if str(actionData) != "3":
		# 	print("line 110")
		try:
			input("Input anything")
			conn.send(actionData.encode("UTF-8"))
		except Exception as e:
			print (e)
		print("actionData totalFilesReceived= ", actionData)

		fileSize = 0
		# getting file size
		# while (fileSize == 0):
		# 	fileSize = int(conn.recv(buffer).decode("UTF-8"))
		# conn.send(str.encode("1"))
		# print("bufferRcv: ", int(fileSize))

		if str(actionData) == DOWNLOAD:# Download
			print("Client is uploading a file...")
			# name = input("Rename the file: ") # raw_input = string
			start = time()
			serverObj.download(conn, int(fileSize), APC_Downloads)
			end = time()
			print("Downloaded in: {}".format(end-start))
			actionData = "0"

		elif str(actionData) == UPLOAD:# Upload
			fileUpload  = input("Choose a file: ") # raw_input = string
			while (not isfile(fileUpload)): # to check if file exists.)
				fileUpload  = input("Choose a file: ") # raw_input = string
			start = time()
			serverObj.upload(fileUpload, conn, buffer)
			end = time()
			print("Uploaded in: {}".format(end-start))
			actionData = "0"
		elif str(actionData) == RECONNECT:# Reconncet
			print("RECONNECT actionData: ", actionData)
			break
		else:
			print("Something went Wrong!")
			continue
			#break

if  __name__ == "__main__":
	finishThread = threading.Event()
	# cmd = "curl -u {}:{} https://now-dns.com/update?hostname={}".format(credintials[0].replace("\n", ""), credintials[1].replace("\n", ""), credintials[2].replace("\n", ""))
	# system(cmd)
	APC_Downloads = initiatePath()
	if not exists(APC_Downloads):
		makedirs(APC_Downloads)

	try:
		localhost = getLocalIP()
		serverObj = server(localhost, serverPort)

		print("({}, {})".format(localhost, serverPort))
		print("[+] Server is UP!")
		print("[+] Files will be downloaded to: "+APC_Downloads)
	except Exception as e:
		print ("[Main ] ",e)
		exit()

	acceptThread = threading.Thread(name = "Accepting Connections", target=serverObj.accept)
	acceptThread.start()
	# while not connectedOnce:
		# pass
	# acceptThread.join() # wait till this thread is finished.
	#print("This is a connection: ", conn) # testing conn global variable

	# main()
	