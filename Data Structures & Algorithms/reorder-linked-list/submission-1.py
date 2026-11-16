# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
       def reorderList(self, head: Optional[ListNode]) -> None:
       # Step 1: Count the nodes
            count = 0
            curr = head

            while curr:
                count += 1
                curr = curr.next

            # Step 2: Find the middle
            middle = (count + 1) // 2

            # Step 3: Split into two lists
            firstList = head
            secondList = None
            curr = head
            i = 0

            while curr:
                if i == middle - 1:
                    secondList = curr.next
                    curr.next = None
                    break

                curr = curr.next
                i += 1

            # Step 4: Reverse the second list
            prev = None

            while secondList:
                temp = secondList.next
                secondList.next = prev
                prev = secondList
                secondList = temp

            # Step 5: Merge the two lists
            first = firstList

            while first and prev:
                tmp1 = first.next
                tmp2 = prev.next

                first.next = prev
                prev.next = tmp1

                first = tmp1
                prev = tmp2