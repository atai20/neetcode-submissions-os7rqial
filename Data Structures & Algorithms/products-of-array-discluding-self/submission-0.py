class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        The task here is to efficiently find product of every element despite the one for i.

        For bruteforce:

        I have to create an array for result.
        I will then go over the array to save in dictionary the product of all elements despite i.
        after that I will make iteration through dictionary using original array to store in result.
        I will then return result.

        addition:
            it should dynamically add numbers to the i's key in dictionary, 
            meaning all elements despite i's should be placed there.
            My idea here is very inefficient since I wanted to check for values each time if they are in the index or not
            I have another idea, here, instead of adding values to one element in the dictionary, it will add it to all values at the same time
            by assigning new values to all keys despite the i's.
            This will also be bruteforce approach.

        Pseudocode:

        result = []
        dict_for_all_but_i = {}

        for index1 in range(len(nums)):
            prod = 1
            for index2 in range(len(nums)):
                if index1 != index2:
                    prod *= 1
            dict_for_all_but_i[index2] = prod

        for index3 in dict_for_all_but_i:
            result.append(dict_for_all_but_i[index3])
        
        return result


        since instead of pseudocode I pretty much used python I will run this after verification.
        
        The time complexity is O(n^2+n) or O(n^2), space complexity is O(n)

        '''

        result = []
        dict_for_all_but_i = {}

        for index1 in range(len(nums)):
            prod = 1
            for index2 in range(len(nums)):
                if index1 != index2:
                    prod *= nums[index2]
                    
            #this goes through every element, but it ignores the ones with same index
            dict_for_all_but_i[index1] = prod

        for index3 in range(len(nums)):
            if (index3 in dict_for_all_but_i):
                result.append(dict_for_all_but_i[index3])
        
        return result

        '''
        example input:[1,2,4,6]
        dictionary:
        {0:48, }
        '''