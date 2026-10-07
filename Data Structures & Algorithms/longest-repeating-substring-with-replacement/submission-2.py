class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        duplicates = {}
        lst =list(s)
        for item in lst:
            if item in duplicates:
                duplicates[item] += 1
            else:
                duplicates[item] = 1
        res = max(duplicates.values())
        if res+k >len(s):
            return len(s)
        print(res)
        return res+k