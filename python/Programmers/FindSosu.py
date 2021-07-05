'''
    차이점 정리
    - combinations : 순서 상관 X
        ex. [1,2]인 경우 combinations([1,2],2) 결과값 : (1,2)
    - permutations : 순서 상관 O
        ex. [1,2]인 경우 permutations([1,2],2) 결과값 : (1,2), (2,1)
    - product : 복수개 사이의 카디션 프로덕트
'''
# 미완

from itertools import permutations

def decimalYn(target):
    for j in range(2,target):
        if target % j == 0:
            return False
    return True


# 소수 찾기
def solution(numbers):
    answer = 0
    # 한 자리 수는 따로 추가
    makeData = set(list(map(lambda x : int("".join(x)), permutations(numbers,len(numbers)))) + list(map(int, numbers)))
    print("makeData : ",makeData)
    # 소수 판별
    for i in makeData:
        if i <= 1:
            continue
        else:
            if decimalYn(i):
                answer+=1
    return answer

# print(solution("17"))
print(solution("011"))
print(solution("0110"))
print(solution("7843")) # 12 나와야함

# inputs = "17"
# data = list(map(lambda x : int("".join(x)), permutations(inputs,2))) + list(map(int, inputs))
# print(data)
n = 25 
for i in range(1, int(n**0.5)):
    if n % i == 0:
        print(i, end=" ")
        print(n//i, end=" ") 

i += 1 
if i**2 == n:
    print(i)

