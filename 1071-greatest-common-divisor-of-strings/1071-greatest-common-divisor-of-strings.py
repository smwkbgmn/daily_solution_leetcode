class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        (lng, shrt) = (str1, str2) if len(str1) > len(str2) else (str2, str1)

        gcd = shrt
        for i in range(len(shrt)):
            if len(lng) % len(gcd) != 0 or len(shrt) % len(gcd) != 0:
                gcd = gcd[:-1]
                continue

            j = 0
            while j < len(lng) and lng[j] == gcd[j % len(gcd)]:
                if j < len(shrt) and shrt[j] != gcd[j % len(gcd)]:
                    break
                j += 1
            
            if j == len(lng) and j % len(gcd) == 0:
                break

            gcd = gcd[:-1]
        
        return gcd
            