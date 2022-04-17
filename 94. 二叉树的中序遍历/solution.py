# 给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。

#  

# 示例 1：


# 输入：root = [1,null,2,3]
# 输出：[1,3,2]
# 示例 2：

# 输入：root = []
# 输出：[]
# 示例 3：

# 输入：root = [1]
# 输出：[1]
#  

# 提示：

# 树中节点数目在范围 [0, 100] 内
# -100 <= Node.val <= 100
#  

# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？


# Definition for a binary tree node.
from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 递归
        # res = []
        # self.inorder(root, res)
        # return res

        # 非递归
        # res = []
        # stack = []
        # while root is not None or stack:
        #     while root is not None:
        #         stack.append(root)
        #         root = root.left
        #     root = stack.pop()
        #     res.append(root.val)
        #     root = root.right
        # return res

        res = []
        stack = [(False, root)]
        while stack:
            is_mid, node = stack.pop()
            if node is None:
                continue
            if not is_mid:
                if node.right is not None:
                    stack.append((False, node.right))
                stack.append((True, node))
                if node.left is not None:
                    stack.append((False, node.left))
            else:
                res.append(node.val)
        return res

            
    def inorder(self, root: Optional[TreeNode], res: List[int]):
        if root is None:
            return
        self.inorder(root.left, res)
        res.append(root.val)
        self.inorder(root.right, res)