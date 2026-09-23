class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        i = 0
        max_count = 0
        max_freq = 0
        count = {}

        for j in range(len(s)):

            count[s[j]] = count.get(s[j], 0) + 1

    
            max_freq = max(max_freq, count[s[j]])

            
            window = j - i + 1

           
            if window - max_freq > k:
                count[s[i]] -= 1
                i += 1

           
            max_count = max(max_count, j - i + 1)

        return max_count