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
        result += list(search.items()) # 이렇게 하면  [3,2] + [2,1] 이 됨. 하지만 location이 1의 위치를 찾는거였으면 예외상황

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
# def solution(priorities, location):



print(solution([1,2,3,2],1)) # 1
# print(solution([1, 1, 9, 1, 1, 1], 0)) # 5
# print(solution([4,1,4,3], 3))
