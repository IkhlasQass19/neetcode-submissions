# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sizeOfList = 0
        current = head

        # Calculate the size of the list
        while current:
            sizeOfList += 1
            current = current.next

        removeElement = sizeOfList - n

        # Remove the first node
        if removeElement == 0:
            return head.next

        index = 0
        current = head

        while current:
            if index + 1 == removeElement:
                current.next = current.next.next
                break

            index += 1
            current = current.next

        return head