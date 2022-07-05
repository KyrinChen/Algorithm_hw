import numpy as np
while True:
    '''用于输入硬币种类和金额总数'''
    P = input("Input（输入数字，并用英文,分隔）: P = ").split(',')  # 将字符串沿空格切片为list
    isInt = True  # 用于判断list中是否都是int型
    for n in P:
        if not n.isdigit():
            isInt = False
            print("please input integer")
            break
    if isInt:
        P = list(map(int, P))  # 将字符串型的数字转为int型
        break
cnt = len(P)-1  # 矩阵数量
dp = np.zeros((cnt, cnt), dtype=int)
path = np.empty((cnt, cnt), dtype=int)
path.fill(-1)

# j = 1
for num in range(cnt):  # （矩阵数量1->cnt）整体上从左下到右上
    for row in range(cnt-num):  # 只考虑num数量矩阵相乘下，遍历所有可能性
        col = row+num  # dp[row][col]的意义是：从第row个矩阵连乘到第col个矩阵 的最小乘法次数
        ''' 执行顺序如下:
            dp[row][row+num] = j
            j = j+1
            [ 1.  5.  8. 10.]
            [ 0.  2.  6.  9.]
            [ 0.  0.  3.  7.]
            [ 0.  0.  0.  4.]
        '''
        # 30,35,15,5,10,20,25
        if row == col:
            dp[row][col] = 0
        else:
            tmp = [dp[row][mid]+dp[mid+1][col]+P[row]*P[mid+1]*P[col+1] for mid in range(row, col)]
            dp[row][col] = min(tmp)
            path[row][col] = tmp.index(dp[row][col]) + row
        # dp[row][col] = min([dp[row][mid]+dp[mid+1][col]+P[row]*P[mid+1]*P[col+1] for mid in range(row, col)])
# print(dp)
# print(path)


def add_bracket(left, right):
    if left == right:
        return
    bracket[left][0] = bracket[left][0] + 1
    bracket[right][1] = bracket[right][1] + 1

    if right-left >= 2:
        mid = path[left][right]
        add_bracket(left, mid)
        add_bracket(mid+1, right)


bracket = np.zeros((cnt, 2), int)
add_bracket(0, path[0][cnt-1])
add_bracket(path[0][cnt-1]+1, cnt-1)
print("Output:" + str(dp[0][cnt-1]))
for i in range(cnt):
    while bracket[i][0]:
        print("(", end='')
        bracket[i][0] = bracket[i][0]-1
    print(chr(i+65), end='')
    while bracket[i][1]:
        print(")", end='')
        bracket[i][1] = bracket[i][1]-1



