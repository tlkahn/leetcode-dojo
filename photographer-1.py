import re


def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
    # Write your code here
    pattern = rf"(P).{{{X-1},{Y-1}}}?(A).{{{X-1},{Y-1}}}?(B)"
    forwardres = [
        (match.start(1), match.start(2), match.start(3))
        for match in re.finditer(pattern, C)
    ]
    backwardres = [
        (match.start(1), match.start(2), match.start(3))
        for match in re.finditer(pattern, C[::-1])
    ]
    print(forwardres)
    print(backwardres)
    return len(set(forwardres + backwardres))


N = 8
C = ".PBAAP.B"
X = 1
Y = 3

print(getArtisticPhotographCount(N, C, X, Y))
