# input/output ,comments

#  output

a=10
print(a) # output

# input

Name=input("name= ")

boyname=input("boyname= ")
girlname=input("girlname= ")

print(boyname + " friend " + girlname)  #concation 
print(f"{boyname} friend {girlname}") #formated string


# age difference between boy and the gir

boy_age=int(input("boyage= "))
girl_age=int(input("girlage= "))

diff=abs(boy_age-girl_age) #absolute value

print(boyname+ " fiend "+ girlname + str(diff))
print(f"{boyname} friend {girlname} and age {diff}" )
# print(f"{boy_age} is greater than {girl_age}")


# hw
a=input("name: ")
b=input("age: ")

print(f"hello {a} you are {b} years")