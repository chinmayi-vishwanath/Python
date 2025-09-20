print("*")


# i=5
# for i in range(1,i+1):
#     print("*",i)


# traingle pattern
for i in range(6):
    print("*"*i)

# inverted traingle pattern
for i in range(5,1,-1):
   print("*"*i)


# 5*5 pattern
for i in range(5):
    print("*"*5)


for i in range(5):
    for i in range(5):
        print(i*'*')
        print(i*'*')

for i in range(6):
    print(i*'*')
    for i in range(2):
        print(i*'*')