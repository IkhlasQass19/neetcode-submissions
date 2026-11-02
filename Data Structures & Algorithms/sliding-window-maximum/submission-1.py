
from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        start = 0
        end = 0
        arr = []
        q = deque()

        while end < len(nums):

            if q and q[0] < start:
                q.popleft()

            if q and nums[q[-1]] < nums[end]:
                q.pop()
                continue

            q.append(end)

            if end - start + 1 == k:
                arr.append(nums[q[0]])
                start += 1

            end += 1

        return arr
