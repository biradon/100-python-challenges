user_input = input()
user_array = list(map(int, user_input.split()))
R1 = user_array[0] - 1
C1 = user_array[1] - 1
R2 = user_array[2] - 1
C2 = user_array[3] - 1

chessboard = [[None] * 9 for _ in range(8)]
loop1 = True
loop2 = True
loop3 = True
loop4 = True
is_found = False

for i in range(0,8,1):
    for j in range(0,8,2):
        if i % 2 == 0:
            chessboard[i][j] = True
        else:
            j = j+1
            chessboard[i][j] = True
    for k in range(0,8,2):
        if i % 2 == 0:
            k= k+1
            chessboard[i][k] = False
        else:
            chessboard[i][k] = False
if R1 == C1 == R2 == C2:
    print("0")
else:
    if chessboard[R1][C1] == True and chessboard[R2][C2] == True or chessboard[R1][C1] == False and chessboard[R2][C2] == False:
        temp1 = R1
        temp2 = C1
        while loop1:
            if temp1 < 0 or temp2 < 0:
                loop1 = False
            temp1 = temp1 - 1
            temp2 = temp2 - 1
            if temp1 == R2 and temp2 == C2:
                print("1")
                loop1 = False
                is_found = True
        temp1 = R1
        temp2 = C1
        while loop2:
            if temp1 > 8 or temp2 > 8:
                loop2 = False
            temp1 = temp1 + 1
            temp2 = temp2 + 1
            if temp1 == R2 and temp2 == C2:
                print("1")
                loop2 = False
                is_found = True
        temp1 = R1
        temp2 = C1
        while loop3:
            if temp1 > 8 or temp2 < 0:
                loop3 = False
            temp1 = temp1 + 1
            temp2 = temp2 - 1
            if temp1 == R2 and temp2 == C2:
                print("1")
                loop3 = False
                is_found = True
        temp1 = R1
        temp2 = C1
        while loop4:
            if temp1 < 0 or temp2 > 8:
                loop4 = False
            temp1 = temp1 - 1
            temp2 = temp2 + 1
            if temp1 == R2 and temp2 == C2:
                print("1")
                loop4 = False
                is_found = True
        if is_found == False:
            print("2")
    else:
        print("-1")

        


