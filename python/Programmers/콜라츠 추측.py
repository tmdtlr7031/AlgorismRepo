# 콜라츠 추측 (https://programmers.co.kr/learn/courses/30/lessons/12943)
def solution(num):
    cnt = 0
    while num != 1:
        # 500이면 -1
        if cnt == 500:
            return -1
        
        # 짝수 홀수 판단
        if num % 2 == 0:
            num = num // 2
        else:
            num = num*3+1
        cnt += 1    

    return cnt

print(solution(6)) # 8
