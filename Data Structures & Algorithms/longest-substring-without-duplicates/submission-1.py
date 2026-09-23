'''class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        listChar = list(s)
        stri = ""
        count = 0
        for i in range(len(listChar)):
            while listChar[i] in stri:
                stri = stri[1:]
            stri += listChar[i]
            count = max(count, len(stri))
        return count'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        stri = ""
        i = 0
        j = 0
        max_count = 0

        while j < len(s):
            if s[j] not in stri:
                stri += s[j]
                j += 1

                max_count = max(max_count, len(stri))

            else:
                stri = stri[1:]
                i += 1

        return max_count