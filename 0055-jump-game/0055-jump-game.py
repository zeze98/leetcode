class Solution:
    def canJump(self, nums: list[int]) -> bool:
        visit = [True] * len(nums)

        def dfs(now_idx):
            visit[now_idx] = False
            if now_idx == len(nums) -1:
                return True
            can_jump = nums[now_idx]
            for i in range(1, can_jump + 1):
                if visit[now_idx + i]: 
                    if dfs(now_idx + i):
                        return True
            return False
        return dfs(0)