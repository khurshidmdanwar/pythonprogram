def fileRead():
    f = open("abc.txt", "r")
    count = 0
    x = f.read()
    word = x.split()
    for w in word:
        if w=="Arif":
            count = count + 1
    print("Arif word occurs ", count+1, " times")
fileRead()