from blackjack_generator import bjgenerate
import betting_systems as bs
from matplotlib import pyplot as plt
from statistics import mean
import numpy as np

#Comparing 4 specific betting systems
betting_system1 = 'Martingale, bl to bl'
betting_system2 = 'Martingale, bl to 1'
betting_system3 = 'LLMartingale, bl to bl'
betting_system4 = 'LLMartingale, bl to 1'

#Enter the number of the total games
total_games = 1000000
betlimit = 2000

win3 , win4 = 0 , 0
earnings , datam = 0 , []
bet1 , earnings1 , data1 = 1 , 0 , []
bet2 , earnings2 , data2 = 1 , 0 , []
bet3 , earnings3 , data3 = 1 , 0 , []
bet4 , earnings4 , data4 = 1 , 0 , []

for i in bjgenerate(total_games):
    
    bet1,earnings1 = bs.martingale(i,bet1,earnings1)
    if bet1 > betlimit:
        bet1 = betlimit
    data1.append(earnings1)
    
    bet2,earnings2 = bs.martingale(i,bet2,earnings2)
    if bet2 > betlimit:
        bet2 = 1
    data2.append(earnings2)
    
    bet3,earnings3,win3 = bs.llmartingale(i,bet3,earnings3,win3)
    if bet3 > betlimit:
        bet3 = betlimit
    data3.append(earnings3)
    
    bet4,earnings4,win4 = bs.llmartingale(i,bet4,earnings4,win4)
    if bet4 > betlimit:
        bet4 = 1
    data4.append(earnings4)
    
    if i != 0:
        datam.append(i)

x = np.array([i+1 for i in range(total_games)])
eqfit1,fit1 = bs.fit(x,data1)
eqfit2,fit2 = bs.fit(x,data2)
eqfit3,fit3 = bs.fit(x,data3)
eqfit4,fit4 = bs.fit(x,data4)
x = x[:,np.newaxis]
eqfitzero1,fitzero1,r_sq1 = bs.fittozero(x,data1)
eqfitzero2,fitzero2,r_sq2 = bs.fittozero(x,data2)
eqfitzero3,fitzero3,r_sq3 = bs.fittozero(x,data3)
eqfitzero4,fitzero4,r_sq4 = bs.fittozero(x,data4)

print(f'Martingale\nPlayer has {round(100*mean(datam),5)}% advantage/disadvantage.\n{betting_system1}: Min value = {round(min(data1),2)}, End up with {round(data1[-1],2)}.\n{betting_system2}: Min value = {round(min(data2),2)}, End up with {round(data2[-1],2)}.')
plt.plot(data1)
plt.plot(data2)
plt.title("Martingale Long-Run")
plt.legend([betting_system1,betting_system2])
plt.show()
print(f'Fit: {eqfit1}, Fit at O: {eqfitzero1}, Coefficient of Determination = {r_sq1}')
plt.plot(data1)
plt.plot(fit1)
plt.plot(fitzero1)
plt.title("Martingale Long-Run")
plt.legend([betting_system1,eqfit1,eqfitzero1])
plt.show()
print(f'Fit: {eqfit2}, Fit at O: {eqfitzero2}, Coefficient of Determination = {r_sq2}')
plt.plot(data2)
plt.plot(fit2)
plt.plot(fitzero2)
plt.title("Martingale Long-Run")
plt.legend([betting_system2,eqfit2,eqfitzero2])
plt.show()
print(f'LLMartingale\nPlayer has {round(100*mean(datam),5)}% advantage/disadvantage.\n{betting_system3}: Min value = {round(min(data3),2)}, End up with {round(data3[-1],2)}.\n{betting_system4}: Min value = {round(min(data4),2)}, End up with {round(data4[-1],2)}.')
plt.plot(data3)
plt.plot(data4)
plt.title("LLMartingale Long-Run")
plt.legend([betting_system3,betting_system4])
plt.show()
print(f'Fit: {eqfit3}, Fit at O: {eqfitzero3}, Coefficient of Determination = {r_sq3}')
plt.plot(data3)
plt.plot(fit3)
plt.plot(fitzero3)
plt.title("LLMartingale Long-Run")
plt.legend([betting_system3,eqfit3,eqfitzero3])
plt.show()
print(f'Fit: {eqfit4}, Fit at O: {eqfitzero4}, Coefficient of Determination = {r_sq4}')
plt.plot(data4)
plt.plot(fit4)
plt.plot(fitzero4)
plt.title("LLMartingale Long-Run")
plt.legend([betting_system4,eqfit4,eqfitzero4])
plt.show()
print(f'Martingale\nPlayer has {round(100*mean(datam),5)}% advantage/disadvantage.\n{betting_system1}: Min value = {round(min(data1),2)}, End up with {round(data1[-1],2)}.\n{betting_system2}: Min value = {round(min(data2),2)}, End up with {round(data2[-1],2)}.')
print(f'Fit: {eqfit1}, Fit at O: {eqfitzero1}, Coefficient of Determination = {r_sq1}')
print(f'Fit: {eqfit2}, Fit at O: {eqfitzero2}, Coefficient of Determination = {r_sq2}')
print(f'LLMartingale\nPlayer has {round(100*mean(datam),5)}% advantage/disadvantage.\n{betting_system3}: Min value = {round(min(data3),2)}, End up with {round(data3[-1],2)}.\n{betting_system4}: Min value = {round(min(data4),2)}, End up with {round(data4[-1],2)}.')
print(f'Fit: {eqfit3}, Fit at O: {eqfitzero3}, Coefficient of Determination = {r_sq3}')
print(f'Fit: {eqfit4}, Fit at O: {eqfitzero4}, Coefficient of Determination = {r_sq4}')