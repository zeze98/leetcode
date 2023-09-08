class Solution:
    def decodeString(self, s: str) -> str:
        answer = ''
        n = 0
        temp = []
        for i in s:
            if i.isdigit():
                n = n * 10 + int(i)
            elif i == '[':
                temp.append(answer)
                temp.append(n)
                answer = ''
                n = 0
            elif i.isalpha():
                answer += i
            elif i == ']':
                p_n = temp.pop()
                p_s = temp.pop()
                answer = p_s + p_n*answer
        return answer