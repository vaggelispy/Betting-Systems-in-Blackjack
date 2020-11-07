from blackjack_generator import bjgenerate
import betting_systems as bs
from matplotlib import pyplot as plt
from statistics import mean

#Enter the number of the total games
total_games = 100000
betlimit = 2000
#Enter the number of repeats
repeats = 500
ends , bins1 , l , w = [] , 10 , 10 , 3
for k in range(repeats):
    a = 0.4856
    while a < -0.9712 or a > 0:
        bet , earnings , data , gains , datam = 1 , 0 , [] , 0 , []
        for i in bjgenerate(total_games):          
            gains += i*bet        
            bet,earnings = bs.adalembert(i,bet,earnings)
            if gains - bet < -l:
                bet = l + 1 + gains
                if bet <= 0:
                    bet = 1
            if gains < -l:
                bet , gains = 1 , 0
            if gains + bet > w:
                bet = w + 1 - gains
                if bet <= 0:
                    bet = 1
            if gains > w:
                bet , gains = 1 , 0
            if bet > betlimit:
                bet = 1
                series = 0
            data.append(earnings) 
            if i != 0:
                datam.append(i)
        a = 100*mean(datam)
    ends.append(data[-1])
    plt.plot(data,'b-',alpha=0.1)
    print(k)
plt.title(f'{repeats} games playing ADAlembert with both win and lose limits')
plt.show()
plt.hist(ends,bins=bins1)
plt.title(f'Times of end up with - {bins1} bins')
plt.show()
print(f'Mean of ends up is {round(100*mean(ends)/total_games,5)}%\nPlaying lose limit = 10, win limit = 3')