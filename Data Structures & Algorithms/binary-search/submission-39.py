class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        if len(nums) == 2:
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r
            
            return -1
        if nums[l] == target:
            return l
        if nums[r] == target:
            return r
        while r > l:
            m = l + (r-l) // 2
            if nums[m] > target:
                r = m
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        
        '''
        [-1,0,3,5,9,12]


        m = 0 + 2 = 2
        l = 0
        r = 5
        
        nums[m] = 3
        target = 2

        m = 0 
        l = 0
        r = 1
        
        nums[m] = -1
        target = 2

        m = 0
        l = 0
        r = 1

        nums[m] = -1
        target = 2

        

        '''
        
        return -1