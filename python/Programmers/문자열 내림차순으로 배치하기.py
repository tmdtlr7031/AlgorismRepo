# 문자열 내림차순으로 배치하기 https://programmers.co.kr/learn/courses/30/lessons/12917
'''
    문제 해석에 오류가 있었음
    - 소문자, 대문자 나눠서 내림차순 후 대문자를 소문자 뒷쪽에 붙여주려고했음
    - 알파벳은 사전순으로 정렬되는데 소문자 우선 정렬되고 대문자는 소문자 뒤에서 정렬됨
'''
def solution(s):
    return ''.join(sorted(s, reverse=True))


print(solution("Zbcdefg")) # 'gfedcbZ'
print(solution("ABDCEFvr"))  # 'vrFEDCBA'
