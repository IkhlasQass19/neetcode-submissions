class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        i = 0
        max_count = 0
        max_freq = 0
        count = {}

        for j in range(len(s)):

            # Add current character
            count[s[j]] = count.get(s[j], 0) + 1

            # Highest frequency in our window
            max_freq = max(max_freq, count[s[j]])

            # Current window size
            window = j - i + 1

            # Too many characters need replacement
            if window - max_freq > k:
                count[s[i]] -= 1
                i += 1

            # Current valid window size
            max_count = max(max_count, j - i + 1)

        return max_count