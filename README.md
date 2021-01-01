# File-based-data-store

About the project:

        A file based key-value data store which supports Create, Read and Delete operations.

Built With:

        Python 3

Steps to use the library:

=> Clone the repository
        
        git clone https://github.com/AkashSanthosh36/File-based-data-store.git
  
 => Open command line in the program folder
 
 =>Enter 'python' to get into python interactive mode
 
 =>Import the library
 
        from dataprocess import DataProcess
 
 =>Initiate the library
        
        t = DataProcess(fileName = "akash", fileAlreadyCreated = False)
  
 =>Commands for CRD operations
 
        =>Create data with expiry time:    t.create(key = "1", value = {"studentName": "Akash", "email": "akashsan362000@gmail.com"}, expiry = True, expiryTime = 10)
        
        =>Create data without expiry time: t.create(key = "1", value = {"studentName": "Akash", "email": "akashsan362000@gmail.com"}, expiry = False)
        
        =>Read:                            t.read(key = "1")
        
        =>Delete                           t.delete(key = "1")
        
Executing testing.py (unit testing)

        =>python testing.py

Files Used:

        =>dataprocess.py   =>   for create, read, delete operations
        
        =>testing.py       =>   unit testing
        
        =>user.log         =>    It is used to log the file status (free or occupied).  It is used to make sure that only one client uses the datastore at any given time
        
Special characteristics of my project:

        =>Gui has been made where one can select the folder to store the file
        
        =>Only one client can process at a time
  
        =>No third party libraries is used
  
        =>The project is easy to use
  
        =>Satisfied all the points given in the project description
  
        =>The code is effectively written with a well documented comments
  
        =>It is supported in all OS
