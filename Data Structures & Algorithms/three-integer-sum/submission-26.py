class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        The same approach as before, but after each moving around we also move the middle pointer
        We do that to make it from O(n^3) solution to O(n^2)

        the 2 sum solution:


        '''
        nums = sorted(nums)

        result = set()

        m = 1
        diff = 0

        while m < len(nums) - 1:
            l = 0
            r = len(nums) - 1

            while r > m and m > l:

                if nums[r] + nums[m] + nums[l] == 0:
                    print(l, r)
                    result.add((nums[l], nums[m], nums[r]))
                    l += 1
                    r -= 1

                elif nums[r] + nums[m] + nums[l] > 0:
                    r -= 1

            
                else:
                    l += 1



            m += 1
                            
                    
            '''
            -2, -1, 1, 2

            -1

            1

            2

            '''
        result = list(result)

        for i in range(len(result)):
            result.append(list(result[i]))
            result.pop(i)

    
        return result