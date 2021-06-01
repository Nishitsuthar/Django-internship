n1 = int(input("Enter first value : "))
n2 = int(input("Enter second value : "))
n3 = int(input("Enter third value : "))

if n1 <= n2 and n1 <= n3:
    print(n1, " is the smallest")
elif n2 <= n1 and n2 <= n3:
    print(n2, " is the smallest")
else:
    print(n3, " is the smallest")
