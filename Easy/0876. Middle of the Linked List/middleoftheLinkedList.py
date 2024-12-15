# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lenList = 1
        node = head
        while (node.next != None):
            lenList += 1
            node = node.next
        middle = lenList // 2 + 1
        node = head
        while (middle != 1):
            node = node.next
            middle -= 1
        return node