# prime number

def prime_number(num):
    if num<=1:
        return False
    for i in range(2,int(num**0.5)+1):  #[2,4]  #num=9    // we check i=2 i=3
            if num % i==0:
                return False
    return True
print(prime_number(12))
