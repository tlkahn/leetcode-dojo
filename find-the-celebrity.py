def knows(a: int, b: int) -> bool:
    return True


class SolutionA:
    def findCelebrity(self, n: int) -> int:
        result = 0
        for i in range(1, n):
            if knows(result, i):
                result = i
        if any(
            knows(result, i) or not knows(i, result) for i in range(n) if i != result
        ):
            return -1
        return result


class SolutionB:
    def findCelebrity(self, n: int) -> int:
        """
        This code is written in C++ and is used to find a celebrity in
        a party of n people.
        The findCelebrity function takes the number of people as input
        and returns the index of the celebrity.
        The variable 'result' is initialized as 0, assuming the first
        person is the celebrity.
        The first loop iterates from 1 to n-1 and checks if the
        current person knows the 'result' person.
        If yes, it updates the 'result' variable to the current
        person.
        The second loop iterates from 0 to n-1 and checks for two conditions:
        - If 'result' is equal to the current person, it continues to
          the next iteration.
        - If 'result' knows the current person or the current person
          doesn't know 'result', it returns -1 (no celebrity found).
        If the loops complete without returning -1, it means the
        'result' person is the celebrity and its index is returned.
        """
        result = 0
        for i in range(1, n):
            if knows(result, i):
                result = i
        for i in range(n):
            if result == i:
                continue
            if knows(result, i) or not knows(i, result):
                return -1
        return result


class SolutionC:
    def findCelebrity(self, n: int) -> int:
        left = 0
        right = n - 1

        # Eliminate candidates who are not celebrities
        while left < right:
            if knows(left, right):
                left += 1
            else:
                right -= 1

        # Check if the potential celebrity satisfies the conditions
        for i in range(n):
            # If 'left' knows any other person or any other person doesn't know 'left', 'left' is not a celebrity
            if (i != left and knows(left, i)) or (i != left and not knows(i, left)):
                return -1

        return left  # 'left' is the celebrity
