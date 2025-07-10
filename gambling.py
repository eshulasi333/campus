dealer=input().split()
player=input().split()
deal_num=[]
deal_let=[]
play_num=[]
play_let=[]
for x in dealer:
    deal_num.append(x[1:])
    deal_let.append(x[0])
for y in player:
    play_num.append(y[1:])
    play_let.append(y[0])
s='23456789'
t='10KJQ'
dealer_val=0
player_val=0
while dealer_val==player_val:
    for a in deal_num:
        if a in s:
            dealer_val+=int(a)
        elif a in t:
            dealer_val+=10
        else:
            word=deal_let[deal_num.index(a)]
            if word in play_num:
                dealer_val+=1
            else:
                dealer_val+=11
    for a in play_num:
        if a in s:
            player_val+=int(a)
        elif a in t:
            player_val+=10
        else:
            word=play_let[play_num.index(a)]
            if word in deal_num:
                player_val+=1
            else:
                player_val+=11
    if player_val<dealer_val:
        print('lost')
    elif player_val>dealer_val:
        print('won')
    else:
        print('hit')