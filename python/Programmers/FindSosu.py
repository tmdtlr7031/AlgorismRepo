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
    : 모든경우의 수 구하고, 한 자리 수는 따로 추가해줬음.. 어디서 비는지 모르겠..
    
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
                if i % j == 0:
                    makeData.discard(i)
    return len(makeData)

# print(solution("17"))
# print(solution("011"))
# print(solution("0110"))
print(solution("7843")) # 12 나와야함

# {4738, 3, 4, 3847, 7, 4873, 8, 7438, 3478, 8473, 4378, 8347, 7834, 8734, 3487, 3874, 7843, 4387, 3748, 8743, 4783, 7348, 8374, 7483, 3784, 7384, 4837, 8437}
# {3, 37, 7, 743, 73, 487, 43, 3847, 47, 4783, 83, 347}


# {3, 3847, 7, 4783}