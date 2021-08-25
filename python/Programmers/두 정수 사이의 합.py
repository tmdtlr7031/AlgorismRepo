# 두 정수 사이의 합 https://programmers.co.kr/learn/courses/30/lessons/12912
'''
    가우스 덧셈이용
    -> 1부터 n까지의 합 => n(n+1) / 2

    1) a,b 중 어떤값이 큰 지 모름 -> 절대값 이용
    2) 1~n까지는 n개니까 |a-b|+1은 a,b사이의 n개가 된다
    3) n+1 -> 1~10까지일때 1+10을 한것 -> n이 10개니까 10+1일 수도 있지만 어찌보면 첫값+끝값 인 것이라 판단 -> a+b
'''
def solution(a, b):
    return int((abs(a-b)+1) * (a+b) /2)

print(solution(3,5)) # 12
print(solution(3,3)) # 3

'''
    다른 풀이
    if a > b:
         a, b = b, a
    return sum(range(a,b+1))

'''
