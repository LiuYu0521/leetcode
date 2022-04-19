# 给你二叉树的根节点 root ，返回它节点值的 前序 遍历。

#  

# 示例 1：


# 输入：root = [1,null,2,3]
# 输出：[1,2,3]
# 示例 2：

# 输入：root = []
# 输出：[]
# 示例 3：

# 输入：root = [1]
# 输出：[1]
# 示例 4：


# 输入：root = [1,2]
# 输出：[1,2]
# 示例 5：


# 输入：root = [1,null,2]
# 输出：[1,2]
#  

# 提示：

# 树中节点数目在范围 [0, 100] 内
# -100 <= Node.val <= 100
#  

# 进阶：递归算法很简单，你可以通过迭代算法完成吗？

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/binary-tree-preorder-traversal
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import *   
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # res = []
        # def preorderTraversalHelp(root: Optional[TreeNode], res: List[int]):
        #     if not root:
        #         return
        #     res.append(root.val)
        #     preorderTraversalHelp(root.left, res)
        #     preorderTraversalHelp(root.right, res)
        # preorderTraversalHelp(root, res)
        # return res

        if not root:
            return []
        res = []
        stack = [(False, root)]
        while stack:
            is_mid,node = stack.pop()
            if not node:
                continue
            if is_mid:
                res.append(node.val)
            else:
                stack.append((False, node.right))
                stack.append((False, node.left))
                stack.append((True, node))
        return res
