class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        n_dic = {}
        for i in nums:
            n_dic[i] = n_dic.get(i,0) + 1
        n_dic = dict(sorted(n_dic.items(), key=lambda x:x[1], reverse=True))
        
        return list(n_dic.keys())[:k]