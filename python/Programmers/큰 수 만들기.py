# 큰 수 만들기 (https://programmers.co.kr/learn/courses/30/lessons/42883)
'''
    참고
    https://velog.io/@soo5717/프로그래머스-큰-수-만들기-파이썬
    
'''
def solution(number, k):
    answer = []
    for i in number:
        if not answer:
            answer.append(i)
            continue
        if k > 0:
            while answer[-1] < i: # 마지막에 추가된 수와 넣으려는 수 비교 시 기존값이 작은 경우 계속 뺌
                answer.pop()
                k -= 1
                if not answer or k <= 0: # 비어있거나 뺴는 횟수가 0이면 중간에 멈춤
                    break
        answer.append(i)
    answer = answer[:-k] if k > 0 else answer # 제거횟수를 다 사용하지 않았을때 남은 횟수만큼 뒷부분 자르기
    return ''.join(answer)

print(solution('4177252841',4))
