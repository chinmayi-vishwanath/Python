# Multiplication table generator
def num(a):
    for i in range(1,11):
        print(f"{a}*{i}={a*i}")
num(2)
num(3)

# or

numb=int(input("Enter the number: "))
for i in range(1,11):
    print(f"{numb}*{i}={numb*i}")