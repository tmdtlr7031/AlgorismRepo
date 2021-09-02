# 제일 작은 수 제거하기 (https://programmers.co.kr/learn/courses/30/lessons/12935)

'''
    작은 수가 중복이면 둘 다 제거해야할 듯.

    - in 으로 O(n), remove(..)로 O(n)이라 O(n^2) 일듯..
    def solution(arr):
    minNum = min(arr)
    while minNum in arr:
        arr.remove(minNum)
    return [-1] if len(arr) == 0 else arr
'''

def solution(arr):
    minNum = min(arr)
    result = [i for i in arr if i != minNum] # 최소값과 다른 값만 따로 리스트 만들기
    return result or [-1] # result가 빈 리스트 일 때 -1


print(solution([4,3,2,1])) # [4,3,2]
# print(solution([10])) # [-1]
