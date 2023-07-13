from itertools import product
from typing import Union, List


class Solution:
    def expandA(self, s: str) -> List[str]:
        """
        You are given a string s representing a list of words. Each letter in
        the word has one or more options.

        If there is one option, the letter is represented as is.
        If there is more than one option, then curly braces delimit the
        options. For example, "{a,b,c}" represents options ["a", "b", "c"].
        For example, if s = "a{b,c}", the first character is always 'a', but
        the second character can be 'b' or 'c'. The original list is ["ab",
        "ac"].

        Return all words that can be formed in this manner, sorted in
        lexicographical order.
        """
        counting = False
        opt = []
        res: list[Union[list, str]] = []
        for c in s:
            if c == "{":
                counting = True
            elif c == "}":
                counting = False
                res.append(opt)
                opt = []
            elif c == ",":
                continue
            elif counting:
                opt.append(c)
            else:
                res.append(c)
        return sorted(["".join(p) for p in product(*res)])
