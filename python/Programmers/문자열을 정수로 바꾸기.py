# 문자열을 정수로 바꾸기 (https://programmers.co.kr/learn/courses/30/lessons/12925)
'''
    def solution(str):
        return int(str[1:]) * -1 if str.startswith('-') else int(str)
'''
def solution(s):
    return int(s)

print(solution('+1234'))
print(solution('-120'))
