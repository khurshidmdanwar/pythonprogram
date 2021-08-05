n=50
f1=0
f2=1
fib=0
print(fib, end=' ')
for i in range(1, n+1):
    f1=f2
    f2=fib
    fib=f1+f2
    print(fib, end=' ')