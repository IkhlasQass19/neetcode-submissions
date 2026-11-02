
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        start = 0
        end = 0
        arr = []
        stack = []
        head = 0

        while end < len(nums):

            if head < len(stack) and stack[head] < start:
                head += 1

            if head < len(stack) and nums[stack[-1]] < nums[end]:
                stack.pop()
                continue

            stack.append(end)

            if end - start + 1 == k:
                arr.append(nums[stack[head]])
                start += 1

            end += 1

        return arr
