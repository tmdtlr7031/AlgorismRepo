# 소수만들기
from itertools import combinations

def  check(tot):
    for j in range(2,tot):
        if tot % j == 0:
            return False
    return True

def solution(nums):
    answer = 0
    target = list(combinations(nums, 3))
    print(target)
    for i in target:
        if check(sum(i)):
            answer += 1
    return answer

print(solution([1,2,3,4]))