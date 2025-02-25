def is_armstrong(num):
    power = len(str(num))
    return num == sum(int(digit) ** power for digit in str(num))

def armstrong_numbers_in_range(start, end):
    return [num for num in range(start, end + 1) if is_armstrong(num) and num>9]

print(armstrong_numbers_in_range(1, 500))  
#[153, 370, 371, 407]
