from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        used = set()

        for i in range(len(strs)):
            if i in used:
                continue

            group = []

            for j in range(len(strs)):
                if j not in used and self.isAnagram(strs[i], strs[j]):
                    group.append(strs[j])
                    used.add(j)

            output.append(group)

        return output