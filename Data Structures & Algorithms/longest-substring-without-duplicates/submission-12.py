class Solution:
    def  lengthOfLongestSubstring(self, s: str) -> int:

        locs = {}
        biggest_l = 0
        start = 0

        for i in range(len(s)):
            if s[i] in locs and start <= locs[s[i]]:
                start = locs[s[i]] + 1
        
            locs[s[i]] = i
            biggest_l = max(i - start + 1, biggest_l)


        return biggest_l

        