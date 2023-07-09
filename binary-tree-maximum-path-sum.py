def maxPathSum(root):
    """
    https://leetcode.cn/problems/binary-tree-maximum-path-sum/submissions/
    """
    maxSum = float("-inf")

    def dfs(root):
        nonlocal maxSum
        if not root:
            return 0
        left = max(0, dfs(root.left))
        right = max(0, dfs(root.right))
        innerMaxSum = left + root.val + right
        maxSum = max(maxSum, innerMaxSum)
        return root.val + max(left, right)

    dfs(root)
    return maxSum
