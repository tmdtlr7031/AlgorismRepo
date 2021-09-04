# 행렬 테두리 회전하기 (https://programmers.co.kr/learn/courses/30/lessons/77485)
'''
    포기.. (https://minnit-develop.tistory.com/23)
    - 왼쪽 세로 -> 하단 가로 -> 오른쪽 세로 -> 상단 가로

'''
def solution(rows, columns, queries):
    # 행렬 초기화
    data = [[0]*columns for i in range(rows)]

    # 초기화 값 셋팅
    cnt = 1
    for i in range(rows):
        for j in range(columns):
            data[i][j] = cnt
            cnt += 1

    answer = []
    for a,b,c,d in queries:
        tmp = data[a-1][b-1]  # 임시 보관용
        small = tmp  # 최소값 
        
        # 왼쪽 세로
        for i in range(a-1, c-1): # 엎어치는 형태라 마지막빼고 3번만 돌면 됨
            data[i][b-1] = data[i+1][b-1] # 다음행 값으로 현재값 엎어치기
            small = min(small, data[i+1][b-1])

        # 히딘 기로
        for i in range(b-1, d-1):
            data[c-1][i] = data[c-1][i+1]
            small = min(small, data[c-1][i+1])

        # 오른쪽 세로
        for i in range(c-1, a-1, -1):
            data[i][d-1] = data[i-1][d-1]
            small = min(small, data[i-1][d-1])
        
        # 상단 가로
        for i in range(d-1, b-1, -1):
            data[a-1][i] = data[a-1][i-1]
            small = min(small, data[a-1][i-1])
        
        data[a-1][b] = tmp  # 맨처음 8이 오른쪽으로 한 칸 가야함.
        answer.append(small) # 최소값 추가

    return answer

print(solution(6,6,[[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]])) # [8,10,25]
