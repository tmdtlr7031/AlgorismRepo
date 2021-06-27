# 완주하지 못한 선수
# https://chancoding.tistory.com/43 쟈료형별시간복잡도
'''
    접근
    1) set으로 형변환 후 차집합
    2) 이때 0 이면 겹치는 경우가 있는 것이므로 Counter를 이용해 participant의 최빈값을 리턴
    3) 70퍼 정답률.. 런타임 에러
'''

# from collections import Counter

# def solution(participant, completion):
#     answer = ''
#     participantForSet = set(participant)
#     completionForSet = set(completion)
#     result = list(participantForSet - completionForSet)

#     if len(result) == 0:
#         # 두개이상인거 찾기
#         answer = Counter(participant).most_common()[0][0] # (값,최빈수) 내림차순으로
#     else:
#         answer = result[0];
#     return answer


'''
    구글링
    1) Counter 사용하려는 접근은 맞음
    2) 원래 dict 이렇게 빼기가 불가능하지만, Counter객체라 가능
        ex) Counter({'mislav': 2, 'stanko': 1, 'ana': 1}) - Counter({'stanko': 1, 'ana': 1, 'mislav': 1}) = Counter({'mislav': 1})
'''
from collections import Counter

def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys())[0]

print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]));

'''
    다른 풀이

    def solution(participant, completion):
        participant.sort()
        completion.sort()
        for p, c in zip(participant, completion):
            if p != c:
                return p
        return participant[-1]
    
    1) 100,000 건 정도인데 sort해도 괜찮은듯
    2) zip은 같은 인덱스끼리 짝지어줌. 변수 하나만 있으면 튜플형태로 뱉음
    3) 정렬했기 때문에 if 조건에 안걸리면 1개 더 많은 participant의 마지막 값을 리턴 (== 미완주자)
'''
