def getPrimes(m):
    primes = []
    for i in range(2,m+1):
        flag = True
        print("i , ", i)
        for j in range(2, i):
            if i%j == 0:
                flag = False
        if flag:
            primes.append(i)
    return primes
            

def isHamming(n):
    primes = getPrimes(n)
    for i in primes:
        if n%i == 0 and i not in [2,3,5]:
            return False
    return True
# Added 2,3 and 5 as in Hamming we consider only 2,3 and 5
print(isHamming(90))