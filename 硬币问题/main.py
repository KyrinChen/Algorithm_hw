import os

while True:
    '''用于输入硬币种类和金额总数'''
    coins = input("Input: coin(用空格分隔，用回车结束输入) = ").split()  # 将字符串沿空格切片为list
    amount = input('Input: amount = ')
    isInt = True  # 用于判断list中是否都是int型
    for n in coins:
        if not n.isdigit():
            isInt = False
            print("please input integer")
            break
    if isInt:
        amount = int(amount)
        coins = list(map(int, coins))  # 将字符串型的数字转为int型
        coins.append(0)
        coins.sort()  # 从小到大排序
        break

# num数组从0到amount，记录每个金额下，需要的最少硬币数
num = [float('inf')] * (amount + 1)  # 初始为无穷大，表示无法组成此金额，利于比较和迭代
num[0] = 0  # 价值为0由0组成
# re_dp数组记录组成当前金额加入的最后一个硬币值。 表示反向求出reverse dynamic programming
re_dp = [-1]*(amount+1)  # 初始为-1，表示无法组成此金额
re_dp[0] = 0  # 价值为0由0组成

for index in range(amount+1):  # 金额为index，从0-amount动态规划
    for coin in coins:  # 试探加入哪种面值的硬币组成此金额（index）数量更少
        if coin <= index and num[index - coin]+1 < num[index]:  # 若要加入coin面值的硬币，数量就是【（当前面值-coin）所需最少硬币数+1】
            '''举例说明：coins=[2,3,5]，amount=11，金额从0到6所需的最少硬币递推如下
                d(0)=0;
                d(1)=inf(无穷大);
                d(2)=d(2-2)+1=1;
                d(3)=min{d(3-2)+1,d(3-3)+1}=1;
                d(4)=min{d(4-2)+1,d(4-3)+1}=2;
                d(5)=min{d(5-2)+1,d(5-3)+1,d(5-5)+1}=1;
                d(6)=min{d(6-2)+1,d(6-3)+1,d(6-5)+1}=2;
                ......'''
            num[index] = num[index - coin] + 1
            re_dp[index] = coin  # re_dp数组记录组成当前金额加入的最后一个硬币值
i = amount
if re_dp[amount] == -1:
    print("Output: -1")
else:
    print("Output: %s coins" % num[amount])
    print("Explanation: ", end="")
    while i > re_dp[i] > 0:
        print("%s+" % re_dp[i], end="")
        i -= re_dp[i]
    print(re_dp[i])

os.system("pause")
