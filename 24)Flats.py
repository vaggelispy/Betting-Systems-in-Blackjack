from blackjack_generator import bjgenerate
from matplotlib import pyplot as plt
from statistics import mean

#Enter the number of the total games
total_games = 100000
#Enter the number of repeats
repeats = 500
ends , bins1 = [] , 10
for j in range(repeats):
    a = 0.4856
    while a < -0.9712 or a > 0:
        earnings , data , datam = 0 , [] , []
        for i in bjgenerate(total_games):          
            earnings += i
            data.append(earnings)           
            if i != 0:
                datam.append(i)
        a = 100*mean(datam)
    print(j)
    ends.append(data[-1])
    plt.plot(data,'b-',alpha=0.05)
plt.title(f'{repeats} games playing Flat')
plt.show()
plt.hist(ends,bins=bins1)
plt.title(f'Times of end up with - {bins1} bins')
plt.show()
print(f'Mean of ends up is {round(100*mean(ends)/total_games,5)}%')