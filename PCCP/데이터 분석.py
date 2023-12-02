def solution(data,ext,val_ext,sort_by) :
    idx_dic = {
        'code': 0,
        'date': 1,
        'maximum': 2,
        'remain': 3
    }
    answer  = []
    data_idx,sort_idx = idx_dic[ext],idx_dic[sort_by]
    for i in data :
        if i[data_idx] < val_ext :
            answer.append(i)

    answer = sorted(answer , key=lambda x:x[sort_idx])
    return answer

print(solution([[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]],'date',20300501,'remain'))