from common import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class SolutionA:
    def rob(self, root: Optional[TreeNode]) -> int:
        """
        This does not work. However it could be an interesting example
        of how I can be misled by examples.
        """
        if not root:
            return 0

        q = deque([(root, 0)])
        sumsbylevel = defaultdict(int)
        while q:
            node, level = q.popleft()
            sumsbylevel[level] += node.val
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))

        oddsum = 0
        evensum = 0
        for level, val in sumsbylevel.items():
            if level & 1 == 1:
                oddsum += val
            else:
                evensum += val

        return max(oddsum, evensum)


class SolutionB:
    def rob(self, root: Optional[TreeNode]) -> int:
        """
        Exceeds time limit
        """
        if not root:
            return 0
        res = root.val
        if root.left:
            res += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            res += self.rob(root.right.left) + self.rob(root.right.right)
        return max(res, self.rob(root.left) + self.rob(root.right))


class SolutionC:
    @lru_cache
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            result = [0] * 2
            if not root:
                return result

            left = dfs(root.left)
            right = dfs(root.right)
            result[0] = max(*left) + max(*right)
            result[1] = root.val + left[0] + right[0]
            return result

        return max(*dfs(root))
