def dup_copy():
    f = open("abc.txt", "r")
    f1 = open("xyz.txt", "w")
    ch=f.read()
    f1.write(ch)
    f.close()
    f1.close()
dup_copy()