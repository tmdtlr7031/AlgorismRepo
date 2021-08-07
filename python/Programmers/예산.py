# 예산 (https://programmers.co.kr/learn/courses/30/lessons/12982)
# 1135 ~1230

'''
    처음에는 모든 조합을 찾아서 budget에 있는지 확인하려했지만 
    예외가 많았다 ([1],4 인 경우, 결과값은 1이 안나오는 등..) 그리고 시간초과가 발생

    -> 간단하게 작은수부터 budget에서 빼면서 음수가 되면 리턴하면 되지않을까? 어차피 예산도 요청한거랑 딱맞춰주고 남은 잔여 예산은 어디에도 쓸모가 없다. (예산이 8이라면 1,2,3 =>6 1,4,2=>7 어차피 3이 리턴)

    -> 정렬했으니 deque까지 쓸 필요는 없을듯.. 그냥 for문이나 돌리자
    import collections
    def solution(d, budget):
        d.sort()
        data = collections.deque(d)

        answer = 0
        while data:
            num = data.popleft()
            budget -= num
            if budget >= 0:
                answer += 1
            else:
                break
    return answer
'''

def solution(d, budget):
    answer = 0
    d.sort()
    for i in d:
        budget -= i
        if budget < 0:
            break
        answer += 1
    return answer

print(solution([1,3,2,5,4], 9)) # 3
print(solution([2,2,3,3], 10)) # 4
print(solution([1,2], 1)) # 1
print(solution([1], 45)) # 1
print(solution([5], 1)) # 0
