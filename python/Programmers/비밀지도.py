# 비밀지도 https://programmers.co.kr/learn/courses/30/lessons/17681
def solution(n, arr1, arr2):
    answer = []
    # 10진법 -> 2,8,16진법은 지원함 (bin, oct, hex)    
    # 0b로 시작하기 때문에 [2:], 9의 경우 1001이지만 비교를 위해 자릿수 맞춰주기 작업 -> rjust (왼쪽부터 채우면서 오른쪽으로 밀기)
    convertArr1 = [list(bin(i)[2:].rjust(n, '0')) for i in arr1]
    convertArr2 = [list(bin(i)[2:].rjust(n, '0')) for i in arr2]
    
    for a1, a2 in zip(convertArr1, convertArr2):
        temp = ''
        # print(a1, a2)
        for i in range(n):
            if int(a1[i])+int(a2[i]) == 0:
                temp += ' '
            else:
                temp += '#'
        answer.append(temp)
    return answer

'''
    다른 사람 풀이 (비트연산자 이용)
    - https://withcoding.com/69
    - or 연산을 이용해 둘중 하나만 1이면 1 return
    - 참고
        : rjust, ljust 대신 zfill 써도 됨

        문자열.zfill(숫자)
        -> 해당 문자열의 앞을 숫자 자리수만큼 0으로 채운다.

    def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer
'''


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
