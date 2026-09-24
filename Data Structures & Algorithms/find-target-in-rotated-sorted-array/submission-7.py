class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i=0
        j=len(nums)//2
        if target not in nums :
            return -1
        if target in nums[:len(nums)//2] :
            i=0
            j=len(nums)//2
        else :
            i=len(nums)//2
            j=len(nums)
        while i<j :
            if nums[i]== target :
                return i
            else :
                i+=1
        #using the binary search
        
      