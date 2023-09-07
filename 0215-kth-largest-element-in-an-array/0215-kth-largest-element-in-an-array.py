import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        max_heap = []
        for i in nums:
            heapq.heappush(max_heap, (-i, i))
        for _ in range(k):
            answer = heapq.heappop(max_heap)[1]
        return answer
