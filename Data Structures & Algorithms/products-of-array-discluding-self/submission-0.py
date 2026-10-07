class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        for i in range (0,len(nums)) :
            output[i]=1
            j=0
            while j<len(nums) :
                if i!=j :
                    output[i]*=nums[j]
                j=j+1
        return output
            