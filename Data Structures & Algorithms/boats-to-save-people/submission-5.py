class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        '''
        idea:
        sort array first
        have two pivots on start and finish
        move them both toward the center until they meet
        move them when match was found

        edge case:
        the limit itself is on the right
        '''
        boats_number = 0
        sorted_people = sorted(people)

        left = 0
        right = len(sorted_people) - 1

        while left < right:
       

            if sorted_people[right] == limit:
                right -= 1
                boats_number += 1

            if sorted_people[right] + sorted_people[left] <= limit:
                boats_number += 1
                left += 1
                right -= 1
            else:
                boats_number += 1
                right -= 1
        
        
        
        return boats_number + len(people[left:right+1])