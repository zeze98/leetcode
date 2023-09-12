class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        answer = 0
        for _ in range(len(height)):
            n = min(height[left], height[right])
            m = right - left
            answer = max(answer, n * m)
            if height[left] < height[right] and left +1 < right:
                left += 1
            else:
                right -= 1
        return answer