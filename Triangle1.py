a = int(input("Enter a angle --->"))
b = int(input("Enter b angle --->"))
c = int(input("Enter c angle --->"))
tot = a + b + c
if tot==180:
    print("Triangle is Possible")
    if a<90 and b<90 and c<90:
        print("Acute angle triangle")
    elif a==90 or b==90 or c==90:
        print("Right angle triangle")
    elif a>90 or b>90 or c>90:
        print("Obtuse angle triangle")
else:
    print("Triangle is not possible")