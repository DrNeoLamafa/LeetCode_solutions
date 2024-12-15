class Solution:
    def romanToInt(self, s: str) -> int:
        romanNums = {"I" : 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total, current, previuos = 0, 0, 0
        for ch in s[::-1]:
            previous = current
            current = romanNums[ch]
            if current >= previous:
                total += current
            else:
                total -= current
        return total