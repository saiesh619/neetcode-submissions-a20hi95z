# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next




class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = head        
        prev = None
        temp = head
        while start:
            temp = start.next
            start.next = prev
            prev = start
            start = temp
        head = prev
        return head



            
