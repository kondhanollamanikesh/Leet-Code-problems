# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head

        # Find middle
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Split into two lists
        second = slow.next
        slow.next = None

        # Sort both halves
        first = self.sortList(head)
        second = self.sortList(second)

        # Merge
        dummy = ListNode(0)
        current = dummy

        while first and second:

            if first.val < second.val:
                current.next = first
                first = first.next
            else:
                current.next = second
                second = second.next

            current = current.next

        if first:
            current.next = first

        if second:
            current.next = second

        return dummy.next