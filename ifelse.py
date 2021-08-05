cost = int(input("Enter Cost Price :"))
sale = int(input("Enter Cost Price :"))
if(sale>cost):
    p = sale - cost
    print("Profit=", p)
else:
    l = cost - sale
    print("Loss=", l)