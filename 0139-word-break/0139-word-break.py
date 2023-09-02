class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dp = [False for _ in range(len(s) + 1)]
        dp[0]= True
        
        for i in range(len(s)):
            for j in range(i, len(s)):
                if dp[i] and s[i:j+1] in wordDict:
                    dp[j+1] = True
        return dp[-1]