class Solution:
  def jump(self, nums: list[int]) -> int:
    ans = 0
    end = 0
    far = 0

    # Implicit BFS
    for i in range(len(nums) - 1):
      far = max(far, i + nums[i])
      if far >= len(nums) - 1:
        ans += 1
        break
      if i == end:     
        ans += 1       
        end = far  

    return ans