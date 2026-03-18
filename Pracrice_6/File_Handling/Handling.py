f = open("demofile.txt")



f = open("demofile.txt", "rt") #read text
f = open("demofile.txt", "r") #read text
f = open("demofile.txt", "rb") #read binary
f = open("demofile.txt", "w") #`write text
f = open("demofile.txt", "wb") #write binary
f = open("demofile.txt", "a") #append text to the end of the file
f = open("demofile.txt", "x") #create a file if it does not exist
f = open("demofile.txt", "w+") #open a file for both writing and reading. Overwrite the existing file if the file exists. If the file does not exist, create a new file for reading and writing.
f = open("demofile.txt", "a+") #open a file for both appending and reading. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for reading and writing.
