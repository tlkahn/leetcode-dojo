from common import *


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergetwo(
            a: Optional[ListNode],
            b: Optional[ListNode],
            start: Optional[ListNode] = None,
        ) -> Optional[ListNode]:
            if not a and not b:
                return None
            if not b:
                return a
            if not a:
                return b

            if b.val <= a.val:
                new_head_a = b
                b = b.next
                new_head_a.next = a
                a = new_head_a
                return mergetwo(a, b)

            if start:
                prev = cur = start
            else:
                prev = cur = a
            while cur.val < b.val:
                prev = cur
                if cur.next:
                    cur = cur.next
                else:
                    cur.next = b
                    return a
            new_node = b
            b = b.next
            new_node.next = cur
            prev.next = new_node
            return mergetwo(a, b, new_node)

        if not lists:
            return None

        if len(lists) == 1:
            return lists[0]

        res = lists[0]
        for el in lists[1:]:
            res = mergetwo(res, el)

        return res


class SolutionB:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwo(
            a: Optional[ListNode], b: Optional[ListNode]
        ) -> Optional[ListNode]:
            if not a or not b:
                return a or b

            if b.val < a.val:
                b.next = mergeTwo(a, b.next)
                return b
            else:
                a.next = mergeTwo(a.next, b)
                return a

        if not lists:
            return None

        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                if i + 1 < len(lists):
                    merged.append(mergeTwo(lists[i], lists[i + 1]))
                else:
                    merged.append(lists[i])
            lists = merged

        return lists[0]


class SolutionC:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        heap = [(l.val, i, l) for i, l in enumerate(lists) if l]
        heapq.heapify(heap)

        while heap:
            _, idx, node = heapq.heappop(heap)
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(heap, (node.next.val, idx, node.next))

        return dummy.next


class SolutionD:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwo(
            a: Optional[ListNode], b: Optional[ListNode]
        ) -> Optional[ListNode]:
            if not a or not b:
                return a or b

            if a.val <= b.val:
                a.next = mergeTwo(a.next, b)
                return a
            else:
                b.next = mergeTwo(a, b.next)
                return b

        if not lists:
            return None

        if len(lists) == 1:
            return lists[0]

        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])

        return mergeTwo(left, right)
