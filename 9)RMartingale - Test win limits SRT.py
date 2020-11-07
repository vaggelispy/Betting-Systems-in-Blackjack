from blackjack_generator import bjgenerate
from matplotlib import pyplot as plt
from statistics import mean

#The following should be added at the end:
#if bet > betlimit:
#   bet ,gains = 1 , 0
#data.append(earnings)
def winlimitim(i,bet,earnings,gains,j):
    gains += i*bet   
    earnings += i*bet
    if i > 0:
        bet *= 2*i
    elif i < 0:
        bet = 1       
    if gains + bet > j:
        bet = j + 1 + gains
        if bet <= 0:
            bet = 1
    if gains > j:
        bet , gains = 1 , 0
    return bet,earnings,gains

#Enter the number of the total games
total_games = 100000
betlimit = 2000
a = 0.4856
#Enter how many repeats
repeats = 500
#Enter the lose limits
j1 , j2 , j3 , j4 , j5 , j6 , j7 , j8 , j9 , j0 = 15 , 20 , 25 , 31 , 40 , 50 , 63 , 80 , 100 , 127
limits = [j1,j2,j3,j4,j5,j6,j7,j8,j9,j0]
ends , ends1 , ends2 , ends3 , ends4 , ends5 , ends6 , ends7 , ends8 , ends9 , ends0 = [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] 
mins , mins1 , mins2 , mins3 , mins4 , mins5 , mins6 , mins7 , mins8 , mins9 , mins0 = [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , []
maxs , maxs1 , maxs2 ,maxs3 , maxs4 , maxs5 , maxs6 , maxs7 , maxs8 , maxs9 , maxs0 = [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , []
 
for j in range(repeats): 
    a = 0.4856
    while a < -0.9712 or a > 0:
        
        bet1 , earnings1 , data1 , gains1 , loss1 = 1 , 0 , [] , 0 , 0
        bet2 , earnings2 , data2 , gains2 , loss2 = 1 , 0 , [] , 0 , 0
        bet3 , earnings3 , data3 , gains3 , loss3 = 1 , 0 , [] , 0 , 0
        bet4 , earnings4 , data4 , gains4 , loss4 = 1 , 0 , [] , 0 , 0
        bet5 , earnings5 , data5 , gains5 , loss5 = 1 , 0 , [] , 0 , 0
        bet6 , earnings6 , data6 , gains6 , loss6 = 1 , 0 , [] , 0 , 0
        bet7 , earnings7 , data7 , gains7 , loss7 = 1 , 0 , [] , 0 , 0
        bet8 , earnings8 , data8 , gains8 , loss8 = 1 , 0 , [] , 0 , 0
        bet9 , earnings9 , data9 , gains9 , loss9 = 1 , 0 , [] , 0 , 0
        bet0 , earnings0 , data0 , gains0 , loss0 = 1 , 0 , [] , 0 , 0
        datam = []
                
        for i in bjgenerate(total_games):
            
            bet1,earnings1,gains1 = winlimitim(i,bet1,earnings1,gains1,j1)
            if bet1 > betlimit:
                bet1 ,gains1 = 1 , 0
            data1.append(earnings1)
            
            bet2,earnings2,gains2 = winlimitim(i,bet2,earnings2,gains2,j2)
            if bet2 > betlimit:
                bet2 ,gains2 = 1 , 0
            data2.append(earnings2)
            
            bet3,earnings3,gains3 = winlimitim(i,bet3,earnings3,gains3,j3)
            if bet3 > betlimit:
                bet3 ,gains3 = 1 , 0
            data3.append(earnings3)
            
            bet4,earnings4,gains4 = winlimitim(i,bet4,earnings4,gains4,j4)
            if bet4 > betlimit:
                bet4 ,gains4 = 1 , 0
            data4.append(earnings4)
            
            bet5,earnings5,gains5 = winlimitim(i,bet5,earnings5,gains5,j5)
            if bet5 > betlimit:
                bet5 ,gains5 = 1 , 0
            data5.append(earnings5)
            
            bet6,earnings6,gains6 = winlimitim(i,bet6,earnings6,gains6,j6)
            if bet6 > betlimit:
                bet6 ,gains6 = 1 , 0
            data6.append(earnings6)
            
            bet7,earnings7,gains7 = winlimitim(i,bet7,earnings7,gains7,j7)
            if bet7 > betlimit:
                bet7 ,gains7 = 1 , 0
            data7.append(earnings7)
            
            bet8,earnings8,gains8 = winlimitim(i,bet8,earnings8,gains8,j8)
            if bet8 > betlimit:
                bet8 ,gains8 = 1 , 0
            data8.append(earnings8)
            
            bet9,earnings9,gains9 = winlimitim(i,bet9,earnings9,gains9,j9)
            if bet9 > betlimit:
                bet9 ,gains9 = 1 , 0
            data9.append(earnings9)
            
            bet0,earnings0,gains0 = winlimitim(i,bet0,earnings0,gains0,j0)
            if bet0 > betlimit:
                bet0 ,gains0 = 1 , 0
            data0.append(earnings0)
            
            if i != 0:
                datam.append(i)
            
        a = 100*mean(datam)
    
    ends1.append(data1[-1])
    mins1.append(min(data1))
    maxs1.append(max(data1))
    ends2.append(data2[-1])
    mins2.append(min(data2))
    maxs2.append(max(data2))
    ends3.append(data3[-1])
    mins3.append(min(data3))
    maxs3.append(max(data3))
    ends4.append(data4[-1])
    mins4.append(min(data4))
    maxs4.append(max(data4))
    ends5.append(data5[-1])
    mins5.append(min(data5))
    maxs5.append(max(data5))
    ends6.append(data6[-1])
    mins6.append(min(data6))
    maxs6.append(max(data6))
    ends7.append(data7[-1])
    mins7.append(min(data7))
    maxs7.append(max(data7))
    ends8.append(data8[-1])
    mins8.append(min(data8))
    maxs8.append(max(data8))
    ends9.append(data9[-1])
    mins9.append(min(data9))
    maxs9.append(max(data9))
    ends0.append(data0[-1])
    mins0.append(min(data0))
    maxs0.append(max(data0))
    endsplot = [data1[-1],data2[-1],data3[-1],data4[-1],data5[-1],data6[-1],data7[-1],data8[-1],data9[-1],data0[-1]]
    plt.plot(limits,endsplot,'b-',alpha=0.1)  
    print(j)
plt.title(f'All {repeats} end ups - Bet limits')
plt.show()
endups = [mean(ends1),mean(ends2),mean(ends3),mean(ends4),mean(ends5),mean(ends6),mean(ends7),mean(ends8),mean(ends9),mean(ends0)]
minvalues = [mean(mins1),mean(mins2),mean(mins3),mean(mins4),mean(mins5),mean(mins6),mean(mins7),mean(mins8),mean(mins9),mean(mins0)]
maxvalues = [mean(maxs1),mean(maxs2),mean(maxs3),mean(maxs4),mean(maxs5),mean(maxs6),mean(maxs7),mean(maxs8),mean(maxs9),mean(maxs0)]
plt.fill_between(limits,maxvalues,color='green',alpha=0.3)
plt.fill_between(limits,minvalues,color='green',alpha=0.3)
plt.plot(limits,minvalues,'r-')
plt.plot(limits,maxvalues,'r-')
plt.plot(limits,endups,'b-')
plt.title('Earnings - Bet limits')
plt.legend(['Mins','Maxes','Ended up','Mins and Maxes'])
plt.show()
plt.plot(limits,endups)
plt.title('Average end ups - Bet limits')
plt.show()