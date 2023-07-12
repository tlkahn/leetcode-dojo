class Solution:
    def shortestWayA(self, source: str, target: str) -> int:
        def update(target, i, source):
            j = 0
            while i < len(target) and j < len(source):
                if target[i] == source[j]:
                    i += 1
                    j += 1
                else:
                    j += 1
            return i

        i = 0
        res = 0
        while i < len(target):
            res += 1
            t = update(target, i, source)
            if t == i:
                return -1
            i = t
        return res

    def shortestWayB(self, source, target):
        sp, tp, ans = (
            0,
            0,
            1,
        )  # sp: source pointer, tp: target pointer, ans: answer count
        sn, tn = len(source), len(target)  # sn: source length, tn: target length

        while tp < tn:
            while sp < sn and source[sp] != target[tp]:
                sp += 1  # increment sp until a matching character is found

            if sp == sn:
                sp = 0  # reset sp to the beginning of the source string
                ans += 1  # increment the answer count
                while sp < sn and source[sp] != target[tp]:
                    sp += 1  # increment sp until a matching character is found again

                if sp == sn:
                    return -1  # if no match found even after resetting sp, return -1

            sp += 1  # move sp and tp to the next characters
            tp += 1

        return ans  # return the answer count

    def shortestWayC(self, source, target):
        sp, tp, ans = 0, 0, 1
        sn, tn = len(source), len(target)

        while tp < tn:
            while sp < sn and source[sp] != target[tp]:
                sp += 1

            if sp == sn:
                sp = 0
                ans += 1
                while sp < sn and source[sp] != target[tp]:
                    sp += 1

                if sp == sn:
                    return -1

            sp += 1
            tp += 1

        return ans

    def shortestWayE(self, source: str, target: str) -> int:
        sp, ans = 0, 1  # sp: source pointer, ans: answer count
        sn, tn = len(source), len(target)
        next = [
            [-1] * 26 for _ in range(sn + 1)
        ]  # next[i][j]: next occurrence of character j after index i in the source string

        # Preprocess the next array to store the next occurrence of each character in the source string
        for i in range(sn - 1, -1, -1):
            next[sn][
                ord(source[i]) - ord("a")
            ] = i  # Store the last occurrence of each character in the last row of the next array

        # Calculate the next array for each index i in the source string
        for i in range(sn - 1, -1, -1):
            c = ord(source[i]) - ord("a")
            for j in range(26):
                if j == c:
                    next[i][
                        j
                    ] = i  # Set next[i][j] to i if character j is found at index i in the source string
                else:
                    next[i][j] = next[i + 1][
                        j
                    ]  # Set next[i][j] to next[i+1][j] if character j is not found at index i

        # Iterate through each character in the target string
        for c in target:
            c = ord(c) - ord("a")  # Convert character to 0-based index
            if next[sp][c] == -1:
                return (
                    -1
                )  # If next occurrence of character c after index sp is -1, it means c is not found in the source string
            if next[sp][c] < sp:
                ans += 1  # If next occurrence of character c is before sp, it means we need to take a new subsequence, so increment the answer count
            sp = (
                next[sp][c] + 1
            )  # Move the source pointer to the next occurrence of character c + 1

        return ans  # Return the answer count

    def shortestWayD(self, source: str, target: str) -> int:
        ans, sp = 0, 0

        while sp < len(target):
            start = sp
            for c in source:
                if sp < len(target) and target[sp] == c:
                    sp += 1
            if sp == start:
                return -1
            ans += 1

        return ans
