class Limits:
    def __init__(self, left, right):
        self.left = left
        self.right = right


def get_next(s):
    next = [-1] * (len(s) + 1)
    j = 0
    k = -1
    while j < len(s):
        if k == -1 or s[j] == s[k]:
            j += 1
            k += 1
            next[j] = k
        else:
            k = next[k]
    return next


def index_kmp(s, t, begin, end, pos):
    next = get_next(t)
    i = pos
    j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            j = next[j]
        if j < 0:
            i += 1
            j += 1
    if j == len(t):
        begin[0] = i - len(t)
        end[0] = i - 1
        return True
    return False


def radix_sort(nums):
    count = [0] * 1000
    pos = [[] for _ in range(1000)]

    for num in nums:
        pos[num.left].append(num)
        count[num.left] += 1

    result = []
    for i in range(1000):
        for j in range(count[i]):
            result.append(pos[i][j])

    return result


def merge_limits(bounds):
    bounds.sort(key=lambda x: x.left)
    merged = []
    i = 0
    while i < len(bounds):
        left = bounds[i].left
        right = bounds[i].right
        while i + 1 < len(bounds) and bounds[i + 1].left <= right + 1:
            right = max(right, bounds[i + 1].right)
            i += 1
        merged.append(Limits(left, right))
        i += 1
    return merged


def add_bold_tag(s, dict):
    if not dict:
        return s
    bounds = []
    for word in dict:
        pos = 0
        while True:
            begin = [0]
            end = [0]
            if not index_kmp(s, word, begin, end, pos):
                break
            bounds.append(Limits(begin[0], end[0]))
            pos = begin[0] + 1
            while pos < len(s) and s[pos] != s[begin[0]]:
                pos += 1

    bounds = merge_limits(bounds)
    bounds.sort(key=lambda x: x.left)

    result = ""
    i = 0
    for j in range(len(s)):
        if i < len(bounds) and j == bounds[i].left:
            result += "<b>"
        result += s[j]
        if i < len(bounds) and j == bounds[i].right:
            result += "</b>"
            i += 1

    return result
