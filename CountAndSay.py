num = 1211
nextNum = ''
c=1
while num>0:
    l_dig = num%10
    num = num // 10
    second_l_dig = num% 10
    print(f"{l_dig} m {num}, {second_l_dig}")
    if l_dig == second_l_dig:
        print("in if")
        c += 1
        temp = f"{c}{l_dig}"
        if num < 9:
            nextNum = f"{c}{l_dig}" + nextNum
            break
    else:
        print("in else - ", nextNum)
        nextNum = f"{c}{l_dig}" + nextNum
        c=1
    print("Next num : ", nextNum)
print(nextNum)


def printNCountAndSay(n):
    num = 1
    for i in range(n):
        nextNum = ''
        c=1
        while num>0:
            
            l_dig = num%10
            num = num // 10
            second_l_dig = num% 10
            # print(f"{l_dig} m {num}, {second_l_dig}")
            if l_dig == second_l_dig:
                # print("in if")
                c += 1
                if num < 9:
                    nextNum = f"{c}{l_dig}" + nextNum
                    break
            else:
                nextNum = f"{c}{l_dig}" + nextNum
                c=1
            # print("Next num : ", nextNum)
        num = int(nextNum)
        print(nextNum)

printNCountAndSay(20)

# Working GRTTTTTTT