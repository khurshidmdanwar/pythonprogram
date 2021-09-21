fileptr = open("python.txt","r");
cont1=fileptr.readline(12)
print("The filepointer is at byte :",fileptr.tell())
#closes the opened file
