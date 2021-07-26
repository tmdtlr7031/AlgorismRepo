'''
    선택정렬
    - 첫번째 값 기준, 최소값하고 교환, 두번째값 기준 최소값하고 교환 (이때 기존에 교환된 값은 제외한 최소값임)
    - O(n^2)
    - 마지막값은 알아서 정렬되기 때문에 n-1번 탐색

    1. 탐색하는 값의 인덱스를 최소값이라 가정하여 기준.
    2. 내부 탐색하면서 기준값보다 작은 값은 새로운 최소값에 해당하는 인덱스로 설정
    3. 탐색 종료 후 스위칭
'''
# 오름차순 정렬
def selectionSort(listData):
    for i in range(len(listData)-1):
        minIdx = i
        for j in range(i+1, len(listData)):
            if listData[minIdx] > listData[j]:
                minIdx = j
        listData[i], listData[minIdx] = listData[minIdx], listData[i]
            
    return listData

print(selectionSort([7, 4, 5, 1, 3]))
