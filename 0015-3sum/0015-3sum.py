class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        answer = []
        nums.sort()
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                
                if s > 0:
                    right -= 1
                elif s < 0:
                    left += 1
                else:
                    answer.append([nums[i], nums[left], nums[right]])
                    
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
            
        return answer