def solution(participant, completion):
    answer = ''
    for i in range(len(completion)):
        if completion[i] in participant:
            participant.remove(completion[i])
    answer = participant[0]
    return answer지