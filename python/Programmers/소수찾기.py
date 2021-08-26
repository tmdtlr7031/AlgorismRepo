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
        num=set(range(2,n+1))

        for i in range(2,n+1):
            if i in num:
                num-=set(range(2*i,n+1,i))
        return len(num)
'''

print(20**0.5)

num = set(range(2, 21))
print(num)

for i in range(2, int(20**0.5)+1):
    if i in num:
        num -= set(range(i*i, 20+1, i))
print(num)
