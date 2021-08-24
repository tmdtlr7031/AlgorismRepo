# 가운데 글자 가져오기 https://programmers.co.kr/learn/courses/30/lessons/12903
def solution(s):
    if len(s) % 2 != 0:
        return s[len(s)//2] # 홀수
    else:
        return s[len(s)//2-1:len(s)//2+1]  # 짝수

print(solution('abcde'))
print(solution('qwer'))

'''
    if 없는 다른 풀이
    def string_middle(str):
        return str[(len(str)-1)//2:len(str)//2+1]
'''
