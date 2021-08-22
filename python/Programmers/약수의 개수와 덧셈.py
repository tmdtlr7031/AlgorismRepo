# 약수의 개수와 덧셈(lv1)
def solution(left, right):
    answer = 0

    for i in range(left, right+1):
        cnt = set({1}) # 약수 개수 count : 1을 셋팅한 이유 => 1,2 인 경우 안쪽 for문 안돌고 끝나기 떄문에 초기값 1로 셋팅
        # 약수 구하기
        for num in range(1, i//2+1): # 해당 값의 절반까지만 판단 후 *2 ==> 한 쌍이기 때문
            if i % num == 0: # 약수인지?
                cnt.add(num)
                cnt.add(i//num)

        # 홀/짝 판단
        if len(cnt) % 2 == 0:
            answer += i
        else:
            answer -= i

    return answer

''' 
    다른 접근
    - 약수
        => 약수의 개수가 홀수 == 제곱수 (0.5제곱한 값[**0.5] == math.pow(i,2))
        ex) 16(1,2,4,8,16)은 제곱근을 int로 했을 때 4, 제곱근 4.0 --> 약수 개수가 홀수

    def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        # print(i, int(i**0.5), i**0.5)
        if int(i**0.5) == i**0.5:
            answer -= i
        else:
            answer += i
    return answer
'''



# print(solution(1, 2))
print(solution(13,17)) # 43
# print(solution(24,27)) # 52
