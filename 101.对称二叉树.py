#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import *
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isSymmetricHelp(root.left, root.right)

    def isSymmetricHelp(self, node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
        if not node1 and not node2:
            return True
        elif (not node1 and node2) or (node1 and not node2):
            return False
        return node1.val == node2.val and self.isSymmetricHelp(node1.left, node2.right) and self.isSymmetricHelp(node1.right, node2.left)
# @lc code=end

