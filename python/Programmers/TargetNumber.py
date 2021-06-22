# 타겟넘버
'''
    접근 방법
    1) 기존 '소수 만들기'에서 사용했던 combinations 에서 착안해 카디션프로덕트가 가능한 itertools의 product 이용
    2) 제시된 리스트의 요소마다 -1,1을 곱한 값을 별도의 list로 만들고 ex) [1,1,1] => [[-1,1],[-1,1],[-1,1]]
    3) 카디션프로덕트 진행
'''
from itertools import product
def solution(numbers, target):
    # data = [[1,1,1,1,1],[-1,-1,-1,-1,-1], [1,1,1,1,1]] 하면 [1,-1,1] 이런 식으로 나옴
    makeList = list()
    for i in numbers:
        makeList.append([i,i*-1])

    answer = 0
    for i in list(product(*makeList)):
        if sum(i) == target:
            answer += 1
            
    return answer

print(solution([1,1,1,1,1], 3))

'''
    리펙토링 된 모범 소스 (완전탐색)

    from itertools import product
    def solution(numbers, target):
        l = [(x, -x) for x in numbers]
        s = list(map(sum, product(*l)))
        return s.count(target)

    1) append하는 부분이 한줄코딩 되었다.
    2) -1 곱하지 않고 그냥 붙였다
    3) map 함수 이용
        - 리스트의 요소를 지정된 함수로 처리한다.
        - map의 리턴 값은 map object이므로 list나 tupel같은 다른 타입으로 바꿔서 사용하자.
    4) count(찾을값) 을 통해 += 사용 안함.
    5) 참고
        - 모범 답안 모음 : https://eda-ai-lab.tistory.com/475
        - DFS(깊이우선탐색), BFS(너비우선탐색) : https://devuna.tistory.com/32

    + 재귀 시 실행되는 순서 주의

    def countdown(n):
        if n == 0:
            print("Blastoff!")
        else:
            print(n)
            countdown(n-1)
            print('==================',n)        
    countdown(3)

    [ 결과 ]
    3 -> 2 -> 1 -> Blastoff! -> ================== 1 -> ================== 2 -> ================== 3
'''
