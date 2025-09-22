# palindrome

word=input("Enter the palindrome: ")

if word==word[::-1]:
    print(f"{word} is palindrome")
else:
    print(f"{word} is not palindrome")


    # or

def palindrome(pal):
    s=str(pal)
    return s==s[::-1]
    
print(palindrome("hello"))


