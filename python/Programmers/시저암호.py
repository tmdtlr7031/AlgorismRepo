# 시저암호 (https://programmers.co.kr/learn/courses/30/lessons/12926)
def solution(s, n):
    answer = ''
    alphLow = 'abcdefghijklmnopqrstuvwxyz'
    alphUp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for i in s:
        if i == ' ':
            answer += ' '
            continue
        elif i in alphLow:
            answer += alphLow[(alphLow.index(i)+n) % len(alphLow)]
        else:
            answer += alphUp[(alphUp.index(i)+n) % len(alphUp)]
            
    return answer

print(solution("AB", 1))
print(solution("z", 1))
print(solution("a B z", 4))
print(solution("AaZz", 25))
