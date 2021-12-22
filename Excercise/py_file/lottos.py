def solution(lottos, win_nums):
    rank = [6,6,5,4,3,2,1]  # 로또 순위
    cnt_z = lottos.count(0) # 0이 몇개인지 확인
    ans = 0 
    for i in win_nums:      # 정답 숫자가
        if i in lottos:     # 로또와 일치할 때 마다 카운트 1 추가
            ans += 1
    return rank[cnt_z+ans], rank[ans]