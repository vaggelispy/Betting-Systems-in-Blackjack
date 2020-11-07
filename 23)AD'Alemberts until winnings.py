from blackjack_generator import bjgenerate
import betting_systems as bs
from statistics import mean

def winningplay(gains,i,bet,gains2,earnings,minn,j,betlimit,winnings,games,mins):
    gains += i*bet
    gains2 += i*bet    
    earnings += i*bet
    if i > 0:
        if bet <= i:
            bet = 1
        else:
            bet -= int(i)
    elif i < 0:
        bet += i
    if bet <= 0:
        bet = 1            
    if earnings < minn:
        minn = earnings
    if gains - bet < -j:
        bet = j + 1 + gains
        if bet <= 0:
            bet = 1
    if gains < -j:
        bet , gains = 1 , 0
    if bet > betlimit:
        bet ,gains = 1 , 0      
    if gains2 + bet > winnings:
        bet = winnings + 1 - gains2
        if bet <= 0:
            bet = 1
    if gains2 > winnings:
        bet , earnings , gains , gains2 = 1 , 0 , 0 , 0
        games.append(g-sum(games[:]))
        mins.append(minn)
        minn = 0
    return gains,bet,gains2,earnings,minn,games,mins

#Enter the number of the total games
total_games = 1000000
betlimit = 2000
#Enter the limit bet at which you want to stop
limits = [20,50,100,200]
j2 , j3 , j4 = 10 , 15 , 20
games11 , games22 , games33 , games44 = [] , [] , [] , []
mins11 , mins22 , mins33 , mins44 = [] , [] , [] , []

for winnings in limits:
    
    g , games1 , games2 , games3 , games4 = 0 , [] , [] , [] , []
    mins1 , mins2 , mins3 , mins4 = [] , [] , [] , []
    bet1 , earnings1 , min1 , gains1 , gains11 = 1 , 0 , 0 , 0 , 0
    bet2 , earnings2 , min2 , gains2 , gains22 = 1 , 0 , 0 , 0 , 0
    bet3 , earnings3 , min3 , gains3 , gains33 = 1 , 0 , 0 , 0 , 0
    bet4 , earnings4 , min4 , gains4 , gains44 = 1 , 0 , 0 , 0 , 0
    
    for i in bjgenerate(total_games):
        
        g += 1
        gains1 += i*bet1
        gains11 += i*bet1
        bet1,earnings1 = bs.adalembert(i,bet1,earnings1)
        if earnings1 < min1:
            min1 = earnings1
        if bet1 > betlimit:
            bet1 ,gains1 = 1 , 0      
        if gains11 + bet1 > winnings:
            bet1 = winnings + 1 - gains11
            if bet1 <= 0:
                bet1 = 1
        if gains11 > winnings:
            bet1 , earnings1 , gains1 , gains11 = 1 , 0 , 0 , 0
            games1.append(g-sum(games1[:]))
            mins1.append(min1)
            min1 = 0

        gains2,bet2,gains22,earnings2,min2,games2,mins2 = winningplay(gains2,i,bet2,gains22,earnings2,min2,j2,betlimit,winnings,games2,mins2)
        gains3,bet3,gains33,earnings3,min3,games3,mins3 = winningplay(gains3,i,bet3,gains33,earnings3,min3,j3,betlimit,winnings,games3,mins3)
        gains4,bet4,gains44,earnings4,min4,games4,mins4 = winningplay(gains4,i,bet4,gains44,earnings4,min4,j4,betlimit,winnings,games4,mins4)

        if len(games1) > 50 and len(games2) > 50 and len(games3) > 50 and len(games4) > 50:
            print(f'{g} broke')
            break
    if len(games1) == 0:
        games1 = [0]
        mins1 = [0]
    if len(games2) == 0:
        games2 = [0]
        mins2 = [0]
    if len(games3) == 0:
        games3 = [0]
        mins3 = [0]
    if len(games4) == 0:
        games4 = [0]
        mins4 = [0]

    print(f'Winnings = {winnings}\nAdapted DAlembert without loss limit : mean of games = {round(mean(games1),2)} and mean of min values = {round(mean(mins1),2)}\nAdapted DAlembert with loss limit 15: mean of games = {round(mean(games2),2)} and mean of min values = {round(mean(mins2),2)}\nAdapted DAlembert with loss limit 20: mean of games = {round(mean(games3),2)} and mean of min values = {round(mean(mins3),2)}\nAdapted DAlembert with loss limit 31: mean of games = {round(mean(games4),2)} and mean of min values = {round(mean(mins4),2)}\n')
    games11.append(round(mean(games1),0))
    games22.append(round(mean(games2),0))
    games33.append(round(mean(games3),0))
    games44.append(round(mean(games4),0))
    mins11.append(round(mean(mins1),0))
    mins22.append(round(mean(mins2),0))
    mins33.append(round(mean(mins3),0))
    mins44.append(round(mean(mins4),0))
    print('1)\t',games1,'\tended leaving ',total_games-sum(games1[:]),' games with gains = ',gains11,'\n')
    print('2)\t',games2,'\tended leaving ',total_games-sum(games2[:]),' games with gains = ',gains22,'\n')
    print('3)\t',games3,'\tended leaving ',total_games-sum(games3[:]),' games with gains = ',gains33,'\n')
    print('4)\t',games4,'\tended leaving ',total_games-sum(games4[:]),' games with gains = ',gains44,'\n')
print('Total games in average:\n',games11,'\n',games22,'\n',games33,'\n',games44,'\nTotal min values in average:\n',mins11,'\n',mins22,'\n',mins33,'\n',mins44)