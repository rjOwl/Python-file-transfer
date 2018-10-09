import socket, sys, threading
from time import sleep
from os.path import basename, getsize, exists

buffer = 1024 #Bytes
fileFinished = bytearray("ENDOFFILE".encode("UTF-8"))

class MAIN(object):
	totalFilesReceived=0
	def download(self, conn, fileSize, path=""): # conn will be used in receiving the data.
		print("In download...")
		# global buffer
		file = ""
		fileName = conn.recv(buffer).decode("UTF-8") # If there is no (buffer) expect something like> Error: int is required.
		self.totalFilesReceived+=1
		if("NAME" in str(fileName)):
			file = path + basename(fileName[:-4])
			print(str(self.totalFilesReceived)+"- File name bieng downloaded: {}".format(basename(file)))
			if self.checkExistence(conn, file):
				print("File Exists")
				return 1
		else:
			print("UNKNOWN File Name: Name Error")
			conn.send("1".encode("UTF-8"))
			return 1
		try:
			with open(file, "wb") as destFile: # open file in writing binary mode
				#i=0 # testing
				# while (True):
				data = conn.recv(buffer) # If there is no (buffer) expect something like> Error: int is required.
				while(data):# while there's data being sent
					if(data.endswith(fileFinished)):
						data = data[:-9]
						newFileByteArray = bytearray(data) # covnert it from string into byte streams to be in proper format (In python3).
						destFile.write(newFileByteArray)  # write to file.
						#print (newFileByteArray) # testing
						break
					else:
						newFileByteArray = bytearray(data) # covnert it from string into byte streams to be in proper format (In python3).
						destFile.write(newFileByteArray)  # write to file.
						#print (newFileByteArray) # testing				
						data = conn.recv(buffer)
				# break
						#i+=1 # testing
			print("Downlded Successfully")
			destFile.close() # close the file
			print("File Closed Successfully")
			conn.send("1".encode("UTF-8")) # sned 1 to confirma that file's Successfully downloaded.
			return 1
			# if(getsize(file) >= fileSize and getsize(file) != 0):
			#print ("Lines totalFilesReceived:", i ) # testing
		except Exception as e:
			print ("[-] In ftp_parent.download()\n>> ", e)
			with open(path+"Error Logs", "a") as logsFile:
				logsFile.write("####################### In Downloading (ftp_parent) #######################\n")
				logsFile.write(str(e))
			logsFile.close()
			return-1

	def upload(self, file, sock, buffer): # See python> tutorial> File 
		try:
			name = file + "NAME"
			# name = basename(file)+"NAME"
			sock.send(str(name).encode("UTF-8"))
			start = "0"
			while start == "0":
				start = str(sock.recv(buffer))

			with open(file, "rb") as UpFile:
				#i = 0 # testing
				for eachline in UpFile: # read file line by line
					newFileByteArray = bytearray(eachline) # turn the line into bytes and store it in a variable.
					#print (newFileByteArray) #testing
					sock.send(newFileByteArray) # covnert it from string into byte streams to be in proper format.
					#i+=1 # testing
			UpFile.close()
			sock.send(fileFinished) # Will send it to confirm an end of file.
			print("Uploaded Successfully")
			#return
			#print ("Lines sent:", i) # testing 
		except Exception as e:
			print("[-] In ftp_parent.upload()\n>> ", e)
			path = file.replace(basename(file), "")
			with open(path+"Error Logs", "a") as logsFile:
				logsFile.write("####################### In Uploading (ftp_parent) #######################\n")
				logsFile.write(str(e))
				logsFile.write("\n")
			logsFile.close()
			return -1

	def checkExistence(self, conn, fileName=str):
		if(exists(fileName)):
			if conn.send("1".encode("UTF-8")):
				return True #exists
		else:
			if conn.send("0".encode("UTF-8")):
				return False

	def android(self, conn, fileSize, path=""):
		file = ""
		fileName = conn.recv(buffer).decode("UTF-8") # If there is no (buffer) expect something like> Error: int is required.
		if("NAME" in str(fileName)):
			file = fileName[:-4]
			if conn.send("1".encode("UTF-8")):
				print("Response sent")
			# file = path + file
			file = path + basename(file)
			print("File name bieng downloaded: {}".format(basename(file)))
		try:
			with open(file, "wb") as destFile: # open file in writing binary mode
				#i=0 # testing
				# while (True):
				data = conn.recv(buffer) # If there is no (buffer) expect something like> Error: int is required.
				while(data):# while there's data being sent
					if(data.endswith(fileFinished)):
						data = data[:-9]
						for byte in data:
							newFileByteArray = bytearray(byte) # covnert it from string into byte streams to be in proper format (In python3).
							destFile.write(newFileByteArray)  # write to file.
						break
					else:
						for byte in data:
							newFileByteArray = bytearray(byte) # covnert it from string into byte streams to be in proper format (In python3).
							destFile.write(newFileByteArray)  # write to file.
						#print (newFileByteArray) # testing				
						data = conn.recv(buffer)
				# break
						#i+=1 # testing
			print("Downlded Successfully")
			destFile.close() # close the file
			print("File Closed Successfully")
			conn.send("1".encode("UTF-8")) # sned 1 to confirm a that file's Successfully downloaded.

			# if(getsize(file) >= fileSize and getsize(file) != 0):
			#print ("Lines totalFilesReceived:", i ) # testing
		except Exception as e:
			print ("[-] In ftp_parent.download()\n>> ", e)
			with open(path+"Error Logs", "a") as logsFile:
				logsFile.write("####################### In Downloading (ftp_parent) #######################\n")
				logsFile.write(str(e))
				logsFile.write("\n")
			logsFile.close()
			return-1


# 		conn.send("Choose totalFilesReceived".encode("UTF-8"))

		# actionData = 0
		# while (actionData != 0 and actionData != 0):
		# 	buffer = actionData = int(conn.recv(100).decode("UTF-8"))

		# conn.send("Buffer totalFilesReceived".encode("UTF-8"))

		# actionData = 0
		# data = ""
		# while (actionData != 0 and actionData != 0):
		# 	actionData = data = conn.recv(buffer).decode("UTF-8") # If there is no (buffer) expect something like> Error: int is required.
