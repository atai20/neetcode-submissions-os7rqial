# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        arr1 = []

        if q:
            qu = deque([q])
            arr1.append(q.val)
            while qu:
                curr = qu.popleft()
                if not curr:
                    break
                
                if curr.left:
                    qu.append(curr.left)
                    arr1.append(curr.left.val)
                else:
                    arr1.append(101)
                if curr.right:
                    qu.append(curr.right)
                    arr1.append(curr.right.val)
                else:
                    arr1.append(101)
        
        arr2 = []
        if p:
            qu = deque([p])
            arr2.append(p.val)
            while qu:
                curr = qu.popleft()
                if not curr:
                    break
                
                if curr.left:
                    qu.append(curr.left)
                    arr2.append(curr.left.val)
                else:
                    arr2.append(101)
                if curr.right:
                    qu.append(curr.right)
                    arr2.append(curr.right.val)
                else:
                    arr2.append(101)
        print(arr1, arr2)
        return arr1 == arr2
        