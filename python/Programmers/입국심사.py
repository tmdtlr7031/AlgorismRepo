# 입국심사 (1941시작 ~ 포기..)
# 이분탐색..
'''
    [ 정답 풀이 ]
    이분탐색...어렵다
    - 핵심 : 이분 탐색을 할 때는 ‘이분 탐색의 범위는 무엇으로 할지’ 와 ‘이분 탐색의 기준을 무엇으로 할지’ 을 잡아야한다.
          : 정렬되어 있어야 한다.

          범위 : 심사를 하는데 총 걸리는 시간으로, 1분 부터 가장 비효율적으로 심사를 받았을 때 걸리는 시간(분)으로 하였다.
          mid : 모든 심사관들에게 주어진 시간이다. 따라서 people 은 모든 심사관들이 mid분 동안 심사한 사람의 수가 된다.
          기준 : mid 동안 심사한 사람의 수(people)가
            심사 받아야할 사람의 수(n)보다 많거나 같을 경우에는 시간이 충분했던 것이므로 주어진 시간을 줄이고 ( right = mid - 1 -> right 를 줄이면 left와 right의 중간 값인 mid 도 줄어드니까 주어진 시간이 줄어든다.)
            심사 받아야할 사람의 수(n)보다 적은 경우에는 시간이 부족했던 것이므로 주어진 시간을 늘린다. (left = mid + 1)

    - 참고 : https://sohee-dev.tistory.com/123
'''
def solution(n, times):
    answer = 0
    # right는 가장 비효율적으로 심사했을 때 걸리는 시간
    # 가장 긴 심사시간이 소요되는 심사관에게 n 명 모두 심사받는 경우이다.
    left, right = 1, max(times) * n
    while left <= right:
        mid = (left + right) // 2
        people = 0

        for time in times:
            # people 은 모든 심사관들이 mid분 동안 심사한 사람의 수
            people += mid // time
            # 모든 심사관을 거치지 않아도 mid분 동안 n명 이상의 심사를 할 수 있다면 반복문을 나간다.
            if people >= n:
                break

        # 심사한 사람의 수가 심사 받아야할 사람의 수(n)보다 많거나 같은 경우
        if people >= n:
            answer = mid
            right = mid - 1
        # 심사한 사람의 수가 심사 받아야할 사람의 수(n)보다 적은 경우
        elif people < n:
            left = mid + 1

    return answer
    
print(solution(6, [7,10])) # 28
