def createFile():
    f = open("abc.txt", "r")
    f1 = open("cap2S.txt", "w")
    ch = f.read()
    for i in ch:
        if i.isupper():
            i = i.lower()
        elif i.islower():
            i = i.upper()
        f1.write(i)
    f.close()
    f1.close()
createFile()