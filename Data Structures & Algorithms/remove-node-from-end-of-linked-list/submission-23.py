# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        counter = 1
        if not head.next:
            return None
        
        while curr.next:
            counter += 1
            curr = curr.next

        curr = head
        counter2 = 0
        
        if counter == 2:
            if n % 2 == 0:
                return curr.next
            else:
                curr.next = None
                return curr
        print(counter, n)

        if counter == n:
            return head.next


        while curr.next:
            if counter2 == (counter - (n + 1)):
                curr.next = curr.next.next
            else:
                curr = curr.next
            counter2 += 1
        
        return head
        
            
            
        
        