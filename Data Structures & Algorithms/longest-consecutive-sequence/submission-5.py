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
        numbers = list(nums)
        longest = 0
        Snumb=sorted(numbers)
        print("nubers " ,Snumb)
        i=0
        count=0
        if len(numbers)==1 :
            return 1
        while i<len(Snumb)-1 : 
            if  Snumb[i+1] - 1 == Snumb[i] or Snumb[i+1] - Snumb[i]  == 0    :
                count+=1
           
            else :
                count=0
            i+=1
            longest = max(longest, count)

        return longest