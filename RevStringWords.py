def revStrWords(s):
    ch = s.split(' ')
    ch2 = []
    for i in range(len(ch) , 0, -1):
        ch2.append(ch[i-1])
    return " ".join(ch2[::])

s = input("Enter the string - ")
print(revStrWords(s))