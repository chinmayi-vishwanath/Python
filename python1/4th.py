# string manippulation

'''
1. string operations
   *concatination
   *repetation
 '''


# concatination

fname="chinmayi"
lname="Gowda"

fullnam=fname+ " " +lname
print(fullnam)

# repetation

fname="chinamyi "*10
print(fname)  #or print(fname*100)

'''
string methods:
  1.upper()
  2.lower()
  3.stripe()
  4.replace(old,new)  
'''


name="gowdru "
print(name.upper())
print(name.lower())
print(name.strip()*10)   #no space
print(name.replace("gowdru","gowdas"))

# Acessing the string character

print(name[0])  #by taking the index value and printing the chacter

# You can also use negative indexing to start counting from the end of the string.

print(name[-2])

# slice

print(name[1:6])
print(name[:6])
print(name[0:])
print(name[2:5])


# another method like after one letter skipp  [start:end:skip]
print(name[::2])



# who we want like that we can write
names="""how we acn rightthat we can write
 the sentence in which linw we want that line
"""
print( names)


# escape sequences
sentence="i am chinmayi ,\n  pursuing BE"
print(sentence)
sentence_tab="i anm chinamyi \t pursing be"
print(sentence_tab)





