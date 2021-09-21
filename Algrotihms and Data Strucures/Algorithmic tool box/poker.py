n = int(input())
arr = []
 
for i in range(n):
    data = input().split(' ')
    arr.append(data)
 

 
for case in arr:
    # n=cards_num,m=jokers_num,k=players_num
    n,m,k = int(case[0]),int(case[1]),int(case[2])
    player_cards = n//k
    mini= min(player_cards,m)
    re = (m-mini+k-2)//(k-1)
    print(mini-re)