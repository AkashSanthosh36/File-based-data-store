
	#Importing required Packages
from tkinter import filedialog
import os
import json

	#Importing the required module for doing Create, read and delete operation
from process import Process

	#File option choosing (Create file and open file)
print( "\n\t\tWelcome +_+ \n\n\t 1. Create File \n\n\t 2. Open File" )
fileOption = int( input( "\nEnter your option: " ) )

if( fileOption == 1 ):
	fileName = input( "\nEnter the file Name: " ).strip()
	folderSelected = filedialog.askdirectory()
	filePath = os.path.join( folderSelected, fileName+'.json' )
	
		#Creating an empty file
	with open(filePath, 'w') as file:
		json.dump({}, file)

	print( "\nSuccessfully created the file +_+ !" )

elif( fileOption == 2 ):
	filePath = filedialog.askopenfilename()
	print( "\nFile Opened Successfully +_+ !" )	

print( "\nFile Path: ", filePath )

#initiating a class
p1 = Process( filePath )

while(1):
	print( "\n\t1. Create Data \n\t2. Read Data \n\t3. Delete Data" )
	choice = int( input( "\nEnter your option: " ) )

	if( choice == 1 ):
		p1.create()   #Create Data
	elif( choice == 2 ):
		p1.read()     #Read Data
	elif( choice == 3 ):
		p1.delete()	  #Delete data
	
	ch = input( "\nDo you want to continue (y/n): " )
	if( ch == 'n' ):
		break

