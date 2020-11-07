from blackjack_generator import bjgenerate
from matplotlib import pyplot as plt

total_games = 10000000
d , ls , ws , ls3 , ws3 , ls4 , ws4 , ls5 , ws5 , ls6 , ws6 = 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0


for i in bjgenerate(total_games):

    if i < 0:
        ls += -i
        ws = 0
    elif i > 0:
        ws += int(i)
        ls = 0
    elif i == 0:
        d += 1
    
    if ls == 3:
        ls3 += 1
    elif ls == 4:
        ls4 += 1
    elif ls == 5:
        ls5 += 1
    elif ls == 6:
        ls6 += 1
    elif ws == 3:
        ws3 += 1
    elif ws == 4:
        ws4 += 1
    elif ws == 5:
        ws5 += 1
    elif ws == 6:
        ws6 += 1

labels = 'LS 3' , 'WS 3' , 'LS 4' , 'WS 4' , 'LS 5' , 'WS 5' , 'LS 6' , 'WS 6'
sizes = [ls3, ws3, ls4, ws4, ls5, ws5, ls6, ws6]
plt.bar(labels,sizes)
plt.show()
print(f'Lose Streak 3: {round(100*ls3/(total_games-d),5)}%\nLose Streak 4: {round(100*ls4/(total_games-d),5)}%\nLose Streak 5: {round(100*ls5/(total_games-d),5)}%\nLose Streak 6: {round(100*ls6/(total_games-d),5)}%\nWin Streak 3: {round(100*ws3/(total_games-d),5)}%\nWin Streak 4: {round(100*ws4/(total_games-d),5)}%\nWin Streak 5: {round(100*ws5/(total_games-d),5)}%\nWin Streak 6: {round(100*ws6/(total_games-d),5)}%')