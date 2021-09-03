# 행렬의 덧셈 (https://programmers.co.kr/learn/courses/30/lessons/12950)
def solution(arr1, arr2):
    answer = []
    for i,v in zip(arr1,arr2): # ([1,2],[3,4]), ([2,3],[5,6]) ==> i : [1,2] v: [3,4]
        answer.append(list(map(sum, zip(i,v)))) # (1,3), (2,4)

    return answer

print(solution([[1, 2], [2, 3]], [[3, 4], [5, 6]]))  # [[4,6],[7,9]]
