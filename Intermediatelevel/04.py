# fabonacci --- means first two numbers are 0 and 1
# each number after that is sum of previous 2 numbers

# eg:10--> 0,1,1,2,3,5,8,13,21,34


def fibonacci(n):
    a,b=0,1
    for i in range(n):
        print(a,end=" ")
        a,b=b,a+b

fibonacci(10)