# 수식 최대화 (https://programmers.co.kr/learn/courses/30/lessons/67257)
'''
    # 전달받은 수식에 포함된 연산자의 우선순위를 자유롭게 재정의하여 만들 수 있는 가장 큰 숫자를 제출하는 것입니다.
    # 같은 순위의 연산자는 없어야 합니다.
    # 수식에 포함된 연산자가 2개라면 정의할 수 있는 연산자 우선순위 조합은 2! = 2가지이며, 연산자가 3개라면 3! = 6가지 조합이 가능
    # 계산된 결과가 음수라면 해당 숫자의 절댓값으로 변환하여 제출하며 제출한 숫자가 가장 큰 참가자를 우승자로 선정

    문제 풀이...(너무 복잡하다..)
    - 툴 못쓰는 환경이라 디버깅이 어려워 아래와 같은 방법은 난관에 부딪히는 경우가 많아 무리가 있다..
        1) 정규식
            - '123-456'일 때 숫자, 기호 각각 나누는 정규식은 (\d+)([+-*])하면 컴파일 에러 --> (\d+)([\+\-\*]) 하면 [123-, 456] 이렇게 됨
                => '\d+|[\+\*\-]' 수정
        2) eval() --> 실제 연산처리.. '100+100'을 200으로 처리
'''
import re
import itertools

def solution(expression):
    calcStr = set(re.findall('[\+\-\*]', expression))  # expression에서 특수문자가 어떤게 있는지 확인
    prior = list(itertools.permutations(calcStr, len(calcStr))) # 특수문자 조홥 경우의 수

    divList = re.findall('\d+|[\+\*\-]', expression) # 숫자,특수문자 각각 분리 (설명 참고)

    answer = 0
    for i in prior:
        temp = divList # 각 조합별로 결과값을 비교해야함으로 원데이터를 복사해서 사용한다.
        for j in i:
            while 1:
                if j not in temp: # 특수문자가 없는 경우 break
                    break
                location = temp.index(j) # 숫자와 특수문자가 분리된 리스트에서 앞에서 부터 해당 특수문자 앞 뒤 숫자 처리

                # list(str(..)) 하면 문자열 쪼개짐 ex. 결과값이 '123'이면 '1','2','3'이 되버림
                # 처리한 위치 전 후로 문자열 붙여준다
                temp = temp[:location-1] + [str(eval(''.join(temp[location-1:location+2])))] + temp[location+2:] 
        answer = max(answer, abs(int(temp[0]))) # 음수일 경우 절대값 처리 후 비교해야해서 abs()처리했고 list 선언 후 append 하여 마지막에 sum하기 싫어서 이렇게 함

    return answer



'''
    다른 사람 풀이 (이건 괄호로 우선순위를 만들어가는 과정인데 실행하면서 봐야활듯..)
    - split 시 없는 문자면 그대로 나옴.. index()와 다르게 에러 안나옴
    
    def solution(expression):
    operations = [('+', '-', '*'),('+', '*', '-'),('-', '+', '*'),('-', '*', '+'),('*', '+', '-'),('*', '-', '+')] # 모든 경우의 수 (-,*만 있는 경우 모든 경우의 수는 2!, 이 문제에선 +-*만쓰기 때문에 3!)
    answer = []
    for op in operations:
        a = op[0]
        b = op[1]
        temp_list = []
        for e in expression.split(a):
            temp = [f"({i})" for i in e.split(b)]
            temp_list.append(f'({b.join(temp)})')
        answer.append(abs(eval(a.join(temp_list))))
    return max(answer)
'''

print(solution("100-200*300-500+20"))  # 60420
