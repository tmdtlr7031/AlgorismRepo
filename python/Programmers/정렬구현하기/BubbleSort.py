'''
    버블정렬
    - 서로 인접한 두 원소를 검사하여 정렬하는 알고리즘 (선택정렬과 기본개념 유사)
    - 일반적으로 자료의 교환 작업(SWAP)이 자료의 이동 작업(MOVE)보다 더 복잡하기 때문에 버블 정렬은 단순성에도 불구하고 거의 쓰이지 않는다.
    - O(n^2)

    1. (7,4), (4,5) ... (1,3) => 4번만 돌면됨.
    2. 안에 값들은 1회차 : 3까지, 2회차는 1까지, 3회차는 5까지 --> 1회차 : range(4)까지만. 왜냐면 n, n+1로 바로 다음 값 찾아야하니까 idx 0~3까지하면 (0,1)(1,2)(2,3)(3,4)로 딱 됨
'''

# 오름차순으로 정렬해보자
def BubbleSort(listData):
    for i in range(len(listData)-1, 0, -1): # 0123
        for j in range(i):
            if listData[j] > listData[j+1]:
                listData[j], listData[j+1] = listData[j+1], listData[j]
    return listData

print(BubbleSort([7,4,5,1,3]))
