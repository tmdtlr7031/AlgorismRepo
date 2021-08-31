# 이상한 문자 만들기 (https://programmers.co.kr/learn/courses/30/lessons/12930)
'''
    문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 각 단어는 하나 이상의 공백문자로 구분되어 있습니다. 
    ==> 하나 이상의 공백 문자로 구분되어 있으므로 공백이 2개 이상인 경우 공백 표시필요
    ex) hello  world => HeLlO  WoRlD
'''
def solution(s):
    answer = ''
    words = s.split(' ')

    for i in words:
        for j in range(len(i)):
            answer += i[j].upper() if j % 2 == 0 else i[j].lower()
        answer += ' '

    return answer[:-1]



print(solution("try hello world"))  # "TrY HeLlO WoRlD"
