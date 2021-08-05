# Python program to find G. C. D of two numbers
# define a function
def compute_gcd(x, y):

# choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf
num1 = int(input("Enter a number :"))
num2 = int(input("Enter a number :"))

print("The H.C.F. is", compute_gcd(num1, num2))