# 给定一个由 0 和 1 组成的矩阵 matrix ，找出只包含 1 的最大矩形，并返回其面积。

# 注意：此题 matrix 输入格式为一维 01 字符串数组。

#  

# 示例 1：



# 输入：matrix = ["10100","10111","11111","10010"]
# 输出：6
# 解释：最大矩形如上图所示。
# 示例 2：

# 输入：matrix = []
# 输出：0
# 示例 3：

# 输入：matrix = ["0"]
# 输出：0
# 示例 4：

# 输入：matrix = ["1"]
# 输出：1
# 示例 5：

# 输入：matrix = ["00"]
# 输出：0
#  

# 提示：

# rows == matrix.length
# cols == matrix[0].length
# 0 <= row, cols <= 200
# matrix[i][j] 为 '0' 或 '1'
#  

# 注意：本题与主站 85 题相同（输入参数格式不同）： https://leetcode-cn.com/problems/maximal-rectangle/

from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for i in range(len(heights)):
            while len(stack) != 0 and heights[stack[-1]] >= heights[i]:
                height = heights[stack.pop()]
                if len(stack) == 0:
                    width = i
                else:
                    width = i - stack[-1] - 1
                maxArea = max(maxArea, height * width)
            stack.append(i)
        while len(stack) != 0:
            height = heights[stack.pop()]
            if len(stack) == 0:
                width = len(heights)
            else:
                width = len(heights) - stack[-1] - 1
            maxArea = max(maxArea, height * width)
        return maxArea


    def maximalRectangle(self, matrix: List[str]) -> int:
        if len(matrix) == 0:
            return 0
        maxArea = 0
        heights = [0] * len(matrix[0])
        for row in matrix:
            for i in range(len(row)):
                if row[i] == '0':
                    heights[i] = 0
                else:
                    heights[i] = heights[i] + 1
            maxArea = max(maxArea, self.largestRectangleArea(heights))
        return maxArea

if __name__ == '__main__':
    solution = Solution()
    res = solution.largestRectangleArea([2,4])
