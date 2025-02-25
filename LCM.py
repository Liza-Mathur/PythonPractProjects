def gcd(a, b):
    while b:
        a, b = b, a % b  
    return a

def find_lcm(a, b):
    return abs(a * b) // gcd(a, b)

i = int(input("Give first number : "))
j = int(input("Give second number : "))
print("LCM of {i} and {j} is:", find_lcm(i, j))  

