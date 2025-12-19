class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        subary = sum(nums[:k])
        highest = subary
        
        i = 0
        j = k
        while j < len(nums):
            subary -= nums[i]
            i += 1
            subary += nums[j]
            j += 1

            if subary > highest:
                highest = subary
        
        return highest / k