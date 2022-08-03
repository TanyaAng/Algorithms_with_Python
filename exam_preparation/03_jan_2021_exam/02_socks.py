from collections import deque

def print_matrix(matrix):
    for row in matrix:
        print(row)


left_socks = [int(x) for x in input().split()]
right_socks = [int(x) for x in input().split()]

rows=len(left_socks)+1
cols=len(right_socks)+1

dp=[]
[dp.append([0]*cols) for _ in range(rows)]

for row in range(1,rows):
    for col in range(1,cols):
        if left_socks[row-1]==right_socks[col-1]:
            dp[row][col]=dp[row-1][col-1]+1
        else:
            dp[row][col]=max(dp[row-1][col], dp[row][col-1])

print(dp[rows-1][cols-1])

# row = rows - 1
# col = cols - 1
# result = deque()
# while row > 0 and col > 0:
#     if left_socks[row - 1] == right_socks[col - 1]:
#         result.appendleft(left_socks[row - 1])
#         row -= 1
#         col -= 1
#     elif dp[row - 1][col] > dp[row][col - 1]:
#         row -= 1
#     else:
#         col-=1
#
# print(*result,sep=' ')