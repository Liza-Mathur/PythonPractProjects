def diamondPatter(n=5):
    for i in range(1, n+1):
        print(' ' * (n-i), end=" ")
        print(i, end="")
        for j in range(1 , i+1):
            # print(i)
            # print(j)
            if i == 1:
                # print("i", i)
                # print("j", j)
                continue
            elif j==i:
                # print("elif j==i")
                print(j , end="")
            else:
                # print("else")
                print(' ', end=" ")
        print()
    
    for i in range(n-1 , 0 , -1): # 4 3 2 1
        print(' ' * (n-i) , end = " ")
        print(i , end="")
        for j in range(i , 0 , -1): # 4 3 2 1 on first loop
            if i == 1:
                continue
            elif j == 1:
                print(i , end="")
            else :
                print(' ', end=' ')

        print()

diamondPatter(5)




# _____1
# ____2_2
# ___3__ 3
# __4_____4
# 5________5
