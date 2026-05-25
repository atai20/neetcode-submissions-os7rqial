class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        Bruteforce:

        define array and add sets of characters there as we go 


        dict1 = {} #{("act") : ["act", "cat"], ...}
        res1 = []


        for str1 in strs:
            key1 = set(str1)

            if key1 in dict1:
                dict1[key1].append(str1)
            else:
                dict1[key1] = [str1]

        for i in dict1:
            res1.append(i)
        
        return res1

        '''

        dict1 = {}
        res1 = []

        for str1 in strs:
            key1 = tuple(sorted(str1))

            if key1 in dict1:
                dict1[key1].append(str1)
            else:
                dict1[key1] = [str1]

        for group in dict1.values():
            res1.append(group)

        return res1

        '''
        test:

        str1 = act
        key1 = {a, c, t}

        dict1 = {{a, c, t}:[act]}

        str1 = post
        key1 = {p, o, s, t}

        ...

        

        '''
        
        
        

        