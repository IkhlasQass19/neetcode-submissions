class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0

        prefix = [0] * n
        sufix = [0] * n

        prefix[0] = height[0]
        for i in range(1, n):
            prefix[i] = max(prefix[i - 1], height[i])

        sufix[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            sufix[i] = max(sufix[i + 1], height[i])

        res = 0
        for i in range(n):
            res += min(prefix[i], sufix[i]) - height[i]
        return res