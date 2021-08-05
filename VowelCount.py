def vowel_count():
    f = open("abc.txt", "r")
    count = 0
    ch = f.read()
    for n in ch:
        if n in 'AEIOUaeiou':
            count = count + 1
    print("Total Vowels=" , count)
    f.close()
vowel_count()