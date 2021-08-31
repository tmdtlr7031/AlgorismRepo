# 자연수 뒤집어 배열로 만들기 (https://programmers.co.kr/learn/courses/30/lessons/12932)
'''
    참고
    - 문자열[::-1] => 문자열 뒤집음 (== reversed(문자열))
        ex. '12345' => '12345'[::-1] == '54321'
    - 문자열[::2] => 2개단위로 끊어서 가져옴
        ex. '12345' => '12345'[::2] == '135'
'''
def solution(n):
    # return list(map(int, sorted(str(n), reverse=True))) 이건 왜 안될까.. ===> 내림차순 정렬이 아니라 '단순 뒤집기 문제'
    return list(map(int, list(str(n))[::-1]))
print(solution(12345)) # [5,4,3,2,1]
