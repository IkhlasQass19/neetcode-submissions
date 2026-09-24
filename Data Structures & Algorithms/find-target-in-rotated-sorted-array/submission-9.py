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
'''        class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1
        # find the pivot first
        while l < r:
            mid = l + (r - l) // 2
            if nums[r] < nums[mid]:
                l = mid + 1
            else:
                r = mid
        pivot = l
        # now we know pivot is smallest number so pivot through pivot - 1 is sorted
        l = pivot
        r = len(nums)-1
        
        if nums[pivot] <= target <= nums[r]:
            l = pivot
            r = len(nums) - 1
        else:
            l = 0
            r = pivot - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1

        

        '''      
      