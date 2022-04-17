# 给定一个二叉树，找出其最大深度。
#
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例：
# 给定二叉树 [3,9,20,null,null,15,7]，
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回它的最大深度 3 。
#

from typing import *
import queue


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if root is None:
        #     return 0
        # left = self.maxDepth(root.left)
        # right = self.maxDepth(root.right)
        # return max(left, right) + 1

        if root is None:
            return 0
        q = queue.Queue()
        maxDep = 0
        q.put(root)
        while not q.empty():
            for i in range(q.qsize()):
                node = q.get()
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
            maxDep = maxDep + 1
        return maxDep
