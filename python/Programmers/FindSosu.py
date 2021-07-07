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
import math

# 소수 판별
# 제곱근을 이용하여 탐색
# 소수, 약수 구하기 : 
#   https://thisblogbusy.tistory.com/entry/%EC%95%BD%EC%88%98-%EA%B5%AC%ED%95%98%EA%B8%B0
#   https://velog.io/@jimmyjoo/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%86%8C%EC%88%98-%EC%B0%BE%EA%B8%B0


# 소수 찾기

'''
    내 접근
    : 모든경우의 수 구하고, 한 자리 수는 따로 추가해줬음.. 잘못된 부분 발견
    : permutations(numbers,len(numbers)))) 으로 했기때문에 3자리인경우 2자리수 조합은 탐색을 안함. (3자리, 한자리만 set에 담김..!)
    
    def solution(numbers):
        # 한 자리 수는 따로 추가
        makeData = set(list(map(lambda x : int("".join(x)), permutations(numbers,len(numbers)))) + list(map(int, numbers)))
        makeData.discard(1)
        makeData.discard(0)
        print("makeData : ",makeData)
        
        useIter = makeData.copy()

        for i in useIter:
            if i <= 1:
                continue
            else:
                for j in range(2, int(math.sqrt(i))+1):
                    for k in range(j*j, i+1, j):
                        makeData.discard(k)
        return len(makeData)
'''

def check(num):
    roop = int(math.sqrt(num))
    # 0, 1은 소수 카운트에서 뺌
    if num < 2:
        return False
    # 제곱근한게 5.2131면 int()하면 5니까 +1해줘서 5까지 돌게
    for k in range(2, roop+1):
        if num % k == 0:
            return False
    return True

def solution(numbers):
    answer = set()
    # 길이가 1이상임
    for i in range(1, len(numbers)+1):
        makeData = set(list(map(lambda x : int("".join(x)), permutations(numbers,i))))
        print("makeData : ",makeData)

        for j in makeData:
            if check(j):
                answer.add(j)
    print("final answer : ",answer)
    return len(answer)

# print(solution("17"))
# print(solution("011"))
# print(solution("0110"))
print(solution("7843")) # 12 나와야함