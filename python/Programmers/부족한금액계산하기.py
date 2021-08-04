# 위클리 챌린지 : 1주차 (부족한 금액 계산하기)
'''
    접근
    0) count만큼 for문..? -> 다른 방법 없을까 고민
    1) price = 3이고 count = 4 일 때, 1,3,6,9
    2) 이는 c=1, 3*1 / c=2, 3*1 + 3*2 .... => c=3, 1n+2n+3n .. 이런식
    3) 규칙은..?
        -   c       합계    
            1       p
            2       3p
            3       6p
               ...
            x       x까지합 * p
    4) 따라서 주어진 count까지의 합 (ex. 5 => 1+2+3+4+5) * price
    5) x까지의 합 = 가우스 공식
        - n*(n+1)/2

    6) 금액이 부족하지 않으면 0 return
'''
def solution(price, money, count):
    data = money - (count * (count+1) // 2) * price # int / int = float 이므로 몫 구하는 // 이용하여 int형
    return abs(data) if data < 0 else 0

print(solution(3,20,4)) # 10

''' 
    다른사람 풀이

    def solution(price, money, count):
        return max(0,price*(count+1)*count//2-money)

    - max(기준값, 기준값보다 작은 경우)
'''
