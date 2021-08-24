# 다트게임 https://programmers.co.kr/learn/courses/30/lessons/17682

'''
    접근
    : 왼쪽부터 하나씩 꺼내서 비교
'''
import collections
def solution(dartResult):
    answer = 0
    data = collections.deque(dartResult)

    tmp = ''
    result = dict()
    while data:
        chars = data.popleft()
        if chars.isnumeric():
            tmp += chars
            continue
        elif chars.isalpha():
            if chars == 'D':
                result[answer] = int(tmp)**2
            elif chars == 'T':
                result[answer] = int(tmp)**3
            else:
                result[answer] = int(tmp)
            tmp = ''
            answer +=1
        else:
            if chars == '*':
                result[answer-1] = result[answer-1] * 2
                if answer != 1:
                    result[answer-2] = result[answer-2] * 2
            else:
                result[answer-1] = result[answer-1] * -1

    return sum(result.values())

# print(solution('1S2D*3T')) # 37
print(solution('1D2S#10S')) # 9


'''
    다른 사람 접근
    : 정규식을 이용한 처리 + *,# 없을떄도 *1 해준것

    import re
    def solution(dartResult):
        bonus = {'S' : 1, 'D' : 2, 'T' : 3}
        option = {'' : 1, '*' : 2, '#' : -1}
        p = re.compile('(\d+)([SDT])([*#]?)')
        dart = p.findall(dartResult)
        for i in range(len(dart)):
            if dart[i][2] == '*' and i > 0:
                dart[i-1] *= 2
            dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

        answer = sum(dart)
        return answer
'''
