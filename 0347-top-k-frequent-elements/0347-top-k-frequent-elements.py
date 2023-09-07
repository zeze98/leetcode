import heapq
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        n_dic = {}
        for i in nums:
            n_dic[i] = n_dic.get(i,0) + 1
        hq = []
        for j in n_dic.keys():
            heapq.heappush(hq, (-n_dic[j], j))
        
        answer = []
        for _ in range(k):
            answer.append(heapq.heappop(hq)[1])
        return answer