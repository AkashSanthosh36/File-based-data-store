
#Importing the required packages
import json
import os
import sys
from datetime import datetime, timedelta 


""" 
	Class for doing Create, Read, Delete operation on the file
"""
class Process: 
	def __init__(self, filePath):
		self.filePath = filePath  

	"""
		This Function checks whether
			=> Key's total characters is lesser or greater than 32 characters
			=> Key exist in the file or not
	"""
	def checkKey(self, key):
		
		#Checking the key's length
		if(len(key) > 32):
			print("\nKey length should be less than 32 characters")
			return 0

		#Checking whether the key exist already in the file or not
		if(self.checkKeyExist(key)):
			if(self.checkTimeToLive(key)):
				print("Key is already present")
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

			if(data[key]["ttl"] == "0"):  #If the ttl has value 0, then it means it has no expiry time
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
	def create(self):

		while(1):
			while(1):
				key = input("\nKey: ").strip()
				
				#Checking the key is valid or not
				if(self.checkKey(key)):
					break

			#Getting data
			studentName = input("\nStudent Name: ").strip()
			email = input("\nEmail: ").strip()
			rollNumber = int(input("\nRoll Number: "))
			classNumber = int(input("\nClass: "))

			choice = input("\nDo you want to give an expiry time for this data (y/n)").strip()
			if(choice == 'y'):
				liveTime = int(input("\nSecond for which data should be available: "))
				
				#Expiry time
				ttl = str( datetime.now() + timedelta(seconds = liveTime) )
			else:
				ttl = "0"
			
			#forming data in the required form
			studentData = { key: {"studentName": studentName, "email": email, "rollNumber": rollNumber, "class": classNumber, "ttl": ttl} }

			#checking the student data size(should be lesser than 16kb) 
			if(sys.getsizeof(studentData) <= (16 * 1024)):
				break

		if( self.checkFileSize(sys.getsizeof(studentData)) ):

			#writing the data to the file
			with open(self.filePath, 'r+') as file:
				data = json.load(file)
				data.update(studentData)
				file.seek(0)
				json.dump(data, file)
				print("\nData added successfully +_+ !")
		else:
			print("\nCannot add data... The file size should never exceed 1GB")

	""" 
		This function is used to read data from the file
	"""
	def read(self):
		key = input("\nKey: ").strip()

		studentData = {}

		with open(self.filePath, 'r') as file:

			#Loading the data
			data = json.load(file)

			if(self.checkKeyExist(key)):
				if(self.checkTimeToLive(key)):
					print("\nValue to the corresponding key: ")
					for field, value in data[key].items():
						if(field != "ttl"):
							studentData[field] = value

					#Converting dictionary to json object
					json_object = json.dumps(studentData, indent = 4) 
					print("\n", json_object)		
					return
			print("\nKey is not present")
	
	""" 
		This function is used to delete data from the file	
	"""
	def delete(self):
		key = input("\nKey: ").strip()

		with open(self.filePath, 'r') as file:

			#loading the data
			data = json.load(file)

			if(self.checkKeyExist(key)):
				if(self.checkTimeToLive(key)):
					del data[key]
					json.dump(data, open(self.filePath, 'w'))
					print("\nDeleted successfully +_+ !")
					return
			print("\nKey is not present")