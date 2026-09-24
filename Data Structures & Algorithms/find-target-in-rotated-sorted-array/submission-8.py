class Solution:
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

        

                     
      