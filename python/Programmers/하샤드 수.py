# 하샤드 수 (https://programmers.co.kr/learn/courses/30/lessons/12947)
def solution(x):
    return True if x % sum(list(map(int, str(x)))) == 0 else False

print(solution(10)) # true
print(solution(11)) # false
