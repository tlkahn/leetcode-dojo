from itertools import product
from typing import List


class Solution:
    def findStrobogrammaticA(self, n: int) -> List[str]:
        immtbl = ["0", "1", "8"]
        rvsbl = {"6": "9", "9": "6", "1": "1", "8": "8", "0": "0"}
        if n == 1:
            return immtbl
        leftn = (n - 1) // 2 if n % 2 == 1 else n // 2
        left = [p for p in (product(rvsbl.keys(), repeat=leftn)) if p[0] != "0"]
        right = [tuple([rvsbl[l] for l in el[::-1]]) for el in left]
        lr = [(l, r) for l, r in zip(left, right)]
        mid = tuple(immtbl)
        return (
            ["".join(p[0][0] + (p[1],) + p[0][1]) for p in product(lr, mid)]
            if n % 2 == 1
            else ["".join(l + r) for l, r in zip(left, right)]
        )

    def findStrobogrammaticB(self, n: int) -> List[str]:
        def helper(n: int, m: int) -> List[str]:
            # Step 1: Check if the input or state is valid
            if n < 0 or m < 0 or n > m:
                raise ValueError("Invalid input")

            # Step 2: Check if recursion should end
            if n == 0:
                return [""]
            if n == 1:
                return ["0", "1", "8"]

            # Step 3: Reduce the problem size
            lst = helper(n - 2, m)

            # Step 4: Combine the results
            res = []
            for s in lst:
                if n != m:
                    # When n=m, it indicates the outermost layer of processing.
                    # For example, if the original requirement is n=m=2, '00' is not valid.
                    # If the original requirement is n=m=4, in the inner loop n=2,m=4, '00'; in the outer loop, when n=m=4, '1001'
                    res.append("0" + s + "0")
                res.append("1" + s + "1")
                res.append("6" + s + "9")
                res.append("8" + s + "8")
                res.append("9" + s + "6")

            return res

        return helper(n, n)
