# 프린터

'''
    def solution(priorities, location):
        search = dict()
        result = []
        for idx, val in enumerate(priorities):
            search[idx] = val

        for i in range(len(priorities)):
            standard = search.pop(i)
            if standard < max(search.values()):
                search[i] = standard
            else:
                result.append((i,standard))
        result += list(search.items()) # [1,2,3,2],1 로 들어오는 경우 [3,2,1,2]가 되어 예외. [3,2,2,1]이 되어야함.

        print("result : ",result)

        for idx, val in enumerate(result):
            print(val)
            if val[0] == location:
                return idx+1
    print(solution([1,2,3,2],1)) # 1
'''

'''
    풀이법
    
'''
import collections
def solution(priorities, location):
    answer = 0
    data = collections.deque([(v, i) for i,v in enumerate(priorities)]) # i : 위치, v : 값, 튜플에서 Max하면 앞에 자리 기준으로 나오기 때문에 (v,i) 순서로 구성
    while len(data): # 0 : false, 1 : true 니까 0이 아닐 때까지 돌 것
        popData = data.popleft()
        if data and max(data)[0] > popData[0]: #  == if len(data) != 0 and max(data)[0] > popData[0] : data를 넣는 경우, [2,0,0,0,0],4 처럼 마지막까지 pop해서 max값을 할 때 빈 리스트의 경우 에러남.
            data.append(popData)
        else:
            answer += 1 # 몇번째로 인쇄되는지 카운트 (= location에 해당하는 튜플이 몇 번째 있는 지 for문 안돌리고 뽑는 것)
            if popData[1] == location:
                break
    return answer



print(solution([1,2,3,2],1)) # 3
# print(solution([1, 1, 9, 1, 1, 1], 0)) # 5
# print(solution([4,1,4,3], 3))

# test = []
# print(0 == max(test))