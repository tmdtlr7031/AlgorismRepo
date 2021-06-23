# 더 맵게

'''
    접근
    1) 리스트 내 요소의 정렬이 보장되지 않아 정렬
    2) 재귀로 0,1만 계산 후 최소값 <= 기준값 후 +1씩 처리 
    
    결과
        - 57% 정답률, 효율성 0 --> 런타임에러와 시간초과
    
    sort가 두번씩 이뤄짐 + 꼭 재귀를 써야하나.. 반성
'''
# answer = 1
# def calculate(arrays, remains, num):
#     global answer
#     calcList = [arrays[0]+(arrays[1]*2)]+remains
#     if min(calcList) <= num:
#         answer += 1
#         calcList.sort()
#         calculate(calcList[:2], calcList[2:], num)
#     else:
#         return

# def solution(scoville, K):
#     global answer
#     scoville.sort()
#     calculate(scoville[:2],scoville[2:], K)

#     if answer == 0:
#         return -1
        
#     return answer

# =======================================================================

'''
    조사 (https://liveyourit.tistory.com/191)
        - 자료구조 : 힙 이용이 필요
            - 힙: 최대힘=> 모든 부모 노드 값이 자식노드 값보다 크거나 같은 이진트리
            - 이를 이용한 "우선순위큐"(가장 우선순위가 높은 값이 먼저 꺼내지는 자료구조)
            - 파이썬에선 heapq 모듈 제공

'''
import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) # 리스트 -> 힙으로 변경

    while True:
        # 힙의 [0]는 정렬이 안 되어 있어도 최소값
        # scoville는 최소 2게 이상
        if len(scoville) == 1 and scoville[0] < K: # 다 돌았는데 안넘는경우
            return -1
        if scoville[0] >= K: # 제시된 값 보다 큰 경우
            return answer

        calcData = heapq.heappop(scoville) + (heapq.heappop(scoville)*2)
        heapq.heappush(scoville, calcData)
        answer+=1

# print(solution([1,2,3,9,10,12], 7))
print(solution([6,7], 6))