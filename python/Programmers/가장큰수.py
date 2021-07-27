# 가장 큰 수

'''
    테스트케이스는 맞는데, 시간초과!

    import itertools
    def solution(numbers):

        data = list(itertools.permutations(list(map(str, numbers)), len(numbers)))
        result = set()

        for i in data:
            result.add(''.join(i))

        return max(result)

    새로운 접근
    - 한 자리씩 탐색해서 큰수대로 나열, 대신 2자리수는 젤 앞에있는 수부터 확인
    - 자리수 다른경우 파악은? => 문자열로 정렬하면 사전순으로 정렬됨. 따라서 34, 30, 3 이렇게 정렬이 될 것

    def solution(numbers):
    strData = list(map(str, numbers)) # 문자열로 치환
    strData.sort() # 정렬 (여기선 pop()쓰려고 일부러 오름차순함)

    answer = ''
    while strData:
        val = strData.pop()
        answer += val

        if len(strData) == 0: # 체크 안하면 다음 if문에서 []인데 strData[-1] 해서 에러남
            break

        if strData[-1].startswith(val[0]):
            if strData[-1][0] in strData: # 첫번재짜리 값이 리스트에 있는지 확인
                answer += strData[-1][0]
                strData.remove(strData[-1][0])

    return answer

    ==> 시간초과
        - 아마도 두번쨰 if ~ in에서 O(n), remove()에서 O(n)이라 O(n^2)이 된 걸까..
'''

# 모범 답안..
def solution(numbers):
    strData = list(map(str, numbers))
    
    # "1000이하 수" 이기 때문에 *3 한 것
    # ['999', '555', '343434', '303030', '333'] 이 될 것이고, 사전순 정렬이니까 ['999', '555', '343434', '333', '303030'] 순서로 정렬 될 것
    strData.sort(key=lambda x: x*3, reverse=True)
    print(strData)  # ['9', '5', '34', '3', '30']

    return str(int(''.join(strData))) # ['0','0','0','0'] 인 경우 '0000' -> 0 ->'0'으로 만들기 위함




# print(solution([6,10,2])) # 6210
print(solution([3, 30, 34, 5, 9]))  # 9534330
