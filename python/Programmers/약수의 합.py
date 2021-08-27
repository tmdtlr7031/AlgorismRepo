# 약수의 합 (https://programmers.co.kr/learn/courses/30/lessons/12928)
def solution(n):
    answer = set() # 1,3,9 경우 3일때 3*3=9 이므로 3이 중복으로 들어가는거 방지

    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            answer.add(n//i)
            answer.add(i)
    return sum(answer)

# 개선..
# 12 + 약수들의 합 (=> 소수처럼 제곱근 까지만 탐색하면 됨)
def solution2(n):
    return n + sum([i for i in range(1, int(n**0.5)+1) if n % i == 0])

'''
    def sumDivisor(num):
        return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])
'''
# print(solution(12)) # 28
# print(solution(5)) # 6
print(solution(9)) # 13

