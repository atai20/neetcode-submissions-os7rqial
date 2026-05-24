class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        '''
        we start with 1
        children left and right are sum of left and right parents

        second step is just add 1s to borders

        third step is adding ones to borders again but this time add sum of the two in the middle
        we will do it through 2pointers moving at the same tie until it gets to the end and we add them to end



        '''
        current = []
        prev = []
        result = []
        for i in range(numRows):
            if i == 0:
                current = [1]
            else:
                current.append(1)
                for i2 in range(i-1):
                    current.append(prev[i2]+prev[i2+1])
                    
                current.append(1)
                    

            result.append(current)
            prev = current
            current = []

        return result
        