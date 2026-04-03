class Solution:
    def maxArea(self, heights: List[int]) -> int:

        '''



        Plan:

        biggest_area = 0

        l = 0
        r = len(element) - 1

        while l<r:

            if biggest_area < (r-l) * min(element [l], element[r]):
                biggest_area = (r-l) * min(element [l], element[r])

            if (element [l] > element [r]):
                r -= 1
            else:
                l += 1
            
        return biggest_area

        height = [1,7,2,5,4,7,3,6]

        l = 1
        r = 6
        biggest_area = 8

        '''
        biggest_area = 0

        l = 0
        r = len(heights) - 1

        while l<r:

            if biggest_area < (r-l) * min(heights[l], heights[r]):
                biggest_area = (r-l) * min(heights[l], heights[r])

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
            
        return biggest_area


        