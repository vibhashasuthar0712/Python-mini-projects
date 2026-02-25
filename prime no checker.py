#mini project- Prime number checker

def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

num=int(input("enter a num:"))
if is_prime(num):
    print("it's a prime number")
else:
    print("not a prime number")
