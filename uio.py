import math
for x in range(3,math.ceil(75**(1/2)),2):
    print(x)
def prime_numbers(n):
    if n<2:
        return False
    if n%2==0:
        return False
    for x in range(3,math.ceil(75**(1/2)),2):
        if n%x==0:
            return False
    return n