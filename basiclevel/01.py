 #simple calculator

number1=int(input("Enter the number: "))
operation=input("Entre the operator(+,-,*,/):")
number2=int(input("Enter the number2: "))

# print(f"{number1} {operation} {number2}")


def calculation(a,b,op):
    if op=='+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '*':
        return a*b
    elif op == '/':
        if b!=0:
            return a/b
        else:
            return 'error'
    else:
        return 'invalid operation'

result=calculation(number1,number2,operation)
print(result)
    