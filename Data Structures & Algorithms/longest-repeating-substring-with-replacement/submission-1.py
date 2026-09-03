class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        store frequencies, l, store maximum current character
        reduce window by one when too much
        '''
        l = 0
        longest = 0
        dict1 = {}

        for i in range(len(s)):
            if s[i] not in dict1:
                dict1[s[i]] = 1
            else:
                dict1[s[i]] += 1
            '''
            how instead of dict1[s[i]], I get max frequency one?
            '''
            if i - l - max(dict1.values()) + 1 > k:
                dict1[s[l]] -= 1
                l += 1
            longest= max(longest, i - l + 1)
        
        return longest
                
