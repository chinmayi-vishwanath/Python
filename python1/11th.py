

'''
while condition:  ----  while condition true agovargu print true
  print(chinmayi)
'''

istrue=True
i=1

while istrue and i<=30:   
    print(i)
    i=i+1



num=1

while num<=140:
    print(num)
    num=num+1


    if(num>100):
        break
print("done")


# while inside the while

x=0
while x<4:
    i=0
    while i<x:
        print("chinmayi")
        i+=1
    x+=1


    # taking the input using the while

pin=1234
trail=1

while trail<4:
    input_pin= int(input(f" trail={trail}=>pin:"))
    trail+=1

    if input_pin==pin:
        print("correct")
        break
    else:
        print("incorrect")






