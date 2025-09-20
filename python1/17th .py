# advance topics of the python 

# returning the values or the outut

def function(num):
    return (num*5)

a=100
b=function(1)
c=a+b
print(c)

# local variable global variable
def fuc():
    local=100
    print(local)
    # print(g)  it is error because  first function calls and then execute then g gets stored and then get printed
     
fuc()
# print(local)  ---- the error it is not defined outside local variable 

g=300
print(g)



#advance topics
def advancefunction (*numbers):
    print(numbers)
advancefunction(1,2,3,4,5,6,7,8,9,0)


# advanced topics--variable length argument
def advance(*numbers):
    print(numbers)
    return sum(numbers)

advance(1,2,3,4,5)

c=advance(1,2)
print(c)


# keywords argument
def function1(**kwargs):
    # print(kwargs)

    for key,value in kwargs.items():
        print(f"{key}:{value}")
function1(name="chinmayi", age=8)

    


