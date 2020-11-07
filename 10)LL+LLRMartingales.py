from blackjack_generator import bjgenerate
from matplotlib import pyplot as plt
from statistics import mean

#Enter the number of the total games
total_games = 100000
betlimit = 2000
#Enter the number of repeats
repeats = 500
ends , bins1 = [] , 10
for j in range(repeats):
    a = 0.4856
    while a < -0.9712 or a > 0:
        bet , earnings , data , loss , datam , gains , win = 1 , 0 , [] , 0 , [] , 0 , 0
        for i in bjgenerate(total_games):                      
            gains += i*bet   
            earnings += i*bet
            if i > 0:
                win += i*bet
                bet = win + 1
                loss = 0
            elif i < 0:
                win = 0
                loss += i*bet
                bet = -loss + 1       
            if gains + bet > j:
                bet = j + 1 - gains
                if bet <= 0:
                    bet = 1
            if gains > j:
                bet , gains = 1 , 0
            if gains - bet < -j:
                bet = j + 1 + gains
                if bet <= 0:
                    bet = 1
            if gains < -j:
                bet , gains = 1 , 0
            if bet > betlimit:
                bet , loss , win = 1 , 0 , 0
            data.append(earnings)           
            if i != 0:
                datam.append(i)
        a = 100*mean(datam)
    print(j)
    ends.append(data[-1])
    plt.plot(data,'b-',alpha=0.1)
plt.title(f'{repeats} games playing LLMartingale')
plt.show()
plt.hist(ends,bins=bins1)
plt.title(f'Times of end up with - {bins1} bins')
plt.show()
print(f'Mean of ends up is {round(100*mean(ends)/total_games,5)}%')