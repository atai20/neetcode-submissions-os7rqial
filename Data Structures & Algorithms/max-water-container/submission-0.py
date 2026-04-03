class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        The bruteforce approach would be to manually go over every single bar 
        and compare that to the other one and store the smaller value as height then multiplying it
        to their difference in vertical distance. We can store the biggest value of them with the bars saved as well.

        The other approach will be to sort their heights and map their distances from origin to dictionary.
        We would have to then find the bars that are lowest in height difference and highest in distance
        at the same time.

        Let's just stick to bruteforce approach


        plan:
        biggest one = 0
        loop through the array
            loop through the array again:
                if value+abs(element1-element2)> biggest one and element1 index is not element2 index:
                    biggest one = value+abs(element1-element2)
        return value*abs(element1-element2)
                    



        '''

        biggest_height = 0
        for ind1 in range(len(heights)):
            for ind2 in range(len(heights)):
                if min(heights[ind1], heights[ind2])*abs(ind1-ind2)>biggest_height and ind1 != ind2:
                    biggest_height = min(heights[ind1], heights[ind2])*abs(ind1-ind2)
        return biggest_height
        