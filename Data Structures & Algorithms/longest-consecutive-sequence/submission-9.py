class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''numbers = set(nums)
        longest = 0

        for num in numbers:
            if num - 1 not in numbers:
                current = num
                count = 1
                while current + 1 in numbers:
                    current += 1
                    count += 1
                longest = max(longest, count)
        return longest'''
        if not nums:
            return 0

        numbers = sorted(set(nums))

        longest = 1
        current = 1

        for i in range(1, len(numbers)):
            if numbers[i] == numbers[i - 1] + 1:
                current += 1
            else:
                longest = max(longest, current)
                current = 1

        return max(longest, current)