# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        slow=head 
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        prev=None
        while slow:
            tmp=slow.next
            slow.next=prev
            prev=slow
            slow=tmp
        while prev:
            if head.val!=prev.val:
                return False
            else:
                head=head.next
                prev=prev.next
        return True
            
        
        