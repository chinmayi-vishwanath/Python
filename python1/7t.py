# tuple:it is a collection of items  ,but it is immutable means unchangeable

tuple=(1,2,3,4)
print(tuple)


fruits=("apple",)
print(fruits)

# we cannot pop or insert

# 2. acessing, sclicing

#3 operations: repetation,concatination we can do then membership operator
name=("chinmayi","chimm","mayii","chinmayiii")
name2=("riya","ramya","raju","rajeshwari")
print(name+name2)

print(name2*2)

print("chimm" in name)

#methods:count index
print(name.count("chimu")) 
print(name2.index("ramya"))
