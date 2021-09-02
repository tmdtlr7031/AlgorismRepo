# 정수 제곱근 판별 (https://programmers.co.kr/learn/courses/30/lessons/12934)
'''
    제곱근일 때 소수점이 0인 경우다.
    121 => 11.0

    따라서 int(11.0) 과 11.0 이 같으면 정수 제곱근
    --> 약수 개수 판별에서 이용하던 방식 (해당 조건 참인 경우 거기선 약수 갯수 홀수)
'''
def solution(n):
    check = n**0.5
    return int((check+1)**2) if check == int(check) else -1

print(solution(121)) # 144
# print(solution(3)) # -1
