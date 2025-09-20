# dictonary:is a collection of key value pairs


dictniory={
    "word":"meaning",
    "chinmayi":"happy",
    "name":"name"

}

print(dictniory)
print(dictniory["name"])

# if it is not there then also  i can print not found or else crash
print(dictniory.get("sudeep","notfound"))


# i can  add  in the run time

dictniory["chinmayivv"]="chimmu"
print(dictniory)

#removing the elements from the dictniory
# del,pop,clear

del dictniory["name"]
print(dictniory)

x=dictniory.pop("chinmayi")
print(x)

print(dictniory)

# dictniory methods
# keys,values,items,update

print(dictniory.values())
print(dictniory.keys())
print(dictniory.items())

# mixing of two dictonary

name1={
    "raju":"ranii",
    "rayaa":"rayan",
}


print(dictniory.update(name1))
print(dictniory)