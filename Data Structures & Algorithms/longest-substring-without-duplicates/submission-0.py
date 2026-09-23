class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        listChar = list(s)
        stri = ""
        count = 0
        for i in range(len(listChar)):
            while listChar[i] in stri:
                stri = stri[1:]
            stri += listChar[i]
            count = max(count, len(stri))
        return count