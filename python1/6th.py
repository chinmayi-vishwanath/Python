# list:collection of items
'''item1=["shoe"]
item2=["sokes"]
item3=["pant"]'''


items=["shoe","sokes","shirt","pant"]

#1. modifing the list--->

     # a chinging th eelement 
items[0]="shoe2"
print(items)

    # b  adding  the element
print(items.append("key"))
print(items.insert(1,"pant2"))
      
    # c  removing the element
print(items.pop(1))
print(items.remove("shirt"))
# print(items.clear())
print(items)




#3. slicing the list [start:stop:step]
names=["chinmayi","chimmu","ranjan","parikshith","riya"]
print(names[0:5:1])


#4. common function--lrngth,sorted

print(len(names))

# sorted
num=[1,2,6,5,4,3]
print(sorted(num))

# sum-list
print(sum(num))

# 5. methods:index(),count(),reverse,sort

fruits=["apple","mango","strawberry"]
numbers=[12,23,34,45]
print(fruits.count("apple"))
print(fruits.index("apple"))
print(numbers.reverse())
print(numbers)
print(numbers.sort())
print(numbers)