# 자릿수 더하기 (https://programmers.co.kr/learn/courses/30/lessons/12931)
def solution(n):
    return sum(list(map(int, str(n))))

print(solution(123)) # 6
print(solution(987)) # 24

'''
    10씩 나누면서 재귀호출
    def sum_digit(number):
        if number < 10:
            return number;
        return (number % 10) + sum_digit(number // 10) 
'''
