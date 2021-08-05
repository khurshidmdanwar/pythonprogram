a = int(input("Enter First Angle of Triangle"))
b = int(input("Enter Second Angle of Triangle"))
c = int(input("Enter Third Angle of Triangle"))
if a + b + c == 180:
    print("Triangle is possible")
    if a < 90 and b < 90 and c < 90:
        print("Acute angle triangle")
    elif a == 90 or b == 90 or c == 90:
        print('Right angle triangle')
    else:
        print("Obtuse angle triangle")
else:
    print("Triangle is not possible")