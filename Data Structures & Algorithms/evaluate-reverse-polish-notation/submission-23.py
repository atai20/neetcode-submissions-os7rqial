class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        

        '''
        do second one, do the dict about operations


        Plan:

        continue adding numbers to stack

        when it becomes an operation start the operations

        stack[4]

        cycle i:

        add to stack current

        stack = [6]

        tokens=["4","13","5","/","+"]

        if current's next opp:

            stack[-2] op stack[-1] = total

            stack.pop.pop

            stack append total


        else:

            stack append current's next


        


        '''
        stack1 = [int(tokens[0])]
        ops = set("+-/*")
        res = 0
        for i in range(1, len(tokens)):
            print(stack1, tokens[i])
            if tokens[i] in ops:
                first = int(stack1[-2])
                second = int(stack1[-1])
                if second != 0:
                    last = first/second
                else:
                    last = 0
                
                dict1 = {"+":first+second, "-":first-second, "*":first*second, "/":last}
                
                stack1.pop()
                stack1.pop()
                res = dict1[tokens[i]]
                stack1.append(res)
            else:
                stack1.append(int(tokens[i]))
        print(stack1)
            
        return int(stack1[-1])



