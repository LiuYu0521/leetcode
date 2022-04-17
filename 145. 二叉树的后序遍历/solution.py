# 给你一棵二叉树的根节点 root ，返回其节点值的 后序遍历 。

#  

# 示例 1：


# 输入：root = [1,null,2,3]
# 输出：[3,2,1]
# 示例 2：

# 输入：root = []
# 输出：[]
# 示例 3：

# 输入：root = [1]
# 输出：[1]
#  

# 提示：

# 树中节点的数目在范围 [0, 100] 内
# -100 <= Node.val <= 100
#  

# 进阶：递归算法很简单，你可以通过迭代算法完成吗？

from inspect import stack
from typing import *
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # def postorder(root: Optional[TreeNode], res: List[int]):
        #     if root is None:
        #         return
        #     postorder(root.left, res)
        #     postorder(root.right, res)
        #     res.append(root.val)
        
        # res = []
        # postorder(root, res)
        # return res

        stack = [(False, root)]
        res = []
        while stack:
            is_mid, node = stack.pop()
            if node is None:
                continue
            if not is_mid:
                stack.append((True, node))
                if node.right is not None:
                    stack.append((False, node.right))
                if node.left is not None:
                    stack.append((False, node.left))
            else:
                res.append(node.val)
        return res
        
