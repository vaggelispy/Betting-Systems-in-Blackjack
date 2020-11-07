from blackjack_generator import bjgenerate
from statistics import mean

#Enter the number of the total games
total_games = 1000000
#Enter the limit bet at which you want to stop
limits = [20,50,100,200]
mins2 , games2 = [] , []

for winnings in limits:

    g , games , mins , earnings , min1 , d , l = 0 , [] , [] , 0 , 0 , [] , 0

    for i in bjgenerate(total_games):       
        g += 1
        earnings += i
        if earnings < min1:
            min1 = earnings
        if earnings > winnings:
            earnings = 0
            games.append(g-sum(games[:]))
            mins.append(min1)
            min1 = 0

        if g - sum(games[:]) > 10000 and earnings < -100:
            earnings = 0
            games.append(g-sum(games[:]))
            d.append(len(games)-1)
            min1 = 0

        if len(games) - len(d) > 50:
            print(f'{g} broke')
            break
        
    if len(games) == 0:
        games = [0]
        mins = [0]
        
    if len(d) != 0:
        for i in d:
            del games[i-l]
            l += 1
            
    print(f'Winnings = {winnings}\nFlat: mean of games = {round(mean(games))} and mean of min values = {round(mean(mins),2)}\n')
    games2.append(round(mean(games),0))
    mins2.append(round(mean(mins),0))
    print(games,'\t sub: ',d,'\tended leaving ',total_games-sum(games[:]),' games with gains = ',earnings,'\n')
print('Total games in average:\n',games2,'\nTotal min values in average:\n',mins2)