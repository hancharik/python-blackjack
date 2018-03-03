import time
from random import randint
from decimal import *

results = []
start_time = time.ctime()
verbose_mode = False

for i in range(0,55):

    winnings = []
    how_many_times = 1000
    #start_time = time.ctime()
    number_of_decks = 1
    bot_risk_level = -4 + (2*i)# an int representing a percentage, 60 is normal

    for i in range(1,how_many_times):

        money = 100
        deck = []
        random_card = '3H'
        suit = ':D'
        player_hand = []
        opponent_hand = []
        slow = False

        def countq(x):
            total = ''
            for i in range(len(x)):
                total = total + x[i][0]#randint(1,10) #print(x[i][0])#
            return total

        def count(x):
            total = 0
            for i in range(len(x)):
                if x[i][0] == '1':
                    total = total + 10
                elif x[i][0] == 'J':
                    total = total + 10
                elif x[i][0] == 'Q':
                    total = total + 10
                elif x[i][0] == 'K':
                    total = total + 10
                elif x[i][0] == 'A':
                    total = total + 11
                else:
                    total = total + int(x[i][0])#randint(1,10) #print(x[i][0])#
            return total


        def ace_count(x):
            total = 0
            for i in range(len(x)):
                if x[i][0] == '1':
                    total = total + 10
                elif x[i][0] == 'J':
                    total = total + 10
                elif x[i][0] == 'Q':
                    total = total + 10
                elif x[i][0] == 'K':
                    total = total + 10
                elif x[i][0] == 'A':
                    total = total + 1
                else:
                    total = total + int(x[i][0])#randint(1,10) #print(x[i][0])#
            return total

        #https://stackoverflow.com/questions/354038/how-do-i-check-if-a-string-is-a-number-float
        def is_int(s):
            try:
                int(s)
                return True
            except ValueError:
                return False

        def enforce_limit(x):
            if x > 100:
                if verbose_mode:
                    print('max bet is $100')
                x = 100
            if x > money:
                if verbose_mode:
                    print('you only have $' + str(money))
                x = money
            return x


        def intro():
            if verbose_mode:
                print('\n\nyou have $' + str(money) + ', deck is at ' + str(len(deck)) + ' cards')


        def odds(x, y):
            if y < 2:
                y = 2
            if y > 11:
                y = 11
            possibles = [0,0,0,0,0,0,0,0,0,0]
            for i in range(len(x)):
                if x[i][0] == '1':
                    possibles[8] = possibles[8] + 1
                elif x[i][0] == 'J':
                    possibles[8] = possibles[8] + 1
                elif x[i][0] == 'Q':
                    possibles[8] = possibles[8] + 1
                elif x[i][0] == 'K':
                    possibles[8] = possibles[8] + 1
                elif x[i][0] == 'A':
                    possibles[9] = possibles[9] + 1
                else:
                    possibles[(int(x[i][0]) - 2)] = possibles[(int(x[i][0]) - 2)] + 1 #randint(1,10) #print(x[i][0])#
            #print(possibles)
            numerator = 0
            denominator = len(x)
            for i in range(y-1):
                numerator = numerator + possibles[i]
            odds_are = int((numerator / denominator)*100)
            if verbose_mode:
                print('the chance of getting a ' + str(y) + ' or less is ' + str(odds_are) +'%')


        def return_odds(x, y):
            if y < 2:
                y = 2
            if y > 11:
                y = 11
            possibles = [0,0,0,0,0,0,0,0,0,0]
            for i in range(len(x)):
                if x[i][0] == '1':
                    possibles[8] = possibles[8] + 1
                elif x[i][0] == 'J':
                    possibles[8] = possibles[8] + 1
                elif x[i][0] == 'Q':
                    possibles[8] = possibles[8] + 1
                elif x[i][0] == 'K':
                    possibles[8] = possibles[8] + 1
                elif x[i][0] == 'A':
                    possibles[9] = possibles[9] + 1
                else:
                    possibles[(int(x[i][0]) - 2)] = possibles[(int(x[i][0]) - 2)] + 1 #randint(1,10) #print(x[i][0])#
            #print(possibles)
            numerator = 0
            denominator = len(x)
            for i in range(y-1):
                numerator = numerator + possibles[i]
            odds_are = int((numerator / denominator)*100)
            #print('the chance of getting a ' + str(y) + ' or less is ' + str(odds_are) +'%')
            return odds_are



        def check_for_ace(x):
            is_ace = False
            for i in range(len(x)):
                if x[i][0] == 'A':
                    is_ace = True
            return is_ace

        def check_for_need():
            if count(opponent_hand) >= 17:
                if count(opponent_hand) > count(player_hand):
                    if verbose_mode:
                        print('\nyou need to hit or you will lose this hand.')
                elif count(opponent_hand) < count(player_hand):
                    if verbose_mode:
                        print('\nstand here! you win!')
                else:
                    if verbose_mode:
                        print('\nstand here to push.')
            else:
                if count(player_hand) > 11:
                    if verbose_mode:
                        print('\nstanding here may be wise. the dealer may bust.')
                else:
                    if verbose_mode:
                        print('you can hit here')


        def odds_adjuster(x):
            adjusted_odds = x
            if x < 1:
                adjusted_odds = 1
            return adjusted_odds


        def show_odds():
            player_points = count(player_hand)
            if  player_points > 21:
                player_points = ace_count(player_hand)
            if verbose_mode:
                print('\nfor you ('+str(player_points)+'):')
            odds(deck, odds_adjuster(21 - player_points))
            if verbose_mode:
                print('for the dealer ('+str(count(opponent_hand))+'):')
            odds(deck, odds_adjuster(21 - count(opponent_hand)))
            check_for_need()


        #ik = randint(0,4)
        for j in range(0, number_of_decks):
            for i in range(0,4):
                if i == 0:
                    suit = 'h'
                elif i == 1:
                    suit = 'd'
                elif i == 2:
                    suit = 'C'
                else:
                    suit = 'S'


                for i in range(2,15):
                    random_card = str(i) + suit
                    if i == 11:
                        random_card = 'J' + suit
                    elif i == 12:
                        random_card = 'Q' + suit
                    elif i == 13:
                        random_card = 'K' + suit
                    elif i == 14:
                        random_card = 'A' + suit
                    deck.append(random_card)

        #print(deck)
        #print('should be 52: ' + str(len(deck)))

        while len(deck) > 10:
            intro()
            #bet = input('how much do you bet?\n')
            if money > 0:
                deck_size = len(deck)
                bet_variance = 10 + (104 - (deck_size*2))
                #print('bet bot thinks the bet variance should be: ' + str(bet_variance))
                bet = 54 - len(deck)#bet = randint(1,bet_variance)#randint(1,money)#
            else:
                bet = 0
            if slow:
                time.sleep(4)
            if is_int(bet):
                bet = enforce_limit(int(bet))
                if verbose_mode:
                    print('bet is $' + str(bet) + '\n')
                if slow:
                    time.sleep(4)
            else:
                if verbose_mode:
                    print('\n\nhey, how about we just put you down for $100...')
                bet = 100
                if verbose_mode:
                    print('bet is $' + str(bet))
            player_hand = []
            opponent_hand = []
            for i in range(2):
                temp_card = deck[randint(0,len(deck)-1)]
                player_hand.append(temp_card)
                deck.remove(temp_card)
                temp_card = deck[randint(0,len(deck)-1)]
                opponent_hand.append(temp_card)
                deck.remove(temp_card)

            if verbose_mode:
                print('***********************************************')
                print('\nplayer hand: ')
                print(player_hand)
                #print(countq(player_hand))
                print(str(count(player_hand)))


                print('\n\ndealer hand:')
                print(opponent_hand)
                #print(countq(opponent_hand))
                print(str(count(opponent_hand)))
                print('\n***********************************************\n\n')
            continuing = True
            while continuing:

                if ace_count(player_hand) < 21:

                    if count(player_hand) == 21:
                        continuing = False
                        if verbose_mode:
                            print('\n\nBLACKJACK!!!\n\n')
                    else:
                        show_odds()
                        chance_here = return_odds(deck, 21 - count(player_hand))
                        if verbose_mode:
                            print('there is a ' + str(chance_here) + '% chance here ')
                        if chance_here > bot_risk_level:
                            response = 1#input('\n\nHit or stand?')
                        else:
                            if count(opponent_hand) >= 17:
                                if count(opponent_hand) > count(player_hand):
                                    response = 1
                                else:
                                    response = 2
                            else:
                                response = 2
                        if slow:
                            time.sleep(4)


                        if response == 1:#'h':
                            if verbose_mode:
                                print('\n\nhit...\n\n')
                            temp_card = deck[randint(0,len(deck)-1)]
                            player_hand.append(temp_card)
                            deck.remove(temp_card)
                            player_points = count(player_hand)
                            if  player_points > 21:
                                player_points = ace_count(player_hand)
                            if verbose_mode:
                                print('you draw the ' + temp_card  + ', you have ' + str(player_points))
                                print(player_hand)
                        elif response == 2:#'s':
                            if verbose_mode:
                                print('\n\nstand.\n\n')
                            player_points = count(player_hand)
                            if  player_points > 21:
                                player_points = ace_count(player_hand)
                            if verbose_mode:
                                print('standing with ' + str(player_points))
                                print(player_hand)
                            continuing = False
                        else:
                            if verbose_mode:
                                print('\n\nwhat? i didn\'t understand that.')
                else:
                    if ace_count(player_hand) == 21:
                        if verbose_mode:
                            print('blackjack!')
                    else:
                        if verbose_mode:
                            print('\n\nBusted!\n\n')
                    continuing = False

                        #print(player_hand)

            if ace_count(player_hand) < 22:
                if count(opponent_hand) > 16:
                    if verbose_mode:
                        print('dealer stands at ' + str(count(opponent_hand)))
                else:
                    while ace_count(opponent_hand) < 17:
                        range_holder = len(deck)-1
                        # this is an attempt to fix the 10k breaking issue
                        #if range_holder < 1:
                            #range_holder = 1
                        if len(deck) > 0:
                            temp_card = deck[randint(0,range_holder)]
                            opponent_hand.append(temp_card)#.insert(len(opponent_hand)-1,temp_card)

                        else:
                            deck.remove(temp_card)
                            #print('\n\n************************\ndeck length is < 1' + str(len(deck)) + '\n***********************************\n\n')
                            break

                        if verbose_mode:
                            print('\n\ndealer draws ' + temp_card  + ', dealer has ' + str(ace_count(opponent_hand)))
                            print(opponent_hand)


            player_points = count(player_hand)
            if  player_points > 21:
                player_points = ace_count(player_hand)

            dealer_points = count(opponent_hand)
            if  dealer_points > 21:
                dealer_points = ace_count(opponent_hand)


            if  player_points > dealer_points:
                if player_points > 21:
                    if verbose_mode:
                        print('\n\nyou loose! (' + str(player_points) + ')')
                    money = money - bet
                else:
                    if verbose_mode:
                        print('\n\nyou win! ' + 'you (' + str(player_points) + '), dealer (' + str(dealer_points) + ')')
                    money = money + bet
            else:
                if dealer_points > 21:
                    if verbose_mode:
                        print('\n\ndealer busts! you win! (' + str(player_points) + ')')
                    money = money + bet
                elif dealer_points == player_points:
                    if verbose_mode:
                        print('push.'+ '  you (' + str(player_points) + '), dealer (' + str(dealer_points) + ')')
                else:
                    if verbose_mode:
                        print('\n\nyou lose! you are a big loser!'+ ' \nyou (' + str(player_points) + '), dealer (' + str(dealer_points) + ')')
                    money = money - bet


        if verbose_mode:
            print('\n\nI need to reshuffle, ' + str(len(deck)) + ' cards left...')
            print('you have $' + str(money))
        winnings.append(money)
    #for i in range(52):
    #    temp_card = deck[randint(0,len(deck)-1)]
    #    print('removing ' + temp_card)
    #    deck.remove(temp_card)
    #    print('should be 51: ' + str(len(deck)))

    #print(deck)
    #print('should be 1: ' + str(len(deck)))
    total_winnings = Decimal('0.00')
    for item in winnings:
        total_winnings = total_winnings + item
    starting_bank = Decimal('100.00')
    total_adjusted_winnings = total_winnings - (starting_bank * how_many_times)

    average_total_winnings = (total_winnings/how_many_times) - starting_bank

    end_time = time.ctime()
    print('\nstart time ' + str(start_time) +  '\n  end time ' + str(end_time) + '\n')
    print(str(how_many_times) + ' times, (bot = ' + str(bot_risk_level) + '), decks = ' + str(number_of_decks) + ', $' + str(average_total_winnings) )
    if verbose_mode:
        print('start time ' + str(start_time) +  '\n  end time ' + str(end_time))
        print('\n\nfor ' + str(how_many_times) + ' times through ' + str(number_of_decks) + ' decks, your average total winnings were: $' + str(average_total_winnings) )
        print('\nmax winnings = $' + str(max(winnings)) + ',  adjusted winnings = $' + str(total_adjusted_winnings))#+ ',  total winnings = $' + str(total_winnings))
        #result_string = '(' + str(how_many_times) + '), bot: ' + str(bot_risk_level) +', $' + str(average_total_winnings)
    bag = []
    bag.append(float(average_total_winnings))
    bag.append(bot_risk_level)
    bag.append(how_many_times)


    results.append(bag)#results.append(result_string)

#print(results)

for each in results:
    print(each)

#for each in results:
    #print(each[2])


max_bot_value = max(results)
print('max return = $' + str(max_bot_value[0]) + ', bot value = ' + str(max_bot_value[1]) + '%')

end_time = time.ctime()
print('start time ' + str(start_time) +  '\n  end time ' + str(end_time))
file_name = 'auto_winnings_bigbet' + str(how_many_times) + '.txt'
outfile = open(file_name, 'wt')
for item in results:
  print(str(item), file=outfile)#print(", ".join(str(item)), file=outfile)#
#print('max return = $' + str(max_bot_value[0]) + ', bot value = ' + str(max_bot_value[1]) + '%')
outfile.close()
print('finished writing to ' + file_name + '.\n')
file_name = 'auto_winnings_time' + str(how_many_times) + '.txt'
outfile = open(file_name, 'wt')
print('for ' + str(how_many_times) + ' cycles:', file=outfile)
print('start time ' + str(start_time), file=outfile)
print('end time ' + str(end_time), file=outfile)
#print(", ".join(str(item)), file=outfile)#
#print('max return = $' + str(max_bot_value[0]) + ', bot value = ' + str(max_bot_value[1]) + '%')
outfile.close()
print('finished writing to ' + file_name + '.\n')
