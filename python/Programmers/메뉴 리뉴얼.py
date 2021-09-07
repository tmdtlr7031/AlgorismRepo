# 메뉴 리뉴얼 (https://programmers.co.kr/learn/courses/30/lessons/72411)
'''
    제한 상황에 없는 함정...입출력 결과 보고 판단해야하나 ㅡㅡ
    : https://programmers.co.kr/questions/15711 (동일한 길이의 주문횟수 중 가장 큰 값 빼고는 탈락) ex. AB: 3회, AD: 4회 면서 [3,4,5]면 AB는 탈락
'''
import collections
import itertools

def solution(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += itertools.combinations(order, course_size) # 단품메뉴 개수에 따른 주문메뉴의 모든 조합

        most_ordered = collections.Counter(order_combinations).most_common() # 최다 빈도 조합
        result += [k for k, v in most_ordered if v > 1 and v == most_ordered[0][1]] # 최소 2인이상 주문조건 & 가장많이 주문된 메뉴 조합들 리턴

    return [''.join(v) for v in sorted(result)]


# print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4])) #["AC", "ACDE", "BCFG", "CDE"]
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5])) # ["ACD", "AD", "ADE", "CD", "XYZ"]
