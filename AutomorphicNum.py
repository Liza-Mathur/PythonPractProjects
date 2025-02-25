def is_automorphic(n):
    return str(n ** 2).endswith(str(n))

print(is_automorphic(25))  # It is
print(is_automorphic(76))  # It is
print(is_automorphic(12))  # Its not
