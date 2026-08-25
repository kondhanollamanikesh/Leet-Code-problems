# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None

        if list1 is None:
            return list2

        if list2 is None:
            return list1

        temp = list1
        temp1 = list2
        res = []

        while temp and temp1:
            if temp.val <= temp1.val:
                res.append(temp.val)
                temp = temp.next
            else:
                res.append(temp1.val)
                temp1 = temp1.next

        while temp is not None:
            res.append(temp.val)     # .val
            temp = temp.next

        while temp1 is not None:
            res.append(temp1.val)    # .val
            temp1 = temp1.next

        # Convert res into Linked List
        dummy = ListNode()
        current = dummy

        for value in res:
            current.next = ListNode(value)
            current = current.next

        return dummy.next