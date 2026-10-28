
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        maxArea= 0
        i = 0

        while i <= n:
            currentHeight = heights[i] if i < n else 0

            if stack and currentHeight < heights[stack[-1]]:
                h = heights[stack.pop()]

                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i

                area = h * width
                maxArea = max(maxArea, area)

            else:
                stack.append(i)
                i += 1

        return maxArea
