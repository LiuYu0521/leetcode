# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

# 有效字符串需满足：

# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
#  

# 示例 1：

# 输入：s = "()"
# 输出：true
# 示例 2：

# 输入：s = "()[]{}"
# 输出：true
# 示例 3：

# 输入：s = "(]"
# 输出：false
# 示例 4：

# 输入：s = "([)]"
# 输出：false
# 示例 5：

# 输入：s = "{[]}"
# 输出：true
#  

# 提示：

# 1 <= s.length <= 104
# s 仅由括号 '()[]{}' 组成

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        stack = []
        pairs = {')':'(', ']':'[', '}':'{'}
        for token in s:
            if token in pairs.values():
                stack.append(token)
            else:
                if len(stack) == 0 or stack[-1] != pairs[token]:
                    return False
                else:
                    stack.pop()
        return not stack

