# functions

# function is a reuseable block of code performs  specific task when caled , 
# functions are usefull to organize code make it reuseable and reduce redundency(repeat)

def greet():  #defining the greet() function
    print(f"i am chimayi")
greet()
greet()

def marriage(boy,girl):
    print(f"{boy} is marrying {girl}")
marriage("chandhan", "chandini")
marriage("raju","rani")  # positiona argument


def marriage(boy,girl):
    print(f"{boy} brother of {girl}")
marriage( boy="ranjan" ,girl="chinamyi")  # keyword argument


def tables(num):
    for i in range(1,11):
        print(f"{num}*{i}={num*i}")
tables(2)
tables(5)
tables(7)
tables(9)
tables(10)

# default parameter
def default(boy="parik",girl="chimmu"):
    print(f"{boy} is brother of {girl}")
default("raja","rani")  # if we pass the arguments then we will get .
default() # it takes the default value like parik and the chimmu





