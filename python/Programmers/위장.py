# 위장 (https://programmers.co.kr/learn/courses/30/lessons/42578)
import collections

def solution(clothes):
    answer = 1
    clothes_dict = collections.defaultdict(list)
    
    for cloth, kind in clothes:
        clothes_dict[kind].append(cloth)

    # 안입는경우, 입는 경우
    # 'headgear': ['yellowhat', 'green_turban'] 라면 headgear의 총 경우의 수는 안입는경우, yellowhat, green_turban 총 3개
    for i in clothes_dict.values():
        answer *= len(i)+1 # (안 입는 경우룰 +1 한 것)

    # 모든 부위를 안 입는 경우 제외
    return answer-1



print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
# print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))

