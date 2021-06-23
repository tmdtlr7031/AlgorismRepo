# 짝지어 제거하기
# def solution(s):
#     '''
#         접근
#         1) 앞에서부터 비교
#         2) 연속되면 연속된거 이전 + 이후 합쳐서 리스트 만들고 반복
#         3) 효율성 실패.. 일부 테스트 실패
#     '''
    
#     flag = False
#     lists = list(s)
#     while 1:
#         if len(lists) == 0:
#             return 1
    
#         for i in range(len(lists)-1):
#             if lists[i] == lists[i+1]:
#                 lists = lists[:i] + lists[i+2:]
#                 flag = True
#                 break
#             else:
#                 flag = False
        
#         # 제거 대상 없으면 / 제거하다 남는 게 있다면
#         if not flag or len(lists) == 1:
#             return 0

'''
    조사
    1) Stack 방식으로 접근 -> 맞으면 pop

    로직 설명
    : "if len(stack) == 0"    ---> 처음 비교할 때 기준값이 필요하므로 append 필요. 
    : "else: stack.append(i)" ---> "abcc"인 경우 
                                    1) a추가 (if부분)
                                    2) b차례에서 다음값 c와 비교 (elif 부분)
                                    3) 불일치
                                    4) append해야 마지막 값이 c가 되어 순차적으로 비교 가능 (else 부분)
'''
def solution(s):
    stack = []
    for i in s:
        # 맨처음
        if len(stack) == 0:
            stack.append(i)
        elif i == stack[-1]: 
            # 마지막 값하고 넣으려는 값이 일치하면 신규값 추가 없이 마지막 값 Pop
            stack.pop()
        else:
            stack.append(i) # 넘어가는 용
    
    # 처음부터 불가능한 경우
    if len(stack) != 0:
        return 0

    return 1

# print(solution("baabaa"))
print(solution("casdavzzv"))