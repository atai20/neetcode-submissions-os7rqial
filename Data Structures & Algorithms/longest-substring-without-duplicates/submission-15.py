class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        dict1 = {}
        longest = 0

        for i in range(len(s)):
            if s[i] in dict1 and dict1[s[i]] >= l:
                l = dict1[s[i]] + 1

            dict1[s[i]] = i
            
            longest = max(longest, i - l + 1)
        
        return longest
