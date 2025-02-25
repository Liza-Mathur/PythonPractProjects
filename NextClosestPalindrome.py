def is_palindrome(n):
    return str(n) == str(n)[::-1]

def next_palindrome(n):
    while True:
        n += 1
        if is_palindrome(n):
            return n

print(next_palindrome(123))  
