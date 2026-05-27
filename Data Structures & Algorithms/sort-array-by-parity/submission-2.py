class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        '''
        arr1 = even
        arr2 = odd

        '''
        result = []
        odd_arr = []
   

        for i in nums:
            if i % 2 == 0:
                result.append(i)
            else:
                odd_arr.append(i)
        
        result.extend(odd_arr)

        return result
        
            
        
        