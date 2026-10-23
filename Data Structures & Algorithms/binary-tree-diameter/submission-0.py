# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        maybe doing dfikstra's from each leaf but finding the longest instead


        Maybe doing bfs

        I don't think we use bfs because it will require too much to find each node's distance to the other, maybe 

        maybe still mapping each's distance to the root

        but when get there you 

        '''
        self.res = 0

        def go_places(node):

            if not node:
                return 0

            r = go_places(node.left)
            l = go_places(node.right)
            
            
            self.res = max(self.res, l + r)
            return 1 + max(l, r)

            '''
            has to get back up:
            '''

        go_places(root)

        return self.res

        