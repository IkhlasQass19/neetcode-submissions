class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Always binary search on the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        left, right = 0, m

        while left <= right:
            # Partition positions
            partition1 = (left + right) // 2
            partition2 = (m + n + 1) // 2 - partition1

            # Elements around the partitions
            left1 = nums1[partition1 - 1] if partition1 > 0 else float("-inf")
            right1 = nums1[partition1] if partition1 < m else float("inf")

            left2 = nums2[partition2 - 1] if partition2 > 0 else float("-inf")
            right2 = nums2[partition2] if partition2 < n else float("inf")

            # Check if the partition is valid
            if left1 <= right2 and left2 <= right1:
                if (m + n) % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2

                return float(max(left1, left2))

            elif left1 > right2:
                # Move partition1 to the left
                right = partition1 - 1

            else:
                # Move partition1 to the right
                left = partition1 + 1

        raise ValueError("Input arrays must be sorted")
