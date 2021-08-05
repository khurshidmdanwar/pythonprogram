n = int(input("Enter a number:"))
f = 1  # Flag variable
for i in range(2, n):
    if n % i ==0:
        f = 0
        break
if f==1:
    print("Prime number is ", n)
else:
    print("Not a Prime number")
