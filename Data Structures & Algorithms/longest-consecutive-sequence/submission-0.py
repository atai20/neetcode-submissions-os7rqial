class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        minimum = 10**9
        maximum = -10**9
        maximum_iterations = 0
        iterations = 0

        for element in nums:
            if element > maximum:
                maximum = element

            if element < minimum:
                minimum = element

        for element in range(minimum, maximum+1):
            #under the hood this might actually iterate through even more if using in approach
            if element in nums:
                iterations += 1
            else:
                if iterations>maximum_iterations:
                    maximum_iterations = iterations
                iterations = 0
        if iterations>maximum_iterations:
            maximum_iterations = iterations
               
        
        return maximum_iterations




        '''
        The problem asks to find number of consequtive elements in an unordered list in O(n).

        I will use dictionary here that stores numbers that are bigger or smaller than
        the key by 1, they keys will be added on runtime.
        But this approach will still be O(n^2)

        Since we are given constraint of time we can use a lot of space.

        Since 2 iterations is still O(n) we can iterate twice.

        Plan:

        dictionary
        minimum
        maximum

        iterate:
            find maximum and minimum
        
        loop to generate dictionary like this from minimum to maximum: {element: bool, ...}

        go through all elements again adding to dictionary.

        iterate through all dictionary saving the highest number of iterations

        We can just sort it out instead of adding to dictionary

        The code:

        minimum = 10**9
        maximum = -10**9
        maximum_iterations = 0
        iterations = 0

        for element in nums:
            if element > maximum:
                maximum = element

            if element < minimum:
                minimum = element

        for element in range(minimum, maximum+1):
            #under the hood this might actually iterate through even more if using in approach
            if element in nums:
                iterations += 1
            else:
                if iterations>maximum_iterations:
                    maximum_iterations = iterations
                iterations = 0
        
        return maximum_iterations

        test cases:
        nums = [2,20,4,10,3,4,5]

        maximum = 10
        minimum = 2
        element goes from 2 to 10 now including 10
        2,3,4,..,10


        another test case:

        nums=[0,3,2,5,4,6,1,1]

        minimum = 0
        maximum = 6
        
        0:
        iteration = 1

        1:
        iteration = 2

        2:
        iteration = 3

        3:
        iteration = 4






        checks if valuse from num is in there if so it iterates,
        storing maximum in the end.
        maximum iterations
     
     '''



        