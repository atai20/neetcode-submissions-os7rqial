class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = []
        columns = [[], [], [], [], [], [],  [], [], []]
        squares = {0: {0: set(), 1: set(), 2: set()}, 1: {0: set(), 1: set(), 2: set()}, 2: {0: set(), 1: set(), 2: set()}}

        temp_l = []
        temp_s = set()

        i_s_x = 0
        i_s_y = 0

        

        for i in range(len(board)):
            digits = set(["1", "2", "3", "4", "5", "6", "7", "8", "9"])

            for i2 in range(len(board[i])):

                if board[i][i2] in digits:
                    digits.remove(board[i][i2])

                    columns[i2].append(board[i][i2])

                    if board[i][i2] in squares[i//3][i2//3]:
                        print(1)
                        return False
                    else:
                        squares[i//3][i2//3].add(board[i][i2])
                        


                elif board[i][i2] != '.':
                    print(2)
                    return False
        
   
                    
        for val in columns:
            digits = set(["1", "2", "3", "4", "5", "6", "7", "8", "9"])

            for i in val:

                if i in digits:
                    digits.remove(i)

                elif i != '.':
                    print(columns)
                    print(3)
                    return False

        return True
                
                
            
            
        
    
                
            
      





        
                
                    
                

        