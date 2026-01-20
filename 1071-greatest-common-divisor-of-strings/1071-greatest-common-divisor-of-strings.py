class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Filter first if it has a common divider
        if str1 + str2 != str2 + str1:
            return ""

        # Euclid gcd - looping instead of recurssion (just preference)
        def gcd(n, m):
            while m:
                n, m = m, n % m
            return n
        
        # Return the longest common divider 
        return str1[:gcd(len(str1), len(str2))]
            