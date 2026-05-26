class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        s_index = 0

        for i in t:
            if s_index>=len(s):
                break
            if i == s[s_index]:
                s_index += 1

        print(s_index)
        print(len(s))
        return s_index == len(s)
        