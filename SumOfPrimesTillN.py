def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    # print(n)
    return True

def sum_of_primes_below(n):
    return sum(num for num in range(2, n) if is_prime(num))

print(sum_of_primes_below(100))  
