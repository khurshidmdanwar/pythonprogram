def simpleInterest(pri, rate, ti):
    p = pri
    r = rate
    t = ti
    si = (p * t * r) / 100
    return si
# Input the value
pr = int(input("Enter Principal :"))
rt = float(input("Enter Rate :"))
time = int(input("Enter Time :"))
# calling the function with return
s=simpleInterest(pr, rt, time)
# Print the Simple Interest
print("Simple Interest", s)
