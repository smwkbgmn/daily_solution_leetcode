class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        subary = 0
        for i in range(0, k):
            subary += nums[i]

        highest = subary
        i = 0
        j = k
        while j < len(nums):
            subary += nums[j]
            j += 1
            subary -= nums[i]
            i += 1

            if subary > highest:
                highest = subary
        
        return highest / k