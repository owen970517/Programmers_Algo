def solution(numbers, hand):
    answer = ''
    keypad = {1 :[0,0] , 2 : [0,1] , 3 : [0,2],
                4: [1,0] ,5 : [1,1] ,6: [1,2],
                7: [2,0] , 8: [2,1] ,9 : [2,2],
            '*' : [3,0] , 0 : [3,1], '#' : [3,2]}
    nl = keypad['*']
    nr = keypad['#']
    for i in numbers :
        if i in [1,4,7] :
            answer += 'L'
            nl = keypad[i]
        elif i in [3,6,9] :
            answer +='R'
            nr = keypad[i]
        elif i in [2,5,8,0] :
            absL = abs(keypad[i][0] - nl[0]) + abs(keypad[i][1]-nl[1])
            absR = abs(keypad[i][0] - nr[0]) + abs(keypad[i][1]-nr[1])
            if absL > absR:
                answer+='R'
                nr=keypad[i]
            elif absL < absR:
                answer +='L'
                nl=keypad[i]
            else :
                if hand == 'left' :
                    answer += 'L'
                    nl =keypad[i]
                elif hand == 'right':
                    answer +='R'
                    nr =keypad[i]
    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = 'right'
print(solution(numbers,hand))