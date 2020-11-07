from random import randrange as r
import numpy as np
from sklearn.linear_model import LinearRegression

def cgenerate(total_games):
    """ Generates casino game outcomes """
    
    for i in range(total_games):
        a = r(37)
        if a <= 18:
            yield -1
        else:
            yield 1
        
        ##BETTING SYSTEMS
#Trioplay with bankroll = 100 units
    #Unfinished?
def trioplay(i,ap1,ap2,result,bank,bankroll,count):
    
    if count[-1] == 12:
        ap2 = 1
    elif count[-1] - count[0] == 5 and ap2 == 0:
        ap1 = 1
    
    if ap2:
        if i > 0:
            result += count[0]
            del count[0]
            if len(count) != 0:
                del count[0]
            if len(count) != 0:
                del count[0]
        elif i < 0:
            result -= count[0]
            count.append(count[-1]+1)
    elif ap1:
        if i > 0:
            result += count[0]
            del count[0]
            if len(count) != 0:
                del count[0]
        elif i < 0:
            result -= count[0]
            count.append(count[-1]+1)
    else:
        if i > 0:
            result += count[0]
            del count[0]
        elif i < 0:
            result -= count[0]
            count.append(count[-1]+1)
        
    if result > 0:
        bank += result
        ap1 , ap2 , result , count = 0 , 0 , 0 , [1]
    elif sum(count) > 100:
        bank += result
        ap1 , ap2 , result , count = 0 , 0 , 0 , [1]
    if len(count) == 0:
        ap1 , ap2 , count = 0 , 0 , [1]
    if bank <= -100 or bank >= 50:
        bankroll += bank
        ap1 , ap2 , result , bank , count = 0 , 0 , 0 , 0 , [1]
        
    return ap1,ap2,result,bank,bankroll,count

#Martingale
def martingale(i,bet,earnings):
    earnings += i*bet
    if i > 0:
        bet = 1
    elif i < 0:
        bet *= 2*(-i)
    return bet,earnings

#Martingale Less Loosy with initial bet = 1
def llmartingale(i,bet,earnings,lose):
    earnings += i*bet
    if i > 0:
        lose = 0
        bet = 1
    elif i < 0:
        lose += i*bet
        bet = -lose + 1
    return bet,earnings,lose

#Revearse Martingale
def rmartingale(i,bet,earnings):
    earnings += i*bet
    if i > 0:
        bet *= 2*i
    elif i < 0:
        bet = 1
    return bet,earnings

#Reverse Martingale Less Loosy with initial bet = 1
def llrmartingale(i,bet,earnings,win):
    earnings += i*bet
    if i > 0:
        win += i*bet
        bet = win + 1
    elif i < 0:
        win = 0
        bet = 1
    return bet,earnings,win

#Climbing
def climbing(i,bet,earnings,winstreak):
    earnings += i*bet
    if i > 0:
        winstreak += 1
        if winstreak <= 2:
            bet = 1
        elif winstreak >= 3:
            bet = 2
        elif winstreak >= 5:
            bet = 3
        elif winstreak >= 7:
            bet = 1
    elif i < 0:
        winstreak = 0
        bet = 1
    return bet,earnings,winstreak
    
#Oscar
def oscar(i,bet,earnings,series):
    earnings += i*bet
    series += i*bet
    if i > 0:
        if series >= 1:
            series = 0
            bet = 1
        elif bet > -series and series < 1:
            bet = 1 - int(series)
        else:
            bet += 1
    return bet,earnings,series

#D'Alembert Adapted
def adalembert(i,bet,earnings):
    earnings += i*bet
    if i > 0:
        if bet <= i:
            bet = 1
        else:
            bet -= int(i)
    elif i < 0:
        bet += i
    if bet <= 0:
        bet = 1
    return bet,earnings

#D'Alembert
def dalembert(i,bet,earnings):
    earnings += i*bet
    if i > 0:
        if bet <= 1:
            bet = 1
        else:
            bet -= 1
    elif i < 0:
        bet += 1
    return bet,earnings

        ##HELPFUL FUNCTIONS
#Linear fit
#x = np.array([i+1 for i in range(total_games)])
def fit(x,data):
    eqfit2 = np.polyfit(x,data,1)
    fit = np.polyval(eqfit2,x)
    eqfit = str(round(eqfit2[0],4))+'x + '+str(round(eqfit2[1],1))
    return eqfit,fit
    
#Linear fit at (0,0)
#x = x[:,np.newaxis]
def fittozero(x,data):
    a, _, _, _ = np.linalg.lstsq(x, data)
    fitzero = a*x
    eqfitzero = str(round(a[0],4))+'x'
    model = LinearRegression().fit(x, data)
    r_sq = model.score(x, data)
    return eqfitzero,fitzero,round(r_sq,4)  