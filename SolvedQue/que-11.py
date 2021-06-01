number = float(input("Please Enter any number : "))

if number > 0:
    print("{0} is a positive number".format(number))
elif number == 0:
    print("{0} is zero".format(number))
else:
    print("{0} is a negative number".format(number))
