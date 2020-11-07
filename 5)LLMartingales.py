from blackjack_generator import bjgenerate
import betting_systems as bs
from matplotlib import pyplot as plt
from statistics import mean

#Enter the number of the total games
total_games = 100000
betlimit = 2000
#Enter the number of repeats
repeats = 1000
ends , bins1 = [] , 10
for j in range(repeats):
    a = 0.4856
    while a < -0.9712 or a > 0:
        bet , earnings , data , loss , datam = 1 , 0 , [] , 0 , []
        for i in bjgenerate(total_games):          
            bet,earnings,loss = bs.llmartingale(i,bet,earnings,loss)
            if bet > betlimit:
                bet = 1
                loss = 0
            data.append(earnings)           
            if i != 0:
                datam.append(i)
        a = 100*mean(datam)
    ends.append(data[-1])
    plt.plot(data,'b-',alpha=0.1)
plt.title(f'{repeats} games playing LLMartingale')
plt.show()
plt.hist(ends,bins=bins1)
plt.title(f'Times of end up with - {bins1} bins')
plt.show()
print(f'Mean of ends up is {round(100*mean(ends)/total_games,5)}%')