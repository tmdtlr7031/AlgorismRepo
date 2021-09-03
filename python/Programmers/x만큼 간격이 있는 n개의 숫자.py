# x만큼 간격이 있는 n개의 숫자 (https://programmers.co.kr/learn/courses/30/lessons/12954)
# 정수 = +, 0, -
def solution(x, n):
    if x == 0:
        return [0] * n

    return [i for i in range(x, x*(n+1), x)]

# print(solution(2,5)) # [2,4,6,8,10]
print(solution(0, 1))
