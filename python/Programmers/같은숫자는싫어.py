# 같은 숫자는 싫어 https://programmers.co.kr/learn/courses/30/lessons/12906
# 해당값이 이전값이랑 다를때만 추가
def solution(arr):
    answer = [arr[0]]

    for i in range(1,len(arr)):
        if arr[i] == answer[-1]:
            continue
        else:
            answer.append(arr[i])

    return answer

print(solution([1,1,3,3,0,1,1])) # [1,3,0,1]
print(solution([4,4,4,3,3])) # [4,3]
