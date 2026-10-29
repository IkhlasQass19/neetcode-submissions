
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        n = len(nums)
        m = int(n / 2)

        while i < n:
            if nums[m] > target:
                n = m
                m = (i + n) // 2

            elif nums[m] < target:
                i = m + 1
                m = (i + n) // 2

            else:
                return m

        return -1
