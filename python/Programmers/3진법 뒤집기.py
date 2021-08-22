# 3진법 뒤집기
def solution(n):
    answer = ''
    result = 0

    # 3진법 -> n이 0이 될 때까지 3으로 계속 나눔
    while n > 0:
        answer += str(n % 3)
        n = n//3

    for i in range(len(answer)):
        result += (3**int(i))*int(answer[-1-i])

    return result

# print(solution(45)) # 7
print(solution(1))
print(solution(2))
# print(solution(3))

'''
    다른 풀이
    - int 이용
        - int('0021', 3) == 7
        - 첫번째를 두번째 진법을 기준으로 구했을 때의 값

    def solution(n):
        tmp = ''
        while n:
            tmp += str(n % 3)
            n = n // 3

        answer = int(tmp, 3)
        return answer
'''
