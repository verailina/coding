# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        heads = [None, None]
        currents = [None, None]
        
        i = 0
        
        current = head
        while current is not None:
            rest = current.next
            current.next = None
            index = i % 2
            if heads[index] is None:
                heads[index] = current
                currents[index] = current
            else:
                currents[index].next = current
                currents[index] = current
            current = rest
            i += 1
                
        currents[0].next = heads[1]
        return heads[0]
        
                
                
        
        

            
        
        
                
        