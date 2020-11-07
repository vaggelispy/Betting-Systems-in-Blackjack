from blackjack_generator import bjgenerate
from matplotlib import pyplot as plt

total_games = 100000000
w4 , w3 , w2 , w , bj , d , l , l2 , l3 , l4 , s = 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0

for i in bjgenerate(total_games):
    if i == -1:
        l += 1
    elif i == 1:
        w += 1
    elif i == 1.5:
        bj += 1
    elif i == 0:
        d += 1
    elif i == 2:
        w2 += 1
    elif i == -2:
        l2 += 1
    elif i == 3:
        w3 += 1
    elif i == -3:
        l3 += 1
    elif i == 4:
        w4 += 1
    elif i == -4:
        l4 += 1
    s += i
    
edge = 100*s/(total_games-d)
labels = 'Win', 'Lose', 'Blackjack', 'Push', 'WinX2', 'LoseX2', 'WinX3', 'LoseX3', 'WinX4', 'LoseX4'
labels = 'Win', 'Lose', 'Blackjack', 'Push', 'WinX2', 'LoseX2', '', '', '', ''
sizes = [100*w/total_games, 100*l/total_games, 100*bj/total_games, 100*d/total_games, 100*w2/total_games, 100*l2/total_games, 100*w3/total_games, 100*l3/total_games, 100*w4/total_games, 100*l4/total_games]
sizes2 = [w, l, bj, d, w2, l2, w3, l3, w4, l4]
plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.show()
plt.bar(labels,sizes2)
plt.show()
print(f'Players edge is {round(edge,4)}%\n{100*w/total_games}% Win\n{100*l/total_games}% Lose\n{100*bj/total_games}% Blackjack\n{100*d/total_games}% Push\n{100*w2/total_games}% WinX2\n{100*l2/total_games}% LoseX2\n{100*w3/total_games}% WinX3\n{100*l3/total_games}% LoseX3\n{100*w4/total_games}% WinX4\n{100*l4/total_games}% LoseX4\ntotal games = {total_games}')