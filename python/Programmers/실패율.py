# 실패율 (https://programmers.co.kr/learn/courses/30/lessons/42889)
# 1510 ~

'''
    처리중에 내부에러 어쩌고.. 뭔가 잘못된듯,. Counter 때문인가..

    import collections
    def solution(N, stages):
        answer = []
        # print(collections.Counter(stages))
        counts = collections.Counter(stages)
        
        result = dict()
        for i in range(1,N+1):
            result.setdefault(i,0)

        standard = len(stages)
        cnt = 1
        while cnt <= N:
            # 전부 1스테이지에서 막힌 경우
            if standard == 0:
                break

            getData = counts.get(cnt, 0) # 실패한 스테이지에 해당하는 개수

            result[cnt] = getData / standard # 스테이지별 실패율
            standard -= getData # 실패율 측정된 스테이지 모수에서 제외

            cnt += 1

        return  [i for i,v in sorted(list(zip(result.keys(), result.values())), key=lambda x: (-x[1], x[0]))] # dict -> tuple 후 다중조건 정렬 후 (라운드, 실패율)에서 라운드만 리스트로 뽑기

'''

# count 때문에 O(n^2)
# 미리 count 만들어 놓고 쓰면 O(n)
def solution(N, stages):
    result = dict()
    standard = len(stages)

    for i in range(1, N+1):
        if standard == 0:
            result[i] = 0
        else:
            count = stages.count(i)
            result[i] = count / standard
            standard -= count

    '''
        value기준 내림차순 정렬 후 key값 리스트로 뽑음.
        상세 설명 
            : result는 dictionary이므로 sorted에 result를 그냥 넘기면 result의 keys가 들어갑니다. keys는 생략이 가능합니다. 
              거기에 lambda는 기준을 result[x] 즉 value로 정렬한다는 뜻입니다. 그래서 key가 출력되게 됩니다.

        Q. 실패율 내림차순 하는데, 동일한 실패율인 경우 라운드 오름차순 조건에서 후자 조건은 어케 처리한거?
        A. 파이썬 3.7부터 dict도 순서성을 보장(=넣은대로 기억) ---> 1~5순서로 넣었기 때문에 dict에는 1,2,3,4, ... 이렇게 오름차순으로 키값이 들어가 있을 것이다.
           따라서 자연스레 후자 조건이 성립되기 때문에 실패율에 따른 내림차순만 신경쓰면 된다.
    '''
    return sorted(result, key=lambda x: result[x], reverse=True)

print(solution(5, [2,1,2,6,2,4,3,3])) # [3,4,2,1,5]
# print(solution(4, [4,4,4,4,4])) # [4,1,2,3]
# print(solution(4, [1,1,1,1,1]))
# print(solution(8, [1, 2, 3, 4, 5, 6, 7]))

