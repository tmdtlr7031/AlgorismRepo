# 나누어 떨어지는 숫자 배열 https://programmers.co.kr/learn/courses/30/lessons/12910
def solution(arr, divisor):
    answer = []
    arr.sort()
    for i in arr:
        if i % divisor == 0:
            answer.append(i)

    return [-1] if len(answer) == 0 else answer

print(solution([5,9,7,10], 5)) # [5,10] 
print(solution([3,2,6], 5))  # [-1]
print(solution([2, 36, 1, 3], 1))  # [1, 2, 3, 36]

'''
    sorted([n for n in arr if n%divisor == 0]) or [-1]
    - 앞에 것이 거짓일때 or 뒤에 것이 호출됨
'''
