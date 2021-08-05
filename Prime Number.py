def isPrime(num) :
    p = 1

    for i in range(2, num - 1):
        if num % i == 0:
            p = 0
            break

    return p
number = int(input("enter a number :"))
ar = isPrime(number)

if ar == 1:
    print("Prime Number")
else:
    print("Not a prime Number")
