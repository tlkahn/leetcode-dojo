from common import *

from collections import deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        arr = []
        p = head
        while p:
            arr.append(p.val)
            p = p.next

        N = len(arr)
        A = deque(range(N))
        B = deque(range(N - 1, -1, -1))
        p = head
        while p and A and B:
            a = A.popleft()
            b = B.popleft()
            if a < b:
                p.val = arr[a]
                p.next.val = arr[b]
                p = p.next.next
            elif a == b:
                p.val = arr[a]
                break
            else:
                break


class SolutionE:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        nodes = []
        p = head
        while p:
            nodes.append(p)
            p = p.next

        left, right = 0, len(nodes) - 1
        while left < right:
            nodes[left].next = nodes[right]
            left += 1
            if left == right:
                break
            nodes[right].next = nodes[left]
            right -= 1

        nodes[left].next = None


class SolutionD:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        arr = []
        p = head
        while p:
            arr.append(p.val)
            p = p.next

        left, right = 0, len(arr) - 1
        p = ListNode(0, head)
        while left <= right:
            if left == right:
                p.next.val = arr[left]
                break
            p.next.val = arr[left]
            p = p.next
            p.next.val = arr[right]
            p = p.next
            left += 1
            right -= 1


class SolutionB:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # Split the list into two halves
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_half = slow.next
        slow.next = None

        # Reverse the second half
        prev, curr = None, second_half
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        second_half = prev

        # Merge the two halves
        p1, p2 = head, second_half
        while p2:
            next_p1, next_p2 = p1.next, p2.next
            p1.next = p2
            p2.next = next_p1
            p1 = next_p1
            p2 = next_p2


class SolutionC:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # Split the list into two halves
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second_half, slow.next = slow.next, None

        # Reverse the second half
        prev, curr = None, second_half
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        second_half = prev

        # Merge the two halves
        p1, p2 = head, second_half
        while p2:
            p1.next, p2.next, p1, p2 = p2, p1.next, p1.next, p2.next
