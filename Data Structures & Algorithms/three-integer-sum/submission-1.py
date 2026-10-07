class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        i = 0
        j = i + 1
        k = j + 1

        arraay = []

        while i < len(nums) - 2:
            print (nums[i], nums[j] ,nums[k] )
            if nums[i] + nums[j] + nums[k] == 0:
                print (nums[i], nums[j] ,nums[k] ,'=',0)
                row = [nums[i], nums[j], nums[k]]
                sorted(row)
                  # Remove duplicates
                if sorted(row) not in arraay:
                    arraay.append(row)
                k += 1

            elif k < len(nums) - 1:
                print('k',k)
                k += 1

            elif j < len(nums) - 2:
                print('j',j)
                j += 1
                k = j + 1

            else:

                i += 1
                j = i + 1
                k = j + 1

        return arraay