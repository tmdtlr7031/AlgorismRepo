# 조이스틱 (https://programmers.co.kr/learn/courses/30/lessons/42860) 탐욕법
'''
    포기...

    탐욕법
    - 매순간 최적의 결정 (하지만 항상 최적의 결과는 아님)
    - 조건
        1) <탐욕스러운 선택 조건 (Greedy choice property)>
            앞의 선택이 이후의 선택에 영향을 주지 않는 조건.

        2) <최적 부분 구조 조건(Optimal Substructure)>
            문제에 대한 최종 해결 방법이 부분 문제에 대해서도 또한 최적 문제 해결 방법이다는 조건.

    상하 관점의 최소값, 좌우 관점의 최소값 고려가 필요한 문제
'''
def solution(name):
    # 단어마다 상하 조정 시 최소 변경값 (상하 조정 끝)
    change = [min(ord(i) - ord("A"), ord("Z") - ord(i)+1) for i in name] # z->a는 1차이라 마지막에 +1
    idx, answer = 0, 0

    while True:
        answer += change[idx]
        change[idx] = 0

        if sum(change) == 0:
            break

        left, right = 1, 1
        while change[idx - left] == 0: # 뒤로 이동 시 'A'(== 0) 가 아닌 문자열 위치 탐색 --> 처리한 문자열(0)도 건너뜀
            left += 1

        while change[idx + right] == 0: # 정상 이동 시 처리해야하는 문자열 위치 탐색
            right += 1

        answer += left if left < right else right # 앞, 뒤 중 이동해야하는 만큼 더하기
        idx += -left if left < right else right # 방향 재 설정

    return answer

# print(solution('JAN')) # 23
print(solution('JEROEN')) # 56
