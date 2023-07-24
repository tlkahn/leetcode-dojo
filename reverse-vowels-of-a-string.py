class SolutionA:
    def reverseVowels(self, s: str) -> str:
        vowels = ["a", "e", "i", "o", "u"]
        vowels += [v.upper() for v in vowels]
        # vowel chars with index
        vci = [(char, i) for i, char in enumerate(s) if char in vowels]
        vcj = [(char, j) for (char, _), (_, j) in zip(vci, reversed(vci))]
        ss = list(s)
        for char, j in vcj:
            ss[j] = char
        return "".join(ss)


class SolutionB:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        ss = list(s)
        i, j = 0, len(s) - 1

        while i < j:
            if ss[i] in vowels and ss[j] in vowels:
                ss[i], ss[j] = ss[j], ss[i]
                i += 1
                j -= 1
            elif ss[i] not in vowels:
                i += 1
            elif ss[j] not in vowels:
                j -= 1

        return "".join(ss)
