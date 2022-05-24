def solution(phone_number):
    answer = ''
    result = []
    for i in range(len(phone_number[:-4])):
        result.append('*')
    result.append(phone_number[-4:])
    answer="".join(result)
    return answer

phone_number = "027778888"
print(solution(phone_number))