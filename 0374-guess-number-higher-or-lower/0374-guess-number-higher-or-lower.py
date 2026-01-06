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

        while check != 0:
            needle = m + (n - m) // 2
            check = guess(needle)
            if check == 1:
                m = needle + 1
            else:
                n = needle - 1

        return needle