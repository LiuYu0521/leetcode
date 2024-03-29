# 请根据每日 气温 列表 temperatures ，重新生成一个列表，要求其对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。如果气温在这之后都不会升高，请在该位置用 0 来代替。

#  

# 示例 1:

# 输入: temperatures = [73,74,75,71,69,72,76,73]
# 输出: [1,1,4,2,1,1,0,0]
# 示例 2:

# 输入: temperatures = [30,40,50,60]
# 输出: [1,1,1,0]
# 示例 3:

# 输入: temperatures = [30,60,90]
# 输出: [1,1,0]
#  

# 提示：

# 1 <= temperatures.length <= 105
# 30 <= temperatures[i] <= 100
#  

# 注意：本题与主站 739 题相同： https://leetcode-cn.com/problems/daily-temperatures/
from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack = []
        # res = [0]*len(temperatures)
        # for i in range(len(temperatures)):
        #     while len(stack) != 0 and temperatures[i] > temperatures[stack[-1]]:
        #         index = stack.pop()
        #         res[index] = i - index
        #     stack.append(i)
        # return res

        stack = []
        res = [0]*len(temperatures)
        for i in range(len(temperatures)-1, -1, -1):
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
            if not stack:
                res[i] = 0
            else:
                res[i] = stack[-1] - i
            stack.append(i)
        return res
            


if __name__ == '__main__':
    temperatures = [73,74,75,71,69,72,76,73]
    solution = Solution()
    solution.dailyTemperatures(temperatures)
