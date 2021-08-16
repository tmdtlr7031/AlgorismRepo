# 상호평가 (위클리 챌린지 2주차)
def solution(scores):
    answer = ''
    
    newData = list()
    # 이차원 배열 -> 열 기준으로 재 배치
    for i in zip(*scores): # * : 이차원 배열 내 배열 요소를 넣는다는 의미
        newData.append(list(i))

    for idx,val in enumerate(newData):
        answer += makeRank(idx, val)

    return answer

def makeRank(idx, lists):
    # 자기 자신을 평가한 점수가 최소, 최대값인지 판단 후 평가.
    '''
        pop(상수) -> O(n)이니까 pop하지 말고 sum 할때 빼자.
    
        if min(lists) == lists[idx] or max(lists) == lists[idx]:
            if lists.count(lists[idx]) == 1:
                lists.pop(idx)
    '''
    avg = sum(lists)/len(lists)
    if lists[idx] in (min(lists), max(lists)):
        if lists.count(lists[idx]) == 1:
           avg = (sum(lists) - lists[idx]) / (len(lists)-1)            

    # 평균 점수 별 등급
    if avg >= 90:
        return 'A'
    elif 80 <= avg < 90:
        return 'B'
    elif 70 <= avg < 80:
        return 'C'
    elif 50 <= avg < 70:
        return 'D'
    else:
        return 'F'


# print(solution([[50,90],[50,87]])) # DA
print(solution([[100, 90, 98, 88, 65], [50, 45, 99, 85, 77], [47, 88, 95, 80, 67], [61, 57, 100, 80, 65], [24, 90, 94, 75, 65]]))  # FBABD
# print(solution([[100, 100, 0], [0,100,100], [100,0,100]]))  # 0 100,0 | 1 0,100

