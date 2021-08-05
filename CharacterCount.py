def char_count():
    f = open("abc.txt", "r")
    count = 0
    ch = f.read()
    for n in ch:
        count = count + 1
    print("Total Characters=",count)
    f.close()
char_count()