# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            # print(root.val, end=" ")
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


if __name__ == '__main__':
    # begin
    tree1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    s = Solution()
    print(s.maxDepth(tree1))

    tree2 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7, TreeNode(1))))
    s = Solution()
    print(s.maxDepth(tree2))
