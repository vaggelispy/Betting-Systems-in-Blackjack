from random import shuffle
from matplotlib import pyplot as plt

def bj_data(total_games):
    
    def ace_check(a,i,ace,deck):
        total_aces = 0
        for j in range(a,i+1):
            if deck[j] == 11:
                total_aces += 1
            if total_aces == 1 and deck[j] == 11:
                ace = j
            elif total_aces > 1:
                deck[j] = 1    
        return total_aces,ace
    
    cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]
    shuffle(cards)
    deck1 = 4*cards
    shuffle(deck1)
    deck = 8*deck1
    shuffle(deck)
    dealer_startcard , start_card , i = 0 , 1 , 2
    print(f'Shuffled deck: {deck}')
    for games in range(1,total_games + 1):
        if i > 210:
            deck = 8*deck1
            shuffle(deck)
            dealer_startcard , start_card , i = 0 , 1 , 2
            print(f'Shuffled deck: {deck}')
        double , double2 , dealer_ace , ace , player1_value , dealer_ready = 0 , 0 , 0 , 0 , 0 , 0
        split , split_decision , split2_startcard , player1_cards , ace_split = 0 , 0 , 0 , [] , 0
        split_card1 = deck[start_card]
        dealer_card = deck[dealer_startcard]
        print(f'\n{games}) GAME START  dealer_startcard: {dealer_startcard}')
#Game is on.
        for k in range(100):
            stand = i  
#Check if there should be a split or not and calculate the aces.
            if split_decision == 2:
                total_aces,ace = ace_check(split2_startcard,i,ace,deck)
                if total_aces > 0:
                    player2_cards = [split_card1] + deck[split2_startcard:i+1]
                    print(player1_cards , " " , player2_cards)
                    print(" " ,player1_value, 3*len(player1_cards)*" ",sum(player2_cards) - 10, " or ", sum(player2_cards))
                else:
                    player2_cards = [split_card1] + deck[split2_startcard:i+1]
                    print(player1_cards , " " , player2_cards)
                    print(" " ,player1_value, 3*len(player1_cards)*" ",sum(player2_cards)) 
            elif split_decision == 1:
                total_aces,ace = ace_check((start_card + 1),i,ace,deck)
                if total_aces > 0:
                    print(deck[start_card + 1:i+1])
                    print(sum(deck[start_card + 1:i+1]) - 10, " or " , sum(deck[start_card + 1:i+1]))
                else:
                    print(deck[start_card + 1:i+1])
                    print(sum(deck[start_card + 1:i+1]))                
            elif split_decision == 0:
                total_aces,ace = ace_check(start_card,i,ace,deck)
                if deck[start_card+1] == 1 and len(deck[start_card:i+1]) == 2:
                    print(deck[start_card:i+1])
                    print(sum(deck[start_card:i+1]) - 10, " or " , sum(deck[start_card:i+1]))
                    split = 1
                    deck[start_card+1] = 11
                elif deck[start_card] == deck[start_card + 1]:
                    print(deck[start_card:i+1])
                    print(sum(deck[start_card:i+1]))
                    split = 1
                elif total_aces > 0:
                    print(deck[start_card:i+1])
                    print(sum(deck[start_card:i+1]) - 10, " or " , sum(deck[start_card:i+1]))
                else:
                    print(deck[start_card:i+1])
                    print(sum(deck[start_card:i+1]))
#Decision making: Hit Stand Double Split.
            if double == 0 and split_decision == 0: 
                if total_aces == 0:
                    player_cards = deck[start_card:i+1]
                    player_value = sum(deck[start_card:i+1])   
                elif total_aces > 0:
                    player_cards = deck[start_card:i+1]
                    player_value = sum(deck[start_card:i+1])
                    if player_value > 21:
                        deck[ace] = 1
                        player_cards = deck[start_card:i+1]
                        player_value = sum(deck[start_card:i+1])
                if len(player_cards) > 2 and split == 1:
                    split = 0
                if total_aces == 0:
                    if dealer_card == 2 and (player_value <= 9 or player_value == 12) and split == 0:
                        i += 1
                    elif dealer_card == 2 and player_value == 8 and split == 1:
                        i += 1
                    elif dealer_card == 2 and (player_value == 10 or player_value == 11):
                        if len(player_cards) == 2:
                            double = 1
                        i += 1
                    elif dealer_card == 2 and player_value < 19 and split == 1:
                        split_decision = 1
                        i += 1       
                    if dealer_card == 3 and (player_value <= 8 or player_value == 12) and split == 0:
                        i += 1
                    elif dealer_card == 3 and player_value == 8 and split == 1:
                        i += 1
                    elif dealer_card == 3 and player_value >= 9 and player_value <= 11:
                        if len(player_cards) == 2:
                            double = 1
                        i += 1
                    elif dealer_card == 3 and player_value < 19 and split == 1:
                        split_decision = 1
                        i += 1
                    if dealer_card >= 4 and dealer_card <= 6 and player_value <= 8 and split == 0:
                        i += 1
                    elif dealer_card >= 4 and dealer_card <= 6 and player_value >= 9 and player_value <= 11:
                        if len(player_cards) == 2:
                            double = 1
                        i += 1
                    elif dealer_card >= 4 and dealer_card <= 6 and player_value < 19 and split == 1:
                        split_decision = 1
                        i += 1
                    if dealer_card == 7 and player_value <= 9 and split == 0:
                        i += 1
                    elif dealer_card == 7 and player_value >= 10 and player_value <= 11:
                        if len(player_cards) == 2:
                            double = 1
                        i += 1
                    elif dealer_card == 7 and player_value >= 12 and player_value <= 16 and split == 0:
                        i += 1
                    elif dealer_card == 7 and (player_value == 8 or player_value == 12) and split == 1:
                        i += 1
                    elif dealer_card == 7 and player_value < 17 and split == 1:
                        split_decision = 1
                        i += 1
                    if dealer_card >= 8 and dealer_card <= 9 and player_value <= 9 and split == 0:
                        i += 1
                    elif dealer_card >= 8 and dealer_card <= 9 and player_value >= 10 and player_value <= 11:
                        if len(player_cards) == 2:
                            double = 1
                        i += 1
                    elif dealer_card >= 8 and dealer_card <= 9 and player_value >= 12 and player_value <= 16 and split == 0:
                        i += 1
                    elif dealer_card >= 8 and dealer_card <= 9 and player_value < 15 and split == 1:
                        i += 1
                    elif dealer_card >= 8 and dealer_card <= 9 and player_value < 19 and split == 1:
                        split_decision = 1
                        i += 1  
                    if dealer_card >= 10 and dealer_card <= 11 and player_value <= 16 and split == 0:
                        i += 1
                    elif dealer_card >= 10 and dealer_card <= 11 and player_value < 17 and split == 1:
                        i += 1   
                elif total_aces > 0:        
                    if dealer_card >= 2 and dealer_card <= 8 and player_value <= 17 and split == 0:
                        i += 1
                    elif dealer_card >= 2 and dealer_card <= 8 and split == 1:
                        split_decision = 1
                        ace_split = 1
                        i += 1           
                    if dealer_card >= 9 and dealer_card <= 10 and player_value <= 18 and split == 0:
                        i += 1
                    elif dealer_card >= 9 and dealer_card <= 10 and split == 1:
                        split_decision = 1
                        ace_split = 1
                        i += 1           
                    if dealer_card == 11 and player_value <= 18 and split == 0:
                        i += 1
                    elif dealer_card == 11 and  split == 1:
                        i += 1  
#Decision review, form player's cards.
            if split_decision == 0 and total_aces == 0:
                total_aces,ace = ace_check(start_card,i,ace,deck)
                if sum(deck[start_card:i+1]) > 21:
                    deck[ace] = 1
                    player_cards = deck[start_card:i+1]
                    player_value = sum(deck[start_card:i+1])
                    print("dealer's card: ", dealer_card)
                else:
                     player_cards = deck[start_card:i+1]
                     player_value = sum(deck[start_card:i+1])
                     print("dealer's card: ", dealer_card)   
            elif split_decision == 0 and total_aces > 0 and ace_split == 1:
                total_aces,ace = ace_check(start_card,i,ace,deck)
                deck[start_card+1] = 11
                player_cards = deck[start_card:i+1]
                player_value = sum(deck[start_card:i+1])
                print("dealer's card: ", dealer_card)
            elif split_decision == 0 and total_aces > 0:
                total_aces,ace = ace_check(start_card,i,ace,deck)
                if sum(deck[start_card:i+1]) > 21:
                    deck[ace] = 1
                    player_cards = deck[start_card:i+1]
                    player_value = sum(deck[start_card:i+1])
                    print("dealer's card: ", dealer_card)
                else:
                     player_cards = deck[start_card:i+1]
                     player_value = sum(deck[start_card:i+1])
                     print("dealer's card: ", dealer_card)        
            elif split_decision == 1 and double == 0:
                if total_aces == 0:
                    player1_cards = deck[start_card + 1:i+1]
                    player1_value = sum(deck[start_card + 1:i+1])
                elif total_aces > 0:
                    total_aces,ace = ace_check(start_card+1,i,ace,deck)
                    player1_cards = deck[start_card + 1:i+1]
                    player1_value = sum(deck[start_card + 1:i+1])
                    if sum(deck[start_card + 1:i+1]) > 21:
                        deck[ace] = 1
                        player1_cards = deck[start_card + 1:i+1]
                        player1_value = sum(deck[start_card + 1:i+1])
                if total_aces == 0:
                    if dealer_card == 2 and (player1_value <= 9 or player1_value == 12):
                        i += 1
                    elif dealer_card == 2 and (player1_value == 10 or player1_value == 11):
                        if len(player1_cards) == 2:
                            double = 1
                        i += 1       
                    if dealer_card == 3 and (player1_value <= 8 or player1_value == 12):
                        i += 1
                    elif dealer_card == 3 and player1_value >= 9 and player1_value <= 11:
                        if len(player1_cards) == 2:
                            double = 1
                        i += 1
                    if dealer_card >= 4 and dealer_card <= 6 and player1_value <= 8:
                        i += 1
                    elif dealer_card >= 4 and dealer_card <= 6 and player1_value >= 9 and player1_value <= 11:
                        if len(player1_cards) == 2:
                            double = 1
                        i += 1
                    if dealer_card >= 7 and dealer_card <= 9 and player1_value <= 9:
                        i += 1
                    elif dealer_card >= 7 and dealer_card <= 9 and player1_value >= 10 and player1_value <= 11:
                        if len(player1_cards) == 2:
                            double = 1
                        i += 1
                    elif dealer_card >= 7 and dealer_card <= 9 and player1_value >= 12 and player1_value <= 16:
                        i += 1   
                    if dealer_card >= 10 and dealer_card <= 11 and player1_value <= 16:
                        i += 1
                elif total_aces > 0 and ace_split == 0:        
                    if dealer_card >= 2 and dealer_card <= 8 and player1_value <= 17:
                        i += 1            
                    if dealer_card >= 9 and dealer_card <= 11 and player1_value <= 18:
                        i += 1                    
            elif split_decision == 2 and double2 == 0:
                if total_aces == 0:
                    player2_cards = deck[split2_startcard:i+1]
                    player2_cards.insert(0,split_card1)
                    player2_value = sum(player2_cards[:])
                elif total_aces > 0:
                    total_aces,ace = ace_check(split2_startcard,i,ace,deck)
                    player2_cards = deck[split2_startcard:i+1]
                    player2_cards.insert(0,split_card1)
                    player2_value = sum(player2_cards[:])
                    if sum(deck[start_card + 1:i+1]) > 21:
                        deck[ace] = 1
                        player2_cards = deck[split2_startcard:i+1]
                        player2_cards.insert(0,split_card1)
                        player2_value = sum(player2_cards[:])
                if total_aces == 0:
                    if dealer_card == 2 and (player2_value <= 9 or player2_value == 12):
                        i += 1
                    elif dealer_card == 2 and (player2_value == 10 or player2_value == 11):
                        if len(player2_cards) == 2:
                            double2 = 1
                        i += 1      
                    if dealer_card == 3 and (player2_value <= 8 or player2_value == 12):
                        i += 1
                    elif dealer_card == 3 and player2_value >= 9 and player2_value <= 11:
                        if len(player2_cards) == 2:
                            double2 = 1
                        i += 1
                    if dealer_card >= 4 and dealer_card <= 6 and player2_value <= 8:
                        i += 1
                    elif dealer_card >= 4 and dealer_card <= 6 and player2_value >= 9 and player2_value <= 11:
                        if len(player2_cards) == 2:
                            double2 = 1
                        i += 1
                    if dealer_card >= 7 and dealer_card <= 9 and player2_value <= 9:
                        i += 1
                    elif dealer_card >= 7 and dealer_card <= 9 and player2_value >= 10 and player2_value <= 11:
                        if len(player2_cards) == 2:
                            double2 = 1
                        i += 1
                    elif dealer_card >= 7 and dealer_card <= 9 and player2_value >= 12 and player2_value <= 16:
                        i += 1    
                    if dealer_card >= 10 and dealer_card <= 11 and player2_value <= 16:
                        i += 1   
                elif total_aces > 0 and ace_split == 0:        
                    if dealer_card >= 2 and dealer_card <= 8 and player2_value <= 17:
                        i += 1            
                    if dealer_card >= 9 and dealer_card <= 11 and player2_value <= 18:
                        i += 1
            if split_decision == 1 and total_aces == 0:
                player1_cards = deck[start_card + 1:i+1]
                player1_value = sum(deck[start_card + 1:i+1])
                print("dealer's card: ", dealer_card) 
            elif split_decision == 1 and total_aces > 0:
                if sum(deck[start_card + 1:i+1]) > 21:
                    player1_cards = deck[start_card + 1:i+1]
                    player1_value = sum(deck[start_card + 1:i+1]) - 10
                    print("dealer's card: ", dealer_card)
                else:
                     player1_cards = deck[start_card + 1:i+1]
                     player1_value = sum(deck[start_card + 1:i+1])
                     print("dealer's card: ", dealer_card)
            elif split_decision == 2 and total_aces == 0:
                player2_cards = deck[split2_startcard:i+1]
                player2_cards.insert(0,split_card1)
                player2_value = sum(player2_cards[:])
                print("dealer's card: ", dealer_card) 
            elif split_decision == 2 and total_aces > 0:
                if sum(deck[start_card + 1:i+1]) > 21:
                    player2_cards = deck[split2_startcard:i+1]
                    player2_cards.insert(0,split_card1)
                    player2_value = sum(player2_cards[:]) - 10
                    print("dealer's card: ", dealer_card)
                else:
                     player2_cards = deck[split2_startcard:i+1]
                     player2_cards.insert(0,split_card1)
                     player2_value = sum(player2_cards[:])
                     print("dealer's card: ", dealer_card)
#Dealer's turn, player stopped making decisions.    
            if stand == i and split_decision == 1:
                split_decision = 2
                i += 1
                split2_startcard = i    
            elif stand == i and split_decision == 2:
                i += 1
                second_card = i
                if player1_value > 21 and player2_value > 21:
                    dealer = deck[second_card:i+1]
                    dealer.insert(0,dealer_card)
                    dealer_value = sum(dealer[:])
                    dealer_ready = 1
                else:
                    existed_ace = 0
                    if dealer_card == 11:
                        if deck[second_card] == 11:
                            deck[second_card] = 1              
                        while (dealer_card + sum(deck[second_card:i+1])) < 17:
                            i += 1
                            if deck[i] == 11:
                                deck[i] == 1
                            if (dealer_card + sum(deck[second_card:i+1])) > 21:
                                dealer_card = 1
                        dealer = deck[second_card:i+1]
                        dealer.insert(0,dealer_card)
                        dealer_value = sum(dealer[:])
                        dealer_ready = 1
                    elif dealer_card <= 10:
                         if deck[second_card] == 11:
                             dealer_ace = 1
                             existed_ace = second_card
                         while (dealer_card + sum(deck[second_card:i+1])) < 17:
                            i += 1
                            if deck[i] == 11 and dealer_ace == 1:
                                deck[i] == 1
                            elif deck[i] == 11 and dealer_ace == 0:
                                dealer_ace = 1
                                existed_ace = i
                            if existed_ace != 0 and (dealer_card + sum(deck[second_card:i+1])) > 21:
                                deck[existed_ace] == 1
                         dealer = deck[second_card:i+1]
                         dealer.insert(0,dealer_card)
                         dealer_value = sum(dealer[:])
                         dealer_ready = 1    
            elif stand == i and split_decision == 0:
                i += 1
                second_card = i
                if player_value > 21:
                    dealer = deck[second_card:i+1]
                    dealer.insert(0,dealer_card)
                    dealer_value = sum(dealer[:])
                    dealer_ready = 1
                elif player_value == 21 and len(player_cards) == 2 and dealer_card + deck[second_card] < 21:
                    dealer = deck[second_card:i+1]
                    dealer.insert(0,dealer_card)
                    dealer_value = sum(dealer[:])
                    dealer_ready = 1
                else:
                    existed_ace = 0
                    if dealer_card == 11:
                        if deck[second_card] == 11:
                            deck[second_card] = 1              
                        while (dealer_card + sum(deck[second_card:i+1])) < 17:
                            i += 1
                            if deck[i] == 11:
                                deck[i] = 1
                            if (dealer_card + sum(deck[second_card:i+1])) > 21:
                                dealer_card = 1
                        dealer = deck[second_card:i+1]
                        dealer.insert(0,dealer_card)
                        dealer_value = sum(dealer[:])
                        dealer_ready = 1
                    elif dealer_card <= 10:
                         if deck[second_card] == 11:
                             dealer_ace = 1
                             existed_ace = second_card
                         while (dealer_card + sum(deck[second_card:i+1])) < 17:
                            i += 1
                            if deck[i] == 11 and dealer_ace == 1:
                                deck[i] = 1
                            elif deck[i] == 11 and dealer_ace == 0:
                                dealer_ace = 1
                                existed_ace = i
                            if existed_ace != 0 and (dealer_card + sum(deck[second_card:i+1])) > 21:
                                deck[existed_ace] = 1
                         dealer = deck[second_card:i+1]
                         dealer.insert(0,dealer_card)
                         dealer_value = sum(dealer[:])
                         dealer_ready = 1
#Final results, the game is over.  
            if split_decision == 2 and dealer_ready == 1:   
                print("player1: ", player1_cards, player1_value)
                print("player2: ", player2_cards, player2_value)
                print("dealer:\t", dealer, dealer_value)           
                if player1_value > 21:
                    split_bet2a = -1
                    print("dealer win, split1 busted")
                elif dealer_value > 21:
                    if double == 1:
                        split_bet2a = 2
                    elif len(player1_cards) == 2 and player1_value == 21 and ace_split == 0:
                        split_bet2a = 1.5
                        print("Blackjack!")
                    else:
                        split_bet2a = 1
                    print("split1 win, dealer busted")
                elif player1_value > dealer_value:
                    if double == 1:
                        split_bet2a = 2
                    elif len(player1_cards) == 2 and player1_value == 21 and ace_split == 0:
                        split_bet2a = 1.5
                        print("Blackjack!")
                    else:
                        split_bet2a = 1
                    print("split1 wins")
                elif player1_value == dealer_value:
                    if player1_value == 21 and len(player1_cards) == 2 and ace_split == 0:
                        split_bet2a = 1.5
                        print("Blackjack!")
                        print("player wins")
                    elif dealer_value == 21 and len(dealer) == 2:
                        split_bet2a = -1
                        print("dealer wins")
                    else:
                        split_bet2a =  0
                        print("draw")
                elif player1_value < dealer_value:
                    if double == 1:
                        split_bet2a = -2
                    else:
                        split_bet2a = -1
                    print("dealer wins split1")  
                if player2_value > 21:
                    split_bet2b = -1
                    print("dealer win, split2 busted")   
                elif dealer_value > 21:
                    if double2 == 1:
                        split_bet2b = 2
                    elif len(player2_cards) == 2 and player2_value == 21 and ace_split == 0:
                        split_bet2b = 1.5
                        print("Blackjack!")
                    else:
                        split_bet2b = 1
                    print("split2 win, dealer busted")
                elif player2_value > dealer_value:
                    if double2 == 1:
                        split_bet2b = 2
                    elif len(player2_cards) == 2 and player2_value == 21 and ace_split == 0:
                        split_bet2b = 1.5
                        print("Blackjack!")
                    else:
                        split_bet2b = 1
                    print("split2 wins")
                elif player2_value == dealer_value:
                    if player2_value == 21 and len(player2_cards) == 2 and ace_split == 0:
                        split_bet2b = 1.5
                        print("Blackjack!")
                        print("player wins")
                    elif dealer_value == 21 and len(dealer) == 2:
                        split_bet2b = -1
                        print("dealer wins")
                    else:
                        split_bet2b =  0
                        print("draw")
                elif player2_value < dealer_value:   
                    if double2 == 1:
                        split_bet2b = -2
                    else:
                        split_bet2b = -1
                    print("dealer wins split2") 
                yield split_bet2a + split_bet2b
                break        
            elif split_decision == 0 and dealer_ready == 1:  
                print("player:\t", player_cards, player_value)
                print("dealer:\t", dealer, dealer_value)          
                if player_value > 21:
                    yield -1
                    print("dealer wins, player busted")
                elif dealer_value > 21:
                    if double == 1:
                        yield 2
                    elif len(player_cards) == 2 and player_value == 21:
                        yield 1.5
                        print("Blackjack!")
                    else:
                        yield 1
                    print("player wins, dealer busted")
                elif player_value > dealer_value:
                    if double == 1:
                        yield 2
                    elif len(player_cards) == 2 and player_value == 21:
                        yield 1.5
                        print("Blackjack!")
                    else:
                        yield 1
                    print("player wins")
                elif player_value == dealer_value:
                    if player_value == 21 and len(player_cards) == 2 and len(dealer) > 2:
                        yield 1.5
                        print("Blackjack!")
                        print("player wins")
                    elif dealer_value == 21 and len(dealer) == 2 and len(player_cards) > 2:
                        yield -1
                        print("dealer wins")
                    else:
                        yield 0
                        print("draw")
                elif player_value < dealer_value:
                    if double == 1:
                        yield -2
                    else:
                        yield -1
                    print("dealer wins")   
                break
        dealer_startcard = i + 1
        start_card = i + 2
        i += 3

total_games = int(input("Enter how many games you want to play:\t"))  
data , dta , s , w , l , w1 , l1 , w2 , l2 , bj , w3 , l3 , w4 , l4 , d = [] , [] , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0
for n in bj_data(total_games):
    data.append(n)
    s += n
    dta.append(s)
    if n == -1:
        l += 1
        l1 += 1
    elif n == 1:
        w += 1
        w1 += 1
    elif n == 2:
        w += 1
        w2 += 1
    elif n == -2:
        l += 1
        l2 += 1
    elif n == 1.5:
        w += 1
        bj += 1
    elif n == 3:
        w += 1
        w3 += 1
    elif n == 4:
        w += 1
        w4 += 1
    elif n == -3:
        l += 1
        l3 += 1
    elif n == -4:
        l += 1
        l4 += 1
    elif n == 0:
        d += 1
if total_games <= 20:
    dat = []
    for k in data:
        if k == -1:
            dat.append('lose')
        elif k == 1:
            dat.append('win')
        elif k == 2:
            dat.append('winX2')
        elif k == -2:
            dat.append('loseX2')
        elif k == 1.5:
            dat.append('blackjack')
        elif k == 3:
            dat.append('winX3')
        elif k == 4:
            dat.append('winX4')
        elif k == -3:
            dat.append('loseX3')
        elif k == -4:
            dat.append('loseX4')
        elif k == 0:
            dat.append('push')
    print(f'\nOutcome: {dat}\n')
print('\nTotal wins = ', w , ' and Total loses = ', l , '\n w1 = ', w1 , ', l1 = ', l1 ,'\n w2 = ', w2 , ', l2 = ', l2 , '\n  Blackjacks = ', bj , '\n w3 = ', w3 , ', l3 = ', l3 , '\n w4 = ', w4 , ', l4 = ', l4)
if total_games >= 1000:
    plt.bar(['L4','L3','L2','L1','W1','BJ','W2','W3','W4'],[l4,l3,l2,l1,w1,bj,w2,w3,w4])
    plt.title('Results of wins/loses in bars')
    plt.show()
    print(' w1 = ', round(w1*100/(total_games - d),2) , '%, l1 = ', round(l1*100/(total_games - d),2) ,'%\n w2 = ', round(w2*100/(total_games - d),2) , '%, l2 = ', round(l2*100/(total_games - d),2) , '%\n  Blackjacks = ', round(bj*100/(total_games - d),2) , '%\n w3 = ', round(w3*100/(total_games - d),2) , '%, l3 = ', round(l3*100/(total_games - d),2) , '%\n w4 = ', round(w4*100/(total_games - d),2) , '%, l4 = ', round(l4*100/(total_games - d),2) , '%')
    print('Min value = ' , min(dta) , '\tEnd up with = ' , dta[-1])
    plt.plot(dta)
    plt.title('Results of earnings')
    plt.show()
    print(f'Percentage: {100*round(dta[-1],4)/total_games}%')