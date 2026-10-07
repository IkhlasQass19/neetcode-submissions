class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        i = 0
        j = i + 1
        k = j + 1

        arraay = []

        while k < len(nums):

            if nums[i] + nums[j] + nums[k] == 0:

                row = sorted([nums[i], nums[j], nums[k]])

                if row not in arraay:
                    arraay.append(row)

            k += 1

            if k >= len(nums):

                j += 1
                k = j + 1

                if j >= len(nums):

                    i += 1
                    j = i + 1
                    k = j + 1

        return arraay