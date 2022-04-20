#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self) -> None:
        self.pre = float('-inf')

    def isValidBST(self, root: TreeNode) -> bool:
        # return self.isValidBSTHelp(root, None, None)
        if not root:
            return True
        if not self.isValidBST(root.left):
            return False
        if root.val <= self.pre:
            return False
        self.pre = root.val
        return self.isValidBST(root.right)

    def isValidBSTHelp(self, root: TreeNode, min: TreeNode, max: TreeNode) -> bool:
        if not root:
            return True
        if min and root.val <= min.val:
            return False
        if max and root.val >= max.val:
            return False
        return self.isValidBSTHelp(root.left, min, root) and self.isValidBSTHelp(root.right, root, max)
# @lc code=end
