# for loop

# for loop is nothing but te iteration of the sequence(list,tuples range,string)

'''
for items in sequence

example: 
   cites=[banglore,manglore]

   for city in sequence
   '''


'''
difference between  for and the while loops are 

in the while we dont know how much  iteration it takes---  we dont know how much salt for 100gram soup
but in the for it takes knows the exact iteration - example 10gram slat-100soup


'''

i=1

for i in range(1,10):
    print(i)

    # same example if we took in the while ... there we have to check the condition - texecute-- incremnt takes //long process


# if we want to print every number on the one line
num=1
for num in range(1,10):
    print(num, end=" ")


cites=["banglore","belur","manglore"]
for city in cites:
    print(city, end=" ")

number=0
for number in range(1,11,3):
    print(number)

    # we use the enumarate to come  what is there  and the index

list111=["cat","dog","elephant"]
for index,animals in enumerate(list111):
    print(f"{animals} and the index {index}")


name="chinmayi"
for index,letters in enumerate(name):
    print(letters*(index+1))


# we can convert dictnories to the tuples

dict={"name":"Chinmayi","age":3, "status":"single"}
print(dict)
for  key,value in dict.items():
    print(key, " ",value)

    # nested loops


# for i in range(1,11):
#    print(f"2*{i}={2*i}")


for j in range(2,11):
    for k in range(1,11):
        # print(i)
        print(f"{j}*{k}={j*k}")