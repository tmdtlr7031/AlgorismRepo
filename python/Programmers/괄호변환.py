# 괄호 변환 (https://programmers.co.kr/learn/courses/30/lessons/60058)
'''
    조건대로 구현하면된다고함..
    - 참고 : https://velog.io/@donggu/프로그래머스-Python-괄호변환
'''
from collections import deque
def divide(p):
    left, right = 0,0 # '(', ')' 개수 확인용 (둘의 숫자가 같으면 균형잡힌 괄호 문자열임)
    u,v = '',''
    for i in range(len(p)):
        temp = p[:i+1]
        left = temp.count('(')
        right = temp.count(')')
        
        if left == right:
            u, v = temp, p[i+1:]
            return (u, v)

def is_correct(u):
    # 3번 조건
    data = deque(u)
    result = [] # 올바른 괄호 문자열 판단

    # '('면 append, 아니면 pop
    while data:
        char = data.popleft()
        if char == '(':
            result.append(char)
        else:
            if not result: # 비어있으면 ()이 순서가 어긋난것
                return False
            result.pop()
    return True


def solution(p):
    # 1번 조건
    if p == '':
        return p

    # 2번 조건
    u, v = divide(p)

    if is_correct(u):
        u += solution(v)
        return u
    else:
        temp = '('
        v = solution(v)
        temp += v + ')'

        for i in u[1:-1]:
            if i == '(':
                temp += ')'
            else:
                temp += '('
        return temp

print(solution('(()())()'))  # (()())()