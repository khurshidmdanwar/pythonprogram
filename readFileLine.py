fileptr = open("firstFile.txt","r")
print("The filepointer is at byte :",fileptr.tell())
content = fileptr.readlines()
#prints the content of the file
print(content)
print("The filepointer is at byte :",fileptr.tell())

fileptr.seek(7);
cont1=fileptr.readline()
print(cont1)
print("The filepointer is at byte :",fileptr.tell())
#closes the opened file
fileptr.close()
