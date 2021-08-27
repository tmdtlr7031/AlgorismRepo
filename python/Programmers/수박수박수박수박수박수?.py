# 수박수박수박수박수박수? (https://programmers.co.kr/learn/courses/30/lessons/12922)
'''
    이렇게해도되거..
        s = "수박" * n
        return s[:n]
'''
def solution(n):
    return '수박'[:n] if n < 3 else '수박'*(n//2)+'수박'[:n % 2]

print(solution(3))  # '수박수'
print(solution(4))  # '수박수박'

