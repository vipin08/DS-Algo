def MatrixSpning(array, max_r, max_c):
    current_row, current_col = 0,0
    while(current_row < max_r and current_col < max_c):
        for i in range(current_row, max_c):
            print(array[current_row][i], end=" ")
        current_row +=1
        for i in range(current_row, max_r):
            print(array[i][max_c-1], end=" ")
        # break

        max_c -= 1
        print("\n")
        print(current_col,max_c)
        for i in range(current_col,max_c):
            print(i, current_col)
        break



array = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

max_cLength = len(array[0])
max_rLength = len(array)
# print( max_rLength, max_cLength)
MatrixSpning(array, max_rLength,max_cLength)
