# 소수찾기 (https://programmers.co.kr/learn/courses/30/lessons/12921)
'''
    에라토스테네스의 체 이용해야함.
    - 배수지우기
'''
def solution(n):
    initArr = [1] * (n+1) # j의 index랑 맞추기 위해 (*10 하면 0~9까지니까 0~10까지 맞춰준 것)
    initArr[0], initArr[1] = 0,0 # 0,1은 카운트에서 제외

    for i in range(2, n+1):
        if initArr[i] == 0:
            continue
        
        for j in range(i*2, n+1, i):
            if initArr[j] == 0:
                continue
            else:
                initArr[j] = 0

    return initArr.count(1)

print(solution(10))  # 4
# print(solution(5))  # 3

'''
    다른사람의 에라토스테네스의 체

    def solution(n):
        num = set(range(2, n+1)) # 2~n까지. (0,1은 제외)
        for i in range(2, int(n**0.5)+1): # n의 제곱근까지만 탐색 : 합성수는 제곱근까지만 탐색해도 된다 ex) 16 => 2*8 로 2와 8이 한 쌍이기 때문에 제곱근인 4까지만 탐색해도 대응되는 8은 지워짐
            if i in num:
                num -= set(range(i*i, n+1, i)) # n=10일때 2 탐색 시 4,6,8,10이 지워지고 3일때는 6,9가 지워지는데 이미 6은 지워졌기때문에 i^2부터 탐색하면 좀 더 개선

        return len(num)
'''