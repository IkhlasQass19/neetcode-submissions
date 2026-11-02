
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        start = 0
        end = 0
        arr = []
        stack = []

        while end < len(nums):

            if stack and stack[0] < start:
                stack.pop(0)

            if stack and nums[stack[-1]] < nums[end]:
                stack.pop()
                continue

            stack.append(end)

            if end - start + 1 == k:
                arr.append(nums[stack[0]])
                start += 1

            end += 1

        return arr
