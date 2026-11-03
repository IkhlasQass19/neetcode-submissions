from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        arr = []

        for i in range(len(nums)):

            # 1. Remove indices outside the window
            while q and q[0] <= i - k:
                q.popleft()

            # 2. Remove smaller elements from the back
            while q and nums[q[-1]] <= nums[i]:
                q.pop()

            # 3. Add the current index
            q.append(i)

            # 4. Store the maximum once window is full
            if i >= k - 1:
                arr.append(nums[q[0]])

        return arr