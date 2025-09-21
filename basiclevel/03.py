# largest of three numbers

# 1st metod
a =int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the third number: "))

print("The largest number", max(a,b,c))


# 2nd method 
a1=int(input("Enter the first number: "))
b1=int(input("Enter  the second number: "))
c1=int(input("Enter the third number: "))

if a1>b1 and a1>c1:
    print("a is the largest number")
elif b1>a1 and b1>c1:
    print("b is the largest number")
else:
    print("c is the largest number")
    