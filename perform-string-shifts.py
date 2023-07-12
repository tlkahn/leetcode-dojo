from typing import List


class Solution:
    def stringShiftA(self, s: str, shift: List[List[int]]) -> str:
        def shift_left(n):
            nonlocal s
            n = n % len(s)
            return s[n:] + s[:n]

        def shift_right(n):
            nonlocal s
            n = n % len(s)
            return s[-n:] + s[:-n]

        total = [0, 0]
        for left, right in shift:
            total[0] += left
            total[1] += right
        shift_left_n = total[0] - total[1]
        if shift_left_n > 0:
            return shift_left(shift_left_n)
        elif shift_left_n < 0:
            return shift_right(-shift_left_n)
        else:
            return s

    def stringShiftB(self, s: str, shift: List[List[int]]) -> str:
        total = sum(left - right for left, right in shift) % len(s)
        return s[-total:] + s[:-total] if total else s

    def stringShiftC(self, s: str, shift: List[List[int]]) -> str:
        n = len(s)
        left_shift = 0
        for direction, dist in shift:
            if direction == 0:
                left_shift += dist
            else:
                left_shift -= dist
        left_shift %= n
        if left_shift == 0:
            return s
        return s[left_shift:] + s[:left_shift]

    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        n = len(s)
        left_shift = (
            sum(dist if direction == 0 else -dist for direction, dist in shift) % n
        )
        return s[left_shift:] + s[:left_shift] if left_shift else s
