class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        make dictionary of frequencies
        go over array and add it to the dict1, or add 1 to the frequency,
        convert frequencies to array and sort,
        go over the values of dict of the array k times
        '''

        dict1 = {}
        reversed_dict = {}
        freqs = []
        keys = []
        result = []
        blacklist = set()
        counter = 0

        for i in nums:
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i] += 1
        print(dict1)
        
        '''
        we either first get out the value array and sort it then finding keys with particular values
        
        or

        we can reverse the dictionary and then dort by keys
        '''

        for key, val in dict1.items():
            if val in reversed_dict.keys():
                reversed_dict[val].append(key)
            else:
                reversed_dict[val] = [key]
        
        reversed_dict = dict(sorted(reversed_dict.items(), reverse = True))
        print(reversed_dict)

        for i in reversed_dict:
            if k == 0:
                break
            for i2 in reversed_dict[i]:
                result.append(i2)
                k -= 1
        

        
        
        
        return result
        

        