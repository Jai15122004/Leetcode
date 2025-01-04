from collections import Counter

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        char_count = Counter(s)  # Count the occurrences of each character
        count = 0

        for key, value in char_count.items():
            # Only consider characters with more than one occurrence
            if value > 1:
                first = s.find(key)  # Find first occurrence
                last = s.rfind(key)  # Find last occurrence

                if last - first > 1:  # Check if there are characters in between
                    # Count unique characters between the first and last occurrence
                    count += len(set(s[first + 1:last]))

        return count
