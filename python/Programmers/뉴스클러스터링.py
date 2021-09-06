# 뉴스 클러스터링 (https://programmers.co.kr/learn/courses/30/lessons/17677)
import math

'''
    문제 해석의 오류
    - "이때 영문자로 된 글자 쌍만 유효하고, 기타 공백이나 숫자, 특수 문자가 들어있는 경우는 그 글자 쌍을 버린다." 
        -> 알파벳부분만 담고 나머지는 버려야하는데 특수문자를 날리고 시작함
        -> 그래서 'aa1+aa2'의 경우 'aa','aa'가 되야하는데 'aa','aa','aa'가 되어버림
    - "자카드 유사도는 원소의 중복을 허용하는 다중집합에 대해서 확장할 수 있다."
        -> ex. [1,2,3], [1,1,4,4]의 합집합의 경우 [1,1,2,3,4,4] 가 되어야함. (21라인 부연설명..)
    - 합집합이 0 인 경우 65536 리턴해야함. (마지막 테스트 케이스 결과값 참고)
'''
def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()

    data1 = [str1[i:i+2] for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    data2 = [str2[i:i+2] for i in range(len(str2)-1) if str2[i:i+2].isalpha()]

    intersection = set(data1) & set(data2)
    # union = len(set(data1)-set(data2) | set(data2)-set(data1)) 이러면 요소의 중복을 없애버림 --> https://programmers.co.kr/questions/16636
    union = set(data1) | set(data2)

    interCnt = sum([min(data1.count(i), data2.count(i)) for i in intersection])
    uniCnt = sum([max(data1.count(i), data2.count(i)) for i in union])

    return math.trunc(interCnt/uniCnt*65536) if uniCnt != 0 else 65536


# print(solution('FRANCE', 'french'))
# print(solution('handshake', 'shake hands'))
# print(solution('aa1+aa2', 'AAAA12'))
print(solution('E=M*C^2', 'e=m*c^2')) # 합집합이 0인 경우