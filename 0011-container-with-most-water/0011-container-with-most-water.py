class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        answer = 0
        while right - left > 0:
            answer = max(answer, (right - left) * min(height[left], height[right]))
            
            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1
        return answer