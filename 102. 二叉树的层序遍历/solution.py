# 给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。

#  

# 示例 1：


# 输入：root = [3,9,20,null,null,15,7]
# 输出：[[3],[9,20],[15,7]]
# 示例 2：

# 输入：root = [1]
# 输出：[[1]]
# 示例 3：

# 输入：root = []
# 输出：[]
#  

# 提示：

# 树中节点数目在范围 [0, 2000] 内
# -1000 <= Node.val <= 1000

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import *
import queue
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = queue.Queue()
        q.put(root)
        while not q.empty():
            this_layer = []
            for i in range(q.qsize()):
                node = q.get()
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
                this_layer.append(node.val)
            res.append(this_layer)
        return res
