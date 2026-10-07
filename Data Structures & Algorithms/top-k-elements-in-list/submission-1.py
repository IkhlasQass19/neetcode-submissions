from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numbers = {}

        for num in set(nums):
            count = nums.count(num)
            numbers[num] = count

        sorted_numbers = sorted(
            numbers,
            key=numbers.get,
            reverse=True
        )

        return sorted_numbers[:k]