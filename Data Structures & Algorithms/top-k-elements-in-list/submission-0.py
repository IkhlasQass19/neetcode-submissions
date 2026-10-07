from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        res = [num for num, freq in count.items() if freq >= k]
        print(res)
        return res
        