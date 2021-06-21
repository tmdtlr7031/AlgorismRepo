# 프로그래머스 오픈 채팅방
def solution(record):
    result = []
    answer = dict()
    for i in record:
        data = i.split(" ")
        if data[0] == 'Enter':
            answer[data[1]] = data[2]
            result.append([data[1], "님이 들어왔습니다."])
        elif data[0] == 'Change':
            answer[data[1]] = data[2]
        else:
            result.append([data[1], "님이 나갔습니다."])

    return [answer[val[0]]+val[1] for val in result]

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))




