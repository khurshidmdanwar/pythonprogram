def my_pow(b, e):
    p = 1
    i = 0
    while i != e:
        p = p * b
        i = i + 1
    return p
    # print("Power=", p)

b = int(input("Enter Base :"))
e = int(input("Enter Exponent :"))
pow = my_pow(b,e) # Calling the Function
print("Power=", pow)
