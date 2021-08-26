# 문자열 다루기 기본 https://programmers.co.kr/learn/courses/30/lessons/12918
'''
    참고 (https://soooprmx.com/파이썬의-숫자판별함수/)
    isdigit(), isnumeric(), isdecimal()
        : isdecimal() = int타입으로 즉시 변환이 가능한 문자 (ex. '1234')
        : isdigit() = ex. 3² => true, decimal은 false 리턴
        : isnumeric() = 숫자값 표현에 해당하는 텍스트까지 인정 ex.“½” => True 
'''
def solution(s):
    return s.isdecimal() and len(s) in (4, 6)

print(solution('a234')) # False
print(solution('1234')) # True
