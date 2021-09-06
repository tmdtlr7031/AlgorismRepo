# 튜플 (https://programmers.co.kr/learn/courses/30/lessons/64065)
'''
    Counter 또는 split없이 체크를 하면 연속되는 숫자 인식 불가
    => ex) 111 -> 1이 3개로 판단..
'''
# import collections
# def solution(s):
#     data = s.replace('{', '').replace('}', '')
#     data = data.split(',')
#     collect = collections.defaultdict(int) # 0으로 초기화

#     for i in data:
#         collect[int(i)] += 1

#     return sorted(dict(collect), key=collect.get, reverse=True)

'''
    다른 사람 풀이
    -> 정규식 + Counter
'''
from collections import Counter
import re

def solution(s):
    data = Counter(re.findall('\d+',s)).most_common()
    return [int(i[0]) for i in data]

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))  # [2,1,3,4]
print(solution("{{111},{22,111}}"))  # [2,1,3,4]
