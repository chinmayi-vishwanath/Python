# sets: collection of unique items,unorderd,unindex,

sets={1,2,30,4,5}
print(sets)
# print(sets[2]) unindex


# sets operations
set1={1,2,3,45,44}
set2={34,1,3,2,45}
print(set1|set2)    #union  --- 1,2,3, 45,44,34,1,3,2,45
print(set1&set2)   #intersection  ----- 1 2 3 45
print(set1-set2)  #difference   -----  44
print(set1^set2) #symetric   44  34


#set methods --->add, remove,discard,pop,clear

print(set1.pop())
