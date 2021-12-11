# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getListLength(self, head: ListNode) -> int:
        length = 0
        while head is not None:
            length += 1
            head = head.next
            
        return length
    
    def getDecimalValue(self, head: ListNode) -> int:
        result = 0
        power = self.getListLength(head) - 1
        while head is not None:
            result += head.val * (2 ** power)
            power -= 1
            head = head.next
        
        return result
        