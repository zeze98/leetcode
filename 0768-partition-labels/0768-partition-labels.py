class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        pos = {}
        answer = []
        for i in range(len(s)):
            pos[s[i]] = i
        
        tempMax = 0  # 더 큰 idx가 나오기 전까지 임시 저장
        start = 0
        
        # 현위치보다 마지막 등장 위치가 크면 적어도 거까진 가야해
        for i in range(len(s)):
            alpha = s[i]
            lastAppearIdx = pos[alpha]
            if i <= lastAppearIdx:
                tempMax = max(tempMax, lastAppearIdx)
                if tempMax == i:  # 임시저장했던 최고idx랑 현위치 같으면 자를수있음
                    answer.append(i+1 - start)
                    start = i + 1  # 다음 조각의 시작위치 갱신
        
        return answer