def changecode(music_): 
    music_ = music_.replace('C#', 'c')
    music_ = music_.replace('D#', 'd')
    music_ = music_.replace('F#', 'f')
    music_ = music_.replace('G#', 'g')
    music_ = music_.replace('A#', 'a')    
    return music_ 

def caltime(musicinfo_):
    starttime = musicinfo_[0]
    endtime = musicinfo_[1]
    hour = 1 * (int(endtime.split(':')[0]) - int(starttime.split(':')[0]))
    if hour == 0: 
        total = int(endtime.split(':')[1]) - int(starttime.split(':')[1])
    else: 
        total = 60 * hour + int(endtime.split(':')[1]) - int(starttime.split(':')[1])

    return total

def solution(m, musicinfos):
    answer = []
    m = changecode(m)
    for idx, info in enumerate(musicinfos):
        info = changecode(info)
        info = info.split(',')
        time = caltime(info)

        if len(info[3]) >= time:
            melody = info[3][:time]
        else:
            a = time // len(info)[3]
            b = time % len(info)[3]
            melody = info[3]*a + info[3][:b]
        if m in melody:
            answer.append([idx, time, info[2]])
    if len(answer) != 0:
        answer = sorted(answer, key = lambda x : x[1])
        return answer[0][2]
    return '(None)'