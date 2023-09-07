import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        max_heap = []
        for i in nums:
            heapq.heappush(max_heap, -i)
        for _ in range(k-1):
            heapq.heappop(max_heap)
        return -heapq.heappop(max_heap)