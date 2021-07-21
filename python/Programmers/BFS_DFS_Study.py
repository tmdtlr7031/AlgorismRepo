# BFS, DFS 학습.. ==> 코테에서 막힐 때 다른 분들 풀이에서 "BFS를 이용했어요~", "DFS를 이용한 풀이입니다" 이런 식이 많아서 따로 학습..

'''
    BFS (너비우선탐색)
        - 최단거리 시 사용
        - 방문이력, 방문예정 필요
        - deque를 통해 pop시 성능 향상 (import collections)
        - 상세 예시는 https://www.fun-coding.org/Chapter18-bfs-live.html 참고
        
    흐름
        - 'A' 시작인 경우 -> 'A'를 방문예정에 넣고 초기화
        - 방문예정이 없을 때까지 반복
        - 방문이력에 'A'가 없으면 추가
        - 'A' 그래프 리스트를 extend (==> 방문예정 = ['B', 'C'])
        - 반복
        - ex. 'B' 차례 -> pop (=> 방문예정 = ['C']) -> 방문이력에 'B' 넣고 방문예정에 'B'의 그래프 리스트 extend (=> 방문옝정 = ['C','A','D']) 이런식으로 붙게됨
            -  Q. 그럼 중복 방지해서 set쓰면 좋지않나..?
               A. 순서성 보장이 안되기 때문에 문제에 따라 따져봐야 할 것 (dict은 파이썬 3.7 이후로 dict에 넣는 순서대로 구성됨.)
'''

'''
    그래프 시각화 (참고, 여기선 왼->오 순으로 탐색함)
                A
            B           C
        D           G   H   I
     E     F            J
'''
initGraph = dict();
initGraph['A'] = ['B','C']
initGraph['B'] = ['A','D']
initGraph['C'] = ['A','G','H','I']
initGraph['D'] = ['B','E','F']
initGraph['E'] = ['D']
initGraph['F'] = ['D']
initGraph['G'] = ['C']
initGraph['H'] = ['C']
initGraph['I'] = ['C','J']
initGraph['J'] = ['I']

print('==========')
print(initGraph)
print('==========')

visited_BFS = dict()  # 방문이력, list 시 if node not in visited 부분에서 O(n) 이므로 hash로 구현

import collections
def BFS(graph, start_node, visited):
    # 방문예정, 시작점을 방문예정 큐에 넣고 시작
    will_visit = collections.deque([start_node])  

    while will_visit:
        node = will_visit.popleft()
        if node not in visited:
            visited[node] = True # 방문이력에 추가
            will_visit.extend(graph[node])
            
    return list(visited.keys())

print('BFS = ', BFS(initGraph, 'A', visited_BFS))


# =========================================================================================================
'''
    DFS (깊이우선탐색)
    - 모든 노드 탐색
    - 스택, 재귀로 구현
    - 속도는 BFS보다 빠르다고함
'''
visited_DFS = dict()
visited_DFS_recursive = []

def DFS(graph, start_node, visited):
    will_visit = [start_node]

    while will_visit:
        node = will_visit.pop()
        if node not in visited:
            visited[node] = True  # 방문이력에 추가
            will_visit.extend(graph[node])

    return list(visited.keys())



print('DFS nomal= ', DFS(initGraph, 'A', visited_DFS))
print('DFS recur= ', DFS_recursive(initGraph, 'A', visited_DFS_recursive))
