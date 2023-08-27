from typing import Optional
#If root isnt null keeping going left and appending to the stack
#If root is null pop and append that value then set root = to right of the node you just appended to result


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        if root is None:
            return []

        stack = []
        result = []

        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                result.append(node.val)
                root = node.right

        return result


# Create a binary tree
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
# Create an instance of the Solution class
solution = Solution()

# Test the inorderTraversal method
result = solution.inorderTraversal(root)
print(result)