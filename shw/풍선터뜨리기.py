from collections import deque

def burst_balloons(paper_list):
    
    n = len(paper_list)
    balloons = deque(enumerate(paper_list, start= 1)) # (풍선번호, 풍선 안 종이번호)
    burst_list = []

    #print(balloons)

    while balloons:

        if not balloons:  # 모든 풍선을 터뜨렸으면 종료
            break

        balloon_num, paper_num = balloons.popleft() # 1번 풍선부터 터트리면서 풍선번호와 종이번호를 반환받음
        burst_list.append(balloon_num)  # 터뜨린 풍선번호를 터뜨린 리스트에 추가

        # 종이번호에 0은 없음  
        ### rotate(양수) -- (오른쪽의 원소들 왼쪽으로 회전, '왼쪽으로 이동')
        ### rotate(음수) -- (왼쪽의 원소들 오른쪽으로 회전, '오른쪽으로 이동') 자기자신도 오른쪽으로 이동하기 때문에 고려해 주어야 함 -1
        if paper_num > 0:
            balloons.rotate(-(paper_num-1)) 
        else:
            balloons.rotate(-paper_num) 
    
    return burst_list

N = int(input("풍선의 개수:"))
paper_list = list(map(int, input("풍선 안에 적힌 종이의 숫자를 입력").split()))

result = burst_balloons(paper_list)
print("풍선이 터지는 순서:", result)