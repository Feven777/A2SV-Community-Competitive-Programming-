# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        tail=dummy=ListNode()
        i=list1
        j=list2
        while i and j:
            if i.val<=j.val:
                tail.next=i
                i=i.next
            else:
                tail.next=j
                j=j.next
            tail=tail.next
        if i:
            tail.next=i
        if j:
            tail.next=j
        return dummy.next
        