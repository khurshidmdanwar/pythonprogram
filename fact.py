def factorial():
    b=int(input('enter a number:'))
    x=1
    for i in range(1, b+1):
            x=x*i
    return x
    
a=factorial()
print(a)