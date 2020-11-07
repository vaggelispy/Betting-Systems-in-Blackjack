from blackjack_generator import bjgenerate
import betting_systems as bs
from matplotlib import pyplot as plt
from statistics import mean

#Enter the number of the total games
total_games = 1000000
betlimit = 2000

bet1 , earnings1 , data1 , datam = 1 , 0 , [] , []
bet2 , earnings2 , data2 = 1 , 0 , []
bet3 , earnings3 , data3 = 1 , 0 , []
bet4 , earnings4 , data4 = 1 , 0 , []
bet5 , earnings5 , data5 = 1 , 0 , []
bet6 , earnings6 , data6 = 1 , 0 , []

for i in bjgenerate(total_games):
    
    bet1,earnings1 = bs.dalembert(i,bet1,earnings1)
    if bet1 > betlimit:
        bet1 = 1
    data1.append(earnings1)
    
    bet2,earnings2 = bs.dalembert(i,bet2,earnings2)
    if bet2 > betlimit:
        bet2 = betlimit
    data2.append(earnings2)

    bet3,earnings3 = bs.dalembert(i,bet3,earnings3)
    data3.append(earnings3)
    
    bet4,earnings4 = bs.adalembert(i,bet4,earnings4)
    if bet4 > betlimit:
        bet4 = 1
    data4.append(earnings4)
    
    bet5,earnings5 = bs.adalembert(i,bet5,earnings5)
    if bet5 > betlimit:
        bet5 = betlimit
    data5.append(earnings5)

    bet6,earnings6 = bs.adalembert(i,bet6,earnings6)
    data6.append(earnings6)

    if i != 0:
        datam.append(i)

print(f'Player has {round(100*mean(datam),5)}% advantage/disadvantage.\nDAlembert bl to 1: Min value = {round(min(data1),2)}, End up with {round(data1[-1],2)}.\nDAlembert bl to bl: Min value = {round(min(data2),2)}, End up with {round(data2[-1],2)}.\nDAlembert no bl: Min value = {round(min(data3),2)}, End up with {round(data3[-1],2)}.\nADAlembert bl to 1: Min value = {round(min(data4),2)}, End up with {round(data4[-1],2)}.\nADAlembert bl to bl: Min value = {round(min(data5),2)}, End up with {round(data5[-1],2)}.\nADAlembert no bl: Min value = {round(min(data6),2)}, End up with {round(data6[-1],2)}.')
plt.plot(data1)
plt.plot(data2)
plt.plot(data3)
plt.legend(["D'Alembert bl to 1","D'Alembert bl to bl","D'Alembert no bl"])
plt.title("D'Alembert System in Long Run")
plt.show()
plt.plot(data1)
plt.title("D'Alembert System bl to 1")
plt.show()
plt.plot(data2)
plt.title("D'Alembert System bl to bl")
plt.show()
plt.plot(data3)
plt.title("D'Alembert System no bl")
plt.show()
plt.plot(data4)
plt.plot(data5)
plt.plot(data6)
plt.legend(["AD'Alembert bl to 1","AD'Alembert bl to bl","AD'Alembert no bl"])
plt.title("AD'Alembert System in Long Run")
plt.show()
plt.plot(data4)
plt.title("AD'Alembert System bl to 1")
plt.show()
plt.plot(data5)
plt.title("AD'Alembert System bl to bl")
plt.show()
plt.plot(data6)
plt.title("AD'Alembert System no bl")
plt.show()