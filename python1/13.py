# list and dictnories for loop.list compreension,dictnory comprehension


# sum through for loop

list=[23,34,45,56,67]
row=0

for num in list:
    row=row+num
    print(row)

# dobule the number

list=[23,34,45,56,67]
dl=[]

for number in list:
    dl.append(number*2)
    print(dl)

# dictnories

dic={"name":"chinmayi","age":20,"status":"single"}

for it in dic.values():
    print(it)

dictnories={"name":"chimmu","age":30,"status":"single"}
for keyvalue in dictnories.keys():
    print(keyvalue)

dictnory={"name":"kruthartha","age":40,"status":"single"}
for keyvalues in dictnories.items():
    print(keyvalues)


# we have seperate key and the value  how can i merge both
student=["chinmayi","chimmu","chinni"]
marks=[100,101,102]
student_marks={}

for index,dic in enumerate(student):
    student_marks[dic]=marks[index]

print(student_marks)

# we have anoother method for this
employe=["saheb","sahali","sahuva"]
marks=[102,103,104]
employe_marks={}

for i in range(3):
    employe_marks[employe[i]]=marks[i]

print(employe_marks)


# if we dont know the length of te employee
employ=["haha","hehe","huhu"]
marks=[100,101,103]

employ_marks={}

for i in range(len(employ)):
    employ_marks[employ[i]]=marks[i]
print(employ_marks)


# list comprehension
