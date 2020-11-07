from blackjack_generator import bjgenerate
import betting_systems as bs
from matplotlib import pyplot as plt
from statistics import mean

#Enter the number of the total games
total_games = 100
betlimit = 2000

bet1 , earnings1 , data1 , series1 , datam = 1 , 0 , [] , 0 , []
bet2 , earnings2 , data2 , series2 = 1 , 0 , [] , 0
bet3 , earnings3 , data3 , series3 = 1 , 0 , [] , 0

for i in bjgenerate(total_games):
    
    bet1,earnings1,series1 = bs.oscar(i,bet1,earnings1,series1)
    if bet1 > betlimit:
        bet1 , series1 = 1 , 0
    data1.append(earnings1)
    
    bet2,earnings2,series2 = bs.oscar(i,bet2,earnings2,series2)
    if bet2 > betlimit:
        bet2 = betlimit
    data2.append(earnings2)

    bet3,earnings3,series3 = bs.oscar(i,bet3,earnings3,series3)
    data3.append(earnings3)

    if i != 0:
        datam.append(i)

print(f'Player has {round(100*mean(datam),5)}% advantage/disadvantage.\nOscar bl to 1: Min value = {round(min(data1),2)}, End up with {round(data1[-1],2)}.\nOscar bl to bl: Min value = {round(min(data2),2)}, End up with {round(data2[-1],2)}.\nOscar no bl: Min value = {round(min(data3),2)}, End up with {round(data3[-1],2)}.')
plt.figure(figsize=(12, 7))
plt.plot(data1)
plt.plot(data2)
plt.plot(data3)
plt.legend(["Oscar bl to 1","Oscar bl to bl","Oscar no bl"],loc='lower right')
plt.title("Oscar's System in Long Run")
plt.show()
plt.plot(data1)
plt.title("Oscar's System bl to 1")
plt.show()
plt.plot(data2)
plt.title("Oscar's System bl to bl")
plt.show()
plt.plot(data3)
plt.title("Oscar's System no bl")
plt.show()