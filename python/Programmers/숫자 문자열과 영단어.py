# 숫자 문자열과 영단어
'''
    접근방법
    1) 해시를 이용해서 빠르게 찾자
    2) 데이터 구성
        - {'zero' : '0', 'one':'1', 'two':'2' ...}
    3) 주어진 문자열(=s)을 한 글자씩 pop해서 꺼내면서 dict의 key값으로 존재하는지 확인 후 있으면 해당 value를 추가
    4) 왼쪽부터 pop을 위해 deque이용

    replace를 사용하면 더 깔끔해진다 -> 다른 사람 풀이 확인
'''
import collections
def solution(s):
    if s.isnumeric():
        return int(s)

    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    # 데이터 구성
    numDict = dict()
    for idx, val in enumerate(words):
        numDict[val] = str(idx)

    answer = collections.deque(s)
    result = '' # return용 변수
    temp = '' # 숫자 외 알파벳을 붙일 임시 변수
    while answer:
        alph = answer.popleft()

        # 알파벳, 숫자 섞여있는 경우 -> pop한게 숫자인지 확인    
        if alph.isnumeric():
            result += alph
        else:
            temp += alph
        
        # 만들어진 문자가 dict의 key값으로 존재하는지 판단
        if temp in numDict:
            result += numDict[temp]
            temp = '' # 초기화

    return int(result)


'''
    다른 사람 풀이 (1)

    num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

    def solution(s):
        answer = s
        for key, value in num_dic.items():
            answer = answer.replace(key, value)
        return int(answer)

    ----

    다른 사람 풀이 (2)

    def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in range(len(words)):
        s = s.replace(words[i], str(i))

    return int(s)
'''

# print(solution('one4seveneight')) #1478
# print(solution('23four5six7'))  # 234567
