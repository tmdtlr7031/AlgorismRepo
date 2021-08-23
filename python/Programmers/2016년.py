# 2016년
def solution(a, b):
    result = {3:'SUN', 4:'MON', 5:'TUE', 6:'WED', 0:'THU', 1:'FRI', 2:'SAT'}
    calcDay = 0

    for i in range(1,a):
        if i in [1,3,5,7,8,10,12]:
            calcDay += 31
        elif i == 2:
            calcDay += 29
        else:
            calcDay += 30

    return result[(calcDay+b)%7]

print(solution(5,24)) # "TUE"
# print(solution(1,7))  # "THU"

'''
    다른 풀이
    1) 제시된 월의 전달까지 일 수 구함 (ex. 5면 4월까지의 일수)
    2) 잔여 일수 구함
    3) % 7

    def getDayName(a, b):
        months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
        return days[(sum(months[:a-1])+b-1) % 7]

    다른 풀이
    1) datetime 이용
    import datetime
    def getDayName(a, b):
        t = 'MON TUE WED THU FRI SAT SUN'.split()
        return t[datetime.datetime(2016, a, b).weekday()]


    print(getDayName(5, 24))
'''
