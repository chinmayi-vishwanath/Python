# if elif else

name="chinmayi"

if name =="chinmayi":
    print("happy")
else:
    print("sad")

# 2
place="valalahalli"

if place=="mysore":
    print("chamundibetta")
elif place=="banglore":
    print("silicon city")
else :
    print("malnad")

# 3
place=input("just type the places: ")


if place=="valalahalli":
    print("malnad")
elif place =="mysore":
    print("chamundibetta")
elif place =="banglre":
    print("silicon")
else:
    print("not found")

# 4---->nested

bottle_c="red"
bottle="water"

if bottle_c=="red" or bottle_c=="blue":
    if bottle=="water":
        print("there is water")
    else :
        print("no water")
else:
    print("the color is red")

