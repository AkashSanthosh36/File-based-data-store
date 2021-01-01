
#Importing the required packages
from dataprocess import DataProcess
import time
import json

#initating a class
t = DataProcess("testData", fileAlreadyCreated = False)

#Creating data with expiry time
jsonData1 = { "1": { "studentName": "Akash", "email": "akashsan362000@gmail.com" } }
print("\nStoring data with 10 seconds expiry time\n", json.dumps(jsonData1, indent = 4))
t.create(key = "1", value = jsonData1, expiry = True, expiryTime = 10 )

#Creating data without expiry time
jsonData2 = { "2": { "studentName": "Vignesh", "email": "vignesh@gmail.com" } }
print("\nStoring data without expiry time\n", json.dumps(jsonData2, indent = 4))
t.create(key = "2", value = jsonData2, expiry = False)

#Creating a new entry with duplicate key(key = 1)
jsonData3 = { "1": { "studentName": "Varsha", "email": "varsha@gmail.com" } }
print("\nCreating a new entry with duplicate key")
t.create(key ="1", value = jsonData3, expiry = False)

print("\nSleep for 12 seconds")
time.sleep(12)

print("\nReading data after 12 seconds")

#Reading data which has expiry time
print("\nReading data which has key = 1(has expiry time of 12 seconds)")
t.read("1")

#Reading data which has no expiry time
print("\nReading data which has key = 2(has no expiry time)")
t.read("2")

print("\nDeleting data")

#Deleting data which has expiry time
print("\nDeleting data which has key = 1")
t.delete("1")

#Deleting data which has no expiry time
print("\nDeleting data which has key = 2")
t.delete("2")

