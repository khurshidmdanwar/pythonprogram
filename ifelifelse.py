phy = int(input("Enter Physics Number --->"))
chem = int(input("Enter Chemistry Number --->"))
math = int(input("Enter Mathematics Number --->"))
avg = (phy+chem+math)/3
if avg>=60:
    print("First Divison")
elif avg>=50 and avg<60:
    print("Second divison")
elif avg>=40 and avg<50:
    print("Third Division")
else:
    print("Fail")