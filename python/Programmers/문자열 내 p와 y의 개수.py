# 문자열 내 p와 y의 개수 https://programmers.co.kr/learn/courses/30/lessons/12916
import collections
def solution(s):
    # 소문자로 통일 + counter 이용해서 해시로! -> count() : O(n)
    # p,y가 없어도 둘 다 None이기 때문에 True -> 둘 다 없는 경우 True리턴 조건에 부합
    conters = collections.Counter(s.lower())
    return conters['p'] == conters['y']

print(solution('pPoooyY')) # true
print(solution('Pyy')) # false
