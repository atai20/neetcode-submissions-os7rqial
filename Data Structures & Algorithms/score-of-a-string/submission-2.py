class Solution:
    def scoreOfString(self, s: str) -> int:
        '''
        go over letters 2 by 2
        '''
        result = 0

        for i in range(len(s)-1):
            result += abs(ord(s[i]) - ord(s[i+1]))
        return result

        '''
        code

        '''