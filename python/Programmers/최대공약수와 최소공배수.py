# 최대공약수와 최소공배수 (https://programmers.co.kr/learn/courses/30/lessons/12940)
'''
    유클리드 호제법?.. 기억이 안나,,
    -> 각 수의 약수 구하고 비교하는 방식으로 가보자
    -> 최대공배수 == 두 수의 곱 // 최대공약수

    def solution(n, m):
        target1 = [1,n] # 2, 5 같이 없는 소수들끼리 상황 대비 초기값
        target2 = [1,m]

        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                target1.append(i)
                target1.append(n//i)

        for i in range(2, int(m**0.5)+1):
            if m % i == 0:
                target2.append(i)
                target2.append(m//i)

        answer = 0
        for i in target1:
            if i in target2 and answer < i:
                answer = i
        return [answer, n*m if answer == 1 else m*n//answer]
'''

# 유클리드 호제법 이용
'''
    a,b의 최대공약수는 (a>b 상황)
    r = a%b 일때 

    a,b -> b,r -> r이 0일때 b가 최대공약수
'''
def solution(n, m):
    # 둘 중 큰 값, 작은 값 return
    maxVal, minVal = max(n, m), min(n, m)
    
    r = 1 # 나눴을 때 나머지 역할
    while r > 0:
        r = maxVal % minVal
        maxVal, minVal = minVal, r # a,b -> b,r 부분

    return [maxVal, n*m//maxVal]

print(solution(3, 12)) # [3,12]
print(solution(2, 5)) # [1, 10]
print(solution(12, 15)) # [3, 60]

