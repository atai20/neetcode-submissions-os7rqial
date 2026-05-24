class Solution:
    def scoreOfString(self, s: str) -> int:
        '''
        go over letters 2 by 2
        '''
        res = 0
        for i in range(len(s) - 1):
            res += abs(ord(s[i]) - ord(s[i + 1]))
        return res

        '''
        code

        '''