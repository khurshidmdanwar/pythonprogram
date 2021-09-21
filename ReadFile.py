#open the file.txt in read mode. Causes error if no such file exists.
fileptr = open("firstFile.txt","r")
#stores all the data of the file into the variable content
content = fileptr.read()
# prints the type of the data stored in the file
print(type(content))
#prints the content of the file
print(content)
#closes the opened file
fileptr.close()
