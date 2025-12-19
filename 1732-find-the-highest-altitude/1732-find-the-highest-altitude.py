class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = 0
        for i, n in enumerate(gain):
            if n > highest:
                highest = n
            if i + 1 < len(gain):
                gain[i + 1] += n    
        
        return highest
        