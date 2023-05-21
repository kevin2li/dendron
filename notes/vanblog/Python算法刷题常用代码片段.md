# 读取数据
```python
# 输入：3 4 5
a, b, c = list(map(int, input().split()))
```

# 特殊数值
```python
# 无穷大
float('inf')
```
<!-- more -->

# 数组
- 声明
```python
# 声明一维数组
dp = [0 for i in range(n)]
dp = [0]*n

# 声明二维数组
vis = [[False for j in range(n)] for i in range(m)]

# 获取二维数组长宽
m, n = len(board), len(board[0])
```

- 判断数组元素位于其他对象中
```python
# 判断数组中模式是否位于字符串s中
s = "20220123"
any([k in s for k in ['012', '123', '234', '345', '456', '567', '678', '789']])
```

- 排序/逆序
```python
l = [1, 2, 5, 3, 4]
# 排序
l.sort()      # [1,2,3,4,5]
l = sorted(l) # [1,2,3,4,5]

# 逆序
l.reverse() # [4,3,5,2,1]
l = list(reversed(l)] # [4,3,5,2,1]
```
- 复制列表
```python
nums = [1,2,3]
nums[:]
# or
nums.copy()
```
- 平移n个单位
```python
l = [1,2,3,4,5,6,7,8]
n = 3
# 左移
l = l[n:]+l[:n] # [4,5,6,7,8,1,2,3]
# 右移
l = l[-n:]+l[:-n] # [6,7,8,1,2,3,4,5]
```

# 链表
- 链表反转
```python

```

- 环形链表
```python

```

# 栈
- 基础操作
```python
```
- 单调栈

```python
```
- 用栈实现队列
```python
```

# 队列
- 基础操作
```python
```
- 单调队列
```python
```

# 字符串处理
- 基本操作
```python
s = "123ABC"
str_array = ['a', 'b', 'c']
s2 = "hello world"

# 逆序
s[::-1]

# 排序
sorted(s)

# 分割字符串
s2.split()

# 拼接字符串数组
"".join(str_array)

# 判断是否为字母
'abc123'.isalpha() # False

# 判断是否为数字串
'abc123'.isdigit()

# 大小写转换
'a'.upper() # 'A'
chr(ord('a')-32) # 'A'

# 字符串转整数
int("101", 2) # 5
```

- 下一个字典序
```python

```

# 日期/时间
- 遍历日期
```python
import datetime
begin = datetime.datetime(2022,1,1)
end = datetime.datetime(2023,1,1)
for i in range((end-begin).days):
    day = begin + datetime.timedelta(days=i)
    print(day)
```

# 数学
- 基础运算
```python
# 乘方
10**2 # 100

# 开方
math.sqrt(4) # 2.0
4**0.5       # 2.0

# 上取整
math.ceil(3.7) # 4.0
math.ceil(4)   # 4.0

# 下取整
math.floor(3.7) # 3.0
math.floor(3)   # 3.0

# 四舍五入
round(3.14159)    # 3
round(3.14159, 3) # 3.142

# 取模
5 % 3 # 2
divmod(5, 3) # 0, 3

# 最大公约数
math.gcd(24, 18) # 6

# 最小公倍数
a*b / math.gcd(a, b)

```
- 排列与组合
```python
math.perm(3)   # 6
math.perm(4,2) # 12

math.comb(5,2) # 10
```

```python
import itertools
list(itertools.combinations(range(1,5), 2)) # [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
list(itertools.permutations(range(1,4), 3)) # [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
```
- 最大公约数与最小公倍数
```python
def gcd(a, b):
	a, b = max(a,b), min(a,b)
	r = a%b
	while r:
		a, b = b, r
		r = a % b
	return b

def lcm(a, b):
    return a*b/gcd(a,b)
```

- 质数判断
```python
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
```

- 质因数分解
```python
def prime_factors(num):
    i = 2
    factors = []
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            factors.append(i)
    if num > 1:
        factors.append(num)
    return factors
```

- 回文数判断
```python
def f(n):
    return str(n)==str(n)[::-1]
```

- 进制转换
```python

```

- 闰年判断
```python
import calendar
calendar.isleap(2024) # True
```

```python
def isLeap(year):
    if year % 100 == 0:
        return year%400==0
    return year%4 == 0
```
# 位运算
```python

```

# 哈希
```python

```

# 集合
```python

```

# 搜索
- 深度优先搜索DFS

**类型一**：只标记

[leetcode-419. 甲板上的战舰](https://leetcode.cn/problems/battleships-in-a-board/)

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/55c0ea1219a591359f06e0c9da40487b.image.png)

目标：搜索战舰数量

```python
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m, n = len(board), len(board[0])
        vis = [[False for j in range(n)] for i in range(m)]
        def dfs(x, y):
            vis[x][y] = True
            for dx, dy in [(0,1), (1,0), (0, -1), (-1, 0)]:
                tx, ty = x+dx, y+dy
                if 0 <= tx < m and 0 <= ty < n:
                    if board[tx][ty]=='X' and not vis[tx][ty]:
                        dfs(tx, ty)
        ans = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X' and not vis[i][j]:
                    dfs(i,j,vis)
                    ans += 1
        return ans
```
**类型二：** 需要回溯

[leetcode-面试题 08.12. 八皇后](https://leetcode.cn/problems/eight-queens-lcci/)
```python
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def dfs(i):
            if i == n:
                ans.append(cur.copy()) # <== 注意copy
                return
            for j in range(n):
                if j in columns or i+j in diag1 or i-j in diag2:
                    continue
                cur.append(j)
                columns.add(j)
                diag1.add(i+j)
                diag2.add(i-j)
                dfs(i+1)
                cur.pop()
                columns.remove(j)
                diag1.remove(i+j)
                diag2.remove(i-j)

        columns, diag1, diag2 = set(), set(), set()
        cur = []
        ans = []
        dfs(0)
        res = []
        for item in ans:
            t = [["." for j in range(n)] for i in range(n)]
            for i, p in enumerate(item):
                t[i][p] = 'Q'
            t = ["".join(row) for row in t]
            res.append(t)
        return res
```
[leetcode-46. 全排列](https://leetcode.cn/problems/permutations/)
```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        def dfs(k):
            if k==n:
                ans.append(cur[:])
                return
            for i in range(n):
                if not used[i]:
                    cur.append(nums[i])
                    used[i] = True
                    dfs(k+1)
                    used[i] = False
                    cur.pop()
        used = [False for i in range(n)]
        cur = []
        ans = []
        dfs(0)
        return ans
```
- 广度优先搜索BFS

```python

```
- 记忆化搜索
> 重点：`@lru_cache(None)`

[leetcode-70. 爬楼梯](https://leetcode.cn/problems/climbing-stairs/)
```python
class Solution:
    @lru_cache(None)
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)
```
# 动态规划
## 背包问题
### 01背包
一般情况：
$$
\begin{equation*}
    dp[i][j]=
    \begin{cases}
    dp[i-1][j], & j<weights[i],\\
    max(dp[i-1][j], dp[i-1][j-weights[i]]+value[i]), & j \ge weights[i]
    \end{cases}
\end{equation*}
$$

[leetcode-416. 分割等和子集](https://leetcode.cn/problems/partition-equal-subset-sum/)
$$
\begin{equation*}
    dp[i][j]=
    \begin{cases}
    dp[i-1][j], & j<nums[i],\\
    dp[i-1][j] \:\: | \:\:dp[i-1][j-nums[i]], & j \ge nums[i]
    \end{cases}
\end{equation*}
$$
```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        s = sum(nums)
        if n<2:
            return False
        if s%2!=0:
            return False
        V = s//2
        dp = [[False for i in range(V+1)] for i in range(n+1)]
        for j in range(n+1):
            dp[j][0] = True
        for i in range(1,n+1):
            for j in range(V+1):
                if j >= nums[i-1]:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][V]
```
空间优化：(注意第二层循环逆序)
```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        s = sum(nums)
        if n<2:
            return False
        if s%2!=0:
            return False
        V = s//2
        dp = [False for i in range(V+1)]
        dp[0] = True
        for i in range(1,n+1):
            for j in range(V, 0, -1):
                if j >= nums[i-1]:
                    dp[j] = dp[j] or dp[j-nums[i-1]]
        return dp[V]
```

### 完全背包  
- 装满：  

[leetcode-322. 零钱兑换](https://leetcode.cn/problems/coin-change/)

目标：不同面额的硬币，凑出指定金额，所需要的最少硬币数
$$
dp[i] = min(dp[i-c])+1, if \:\: i \ge c
$$
```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        M = float("inf")
        dp = [M]*(amount+1)
        dp[0] = 0
        for i in range(amount+1):
            for c in coins:
                if i>=c:
                    dp[i] = min(dp[i], dp[i-c]+1)
        if dp[amount] != M:
            return dp[amount]
        return -1
```

[leetcode-518. 零钱兑换 II](https://leetcode.cn/problems/coin-change-ii/)  
目标：不同面额的硬币，凑出指定金额的不同方案数

$$
\begin{equation*}
    dp[i][j]=
    \begin{cases}
    dp[i-1][j], & j<coins[i],\\
    dp[i-1][j]+dp[i][j-coins[i-1]], & j \ge coins[i]
    \end{cases}
\end{equation*}
$$
```python
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        M = float("inf")
        dp = [[0 for i in range(amount+1)] for j in range(n+1)]
        for i in range(n+1):
            dp[i][0] = 1

        for i in range(1,n+1):
            for j in range(amount+1):
                if j >= coins[i-1]:
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][amount]
```
空间优化：(注意第二层循环顺序)  
$$
dp[j] = dp[j] + dp[j-coins[i-1]],\: if\: j \ge coins[i-1]
$$

```python
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [0 for i in range(amount+1)]
        dp[0] = 1
        for i in range(n):
            for j in range(1, amount+1):
                if j >= coins[i]:
                    dp[j] = dp[j] + dp[j-coins[i]]
        return dp[amount]
```

[leetcode-377. 组合总和 Ⅳ (相当于 零钱兑换 III)](https://leetcode.cn/problems/combination-sum-iv/)  
目标：不同面额的硬币，凑出指定金额的不同方案数，考虑顺序  
（注意循环顺序，先容量再物品）
```python
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [1] + [0]*target
        for i in range(target+1):
            for num in nums:
                if i>=num:
                    dp[i] += dp[i-num]
        return dp[target]
```

## 一维DP
```python

```

环形：
```python

```
## 二维DP
```python

```
## 子序列问题
[leetcode-300. 最长递增子序列](https://leetcode.cn/problems/longest-increasing-subsequence/)
$$
dp[i] = max(dp[j])+1,\:\:\: 0 \le j<i \:\: \&\& \:\: nums[j]<nums[i]
$$
```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        ans = 1
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
                ans = max(ans, dp[i])
        return ans
```


[leetcode-1143. 最长公共子序列](https://leetcode.cn/problems/longest-common-subsequence/)
$$
\begin{equation*}
    dp[i][j]=
    \begin{cases}
    dp[i-1][j-1]+1, & s_1[i] = s_2[j],\\
    max(dp[i-1][j], dp[i][j-1]), & s_1[i] \ne s_2[j]
    \end{cases}
\end{equation*}
$$
```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        dp = [[0 for i in range(m+1)] for j in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[n][m]
```

## 分割类问题
```python

```
## 其他
```python

```

# 排序
```python
```
# 查找
- 二分查找

```python
```

# 并查集
```python
```
# 二叉树
- 遍历
```python
```
# 堆
```python
```
# 字典树

```python
```
# 线段树

```python
```
# 树形数组
```python
```
# 博弈
```python
```
# 前缀和
- 一维
```python
```
- 二维
```python
```
# 状态机
```python
```