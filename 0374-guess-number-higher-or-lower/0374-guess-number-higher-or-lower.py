# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        m = 0
        needle = 0
        check = -42

        while check != 0 and n - m != 1:
            needle = (m + n) // 2
            check = guess(needle)
            if check == 1:
                m = needle
            else:
                n = needle

        if n - m == 1:
            return m if guess(m) == 0 else n
        return needle