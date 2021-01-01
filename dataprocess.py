
#Importing the required packages
import json
import os
import sys
from datetime import datetime, timedelta 
from tkinter import filedialog, Button, Tk


""" 
	Class for doing Create, Read, Delete operation on the file
"""
class DataProcess: 

	#Constructor
	def __init__(self, fileName, fileAlreadyCreated = False):
		if(os.path.isfile('user.log')):
			with open("user.log", 'r+') as logFile:
				if(logFile.read() == "occupied"):
					print("Someone else is using...Please try again after sometime\n")
					return

		with open("user.log", 'w') as file:
			file.write("occupied")

		root = Tk()
		if(fileAlreadyCreated == True):
			filePath = filedialog.askopenfilename()
			Button(root, text="Quit", command=root.destroy).pack()
			root.mainloop()
			print("Successfully loaded the file +_+ !\n")
		else:
			folderSelected = filedialog.askdirectory()
			Button(root, text="Quit", command=root.destroy).pack()
			root.mainloop()
			filePath = os.path.join( folderSelected, fileName+'.json' )
	
			#Creating an empty file
			with open(filePath, 'w') as file:
				json.dump({}, file)

			print( "Successfully created the file +_+ !\n" )

		self.filePath = filePath  

	"""
		This Function checks whether
			=> Key's total characters is lesser or greater than 32 characters
			=> Key exist in the file or not
	"""
	def checkKey(self, key):
		
		#Checking the key's length
		if(len(key) > 32):
			print("Key length should be less than 32 characters\n")
			return 0

		#Checking whether the key exist already in the file or not
		if(self.checkKeyExist(key)):
			if(self.checkTimeToLive(key)):
				print("Key is already present\n")
				return 0
			else:
				return 1

		return 1	

	""" 
		This function checks whether the data can be added to the file or not
		(The file size should never exceed 1 GB) 
	"""
	def checkFileSize(self, dataSize):
        
		"""
			'os.path.getsize' gives file size in bytes
		    1 GB = 1024 *1024 *1024 bytes 
		"""
		if( ( os.path.getsize(self.filePath) + dataSize ) <= ( 1024 * 1024 * 1024 ) ):
			return 1
		return 0

	""" 
		This function checks whether the key exist in the file or not
	"""
	def checkKeyExist(self, key):
		with open(self.filePath, 'r') as file:
			data = json.load(file)

			if(key in data):
				return 1
		return 0

	""" 
		This function Checks whether the key is expired or not.
	"""
	def checkTimeToLive(self, key):
		with open(self.filePath, 'r') as file:
			data = json.load(file)

			if(data[key]["ttl"] == "null"):  #If the ttl has value 0, then it means it has no expiry time
				return 1
			else:
				expiryTime = datetime.strptime(data[key]["ttl"], '%Y-%m-%d %H:%M:%S.%f')
				if(datetime.now() > expiryTime):
					del data[key]
					json.dump(data, open(self.filePath, 'w'))
					return 0
		return 1			

	""" 
		This function is used to store data to the file by getting the required details
	"""
	def create(self, key, value, expiry = False, expiryTime = 10):
		
		#Checking the key is valid or not
		if(not self.checkKey(key)):
			return
		
		if(expiry == True):
			#Expiry time
			ttl = str( datetime.now() + timedelta(seconds = expiryTime) )
		else:
			ttl = "null"
		
		value["ttl"] = ttl

		#forming key value pair
		studentData = { key: value }

		#checking the student data size(should be lesser than 16kb) 
		if(sys.getsizeof(studentData) >= (16 * 1024)):
			print("The data size should be less than 16KB\n")
			return
		
		if( self.checkFileSize(sys.getsizeof(studentData)) ):

			#writing the data to the file
			with open(self.filePath, 'r+') as file:
				data = json.load(file)
				data.update(studentData)
				file.seek(0)
				json.dump(data, file)
				print("Data added successfully +_+ !\n")
		else:
			print("Cannot add data... The file size should never exceed 1GB\n")

	""" 
		This function is used to read data from the file
	"""
	def read(self, key):
		studentData = {}

		with open(self.filePath, 'r') as file:

			#Loading the data
			data = json.load(file)

			if(self.checkKeyExist(key)):
				if(self.checkTimeToLive(key)):
					for field, value in data[key].items():
						if(field != "ttl"):
							studentData[field] = value

					#Converting dictionary to json object
					json_object = json.dumps(studentData, indent = 4) 
					print("\n", json_object)		
					return
			print("Key is not present\n")
	
	""" 
		This function is used to delete data from the file	
	"""
	def delete(self, key):

		with open(self.filePath, 'r') as file:

			#loading the data
			data = json.load(file)

			if(self.checkKeyExist(key)):
				if(self.checkTimeToLive(key)):
					del data[key]
					json.dump(data, open(self.filePath, 'w'))
					print("Deleted successfully +_+ !\n")
					return
			print("Key is not present\n")

	def __del__(self):
		with open("user.log", 'w') as file:
			file.write("free")