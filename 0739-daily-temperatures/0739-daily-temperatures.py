class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answer = [0] * len(temperatures)
        temp = []
        
        for idx, t in enumerate(temperatures):
            while temp and  t > temperatures[temp[-1]]:
                last = temp.pop()
                answer[last] = idx - last
            temp.append(idx)
                
        return answer