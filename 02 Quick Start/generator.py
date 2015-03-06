def isprime(n):
    if n == 1 :
        return False
    for x in range(2,n):
        if n % x == 0 :
            return False
    else :
        return True

def primes(n = 1) :
    while(True):
        if isprime(n) : yield n
        n = n + 1
        
for n in primes():
    print(n)
    if n > 100 : break