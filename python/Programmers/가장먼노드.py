# 가장 먼 노드
# 1에서 가장 멀리 떨어진 노드가 몇 개인지

''' 
    bfs!
    - 인접경로 마다 체크해서 몇번지나는지 보는 느낌..
'''

from collections import deque
def solution(n, edge):

    # 초기화
    graph = dict()
    for v1, v2 in edge:
        graph.setdefault(v1, []).append(v2)
        graph.setdefault(v2, []).append(v1)

    print(graph)

    will_visit = deque([[1,0]]) # node, depth
    check = [-1] * (n+1) # node 번호랑 일치 시키려고 +1 한듯..?

    while will_visit:
        node, depth = will_visit.popleft()
        check[node] = depth

        # 한번도 방문한 적 없는 node인지 확인
        for val in graph[node]:
            if check[val] == -1:
                check[val] = 0
                will_visit.append([val, depth+1])
        print(will_visit)
        print(check)
        print("----------------")

    return check.count(max(check))


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])) # 3
