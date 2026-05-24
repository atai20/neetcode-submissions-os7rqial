class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        '''
        Plan:
        go over every character making 
        substrings from start to the point
        where 2 letters don't match

        after that still go over s only,
        stopping t at some index
        and when it is the next character
        of t, move them both again, 

        if next character is starting s
        again, start the new process with
        new array
        
        but when they don't match again
        we return back

        if we reach end of s, output
        the ending substring length of t

        other wise return 0

        but there are other cases like:

        cocodaching

        with our algo will give 4,
        when it is truly 0

        we have to try to go over elements
        but also if it is start again
        after we found first unmatching,
        add to algo.


        Code:
        t_index = 0


        for i in range(len(s)):
            if i < len(t):
                if t[t_index] == s[i]:
                    t_index += 1
        return len(t[i_index:])
        '''
        t_index = 0
        for i in range(len(s)):
            if t_index < len(t):
                if t[t_index] == s[i]:
                    t_index += 1
        return len(t[t_index:])
                



     