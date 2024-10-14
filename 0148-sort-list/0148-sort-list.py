# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        if not head or not head.next:
            return head
        left=head
        right=self.mid(head)
        tmp=right.next
        right.next=None
        right=tmp
        left=self.sortList(left)
        right=self.sortList(right)
        return self.merge(left,right)
    def mid(self, head):
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow
    def merge(self,left,right):
        tail=dummy=ListNode()
        while left and right:
            if left.val<right.val:
                tail.next=left
                left=left.next
            else:
                tail.next=right
                right=right.next
            tail=tail.next
        if left:
            tail.next=left
        if right:
            tail.next=right
        return dummy.next
        
            