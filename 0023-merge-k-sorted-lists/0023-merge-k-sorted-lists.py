# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        if not lists:
            return None

        while len(lists) > 1:
            merged = []

            for i in range(0, len(lists), 2):

                list1 = lists[i]

                if i + 1 < len(lists):
                    list2 = lists[i + 1]
                else:
                    list2 = None

                merged.append(self.merge(list1, list2))

            lists = merged

        return lists[0]

    def merge(self, list1, list2):

        dummy = ListNode(0)
        current = dummy

        while list1 and list2:

            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        if list1:
            current.next = list1

        if list2:
            current.next = list2

        return dummy.next
