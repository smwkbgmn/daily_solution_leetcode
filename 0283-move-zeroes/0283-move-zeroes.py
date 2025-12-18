class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        def swap():
            nums[i], nums[j] = nums[j], nums[i]
        
        i = 0
        while i < len(nums):
            if nums[i] != 0:
                i += 1
            else:
                break

        j = i + 1
        while j < len(nums):
            if nums[j] != 0:
                swap()
                i += 1
            j += 1
        