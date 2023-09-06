class Solution:
    def jump(self, nums: list[int]) -> int:
        cnt = [0] * len(nums)
        for i in range(len(nums)):
            for j in range(1, nums[i] + 1):
                if i + j >= len(nums):
                    continue
                if cnt[i + j] == 0:
                    cnt[i + j] = cnt[i] + 1
        
        return cnt[-1]