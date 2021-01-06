
#importing os module for the clear() finction
import os
def clear():
    os.system( 'cls' )
import random 

#suits,ranks and values.
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace': 1 }

#creating a card class
class Card :
    
    def __init__ (self,suit,rank,value) :
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    def __str__ (self) :
        return self.rank + " of " + self.suit
    def show(self) : 
        return str(self.rank + " of " + self.suit)
    pass
#creating and shuffing deck
def shuffle_deck():
    deck = []
    for suit in suits :
        for rank,value in list(zip(ranks,list(values.values()))):
            deck.append(Card(suit,rank,values[rank]))
    random.shuffle(deck)
    return deck
shuffle_deck = shuffle_deck()
#function that performs the action of hit
def hit(is_player) :
    if is_player : 
        player_cards.append(shuffle_deck[0])
        shuffle_deck.pop(0)
        pass
    else :
        dealer_cards.append(shuffle_deck[0])
        shuffle_deck.pop(0)
        pass
    pass

#caluclates the sum of player's cards in the intrest of player
def player_sum() :
    player_sum = 0 
    no_of_aces = 0
    for player_card in player_cards :
        player_sum += player_card.value
        if player_card.rank == "Ace":
            no_of_aces += 1
            pass
        else :
            pass
    while no_of_aces > 0 :
        if player_sum + 10 <= 21 :
            player_sum += 10
            pass
        else :
            pass
        no_of_aces = no_of_aces -1
        pass

    return player_sum
#caluclates the sum of dealer's cards in the intrest of dealer
def dealer_sum() :
    dealer_sum = 0 
    no_of_aces = 0
    for dealer_card in dealer_cards :
        dealer_sum += dealer_card.value
        if dealer_card.rank == "Ace" :
            no_of_aces += 1
            pass
        else :
            pass
    while no_of_aces > 0 :
        if dealer_sum + 10 :
            dealer_sum += 10
            pass
        else :
            pass 
        no_of_aces = no_of_aces -1
        pass
    return (dealer_sum)
#caluculates the sum that is to be displayed to player 
def display_dealer_sum() :
    display_dealer_sum = 0
    dealer_faceup_cards = [dealer_card for dealer_card in dealer_cards]# actually just written dealer_faceup_cards = dealer_cards //but it does not work that way as python gets confused and just replaces dealerxcards with an emptylist(i.e dealer_faceup_cards)
    dealer_faceup_cards.reverse()
    dealer_faceup_cards.pop()
    no_of_aces = 0
    for dealer_card in dealer_faceup_cards :
        display_dealer_sum += dealer_card.value
        if dealer_card.rank == "Ace" :
            no_of_aces += 1
            pass
        else :
            pass
    while no_of_aces > 0 :
        if display_dealer_sum + 10 :
            display_dealer_sum += 10
            pass
        else :
            pass 
        no_of_aces = no_of_aces -1
        pass
    return (display_dealer_sum)

#function to display game
def display_game(game_ended) :
    #Game Name
    print(" ")
    print(" " + "_"*75)
    print("|" + " "*75 + "|")
    print("|" + " "*32 +"BLACKJACK"+ " "*34 + "|")
    print("|" + " "*75 + "|")
    print(" " + "-"*75)
    #create a display list for both dealer's and player's cards
    if len(player_cards) > len(dealer_cards) :
        display_player_cards = [card.show() for card in player_cards]
        display_dealer_cards = [card.show() for card in dealer_cards]
        while len(display_player_cards) > len(display_dealer_cards) :
            display_dealer_cards.append(" ")
            pass
        pass
    else :
        display_player_cards = [card.show() for card in player_cards]
        display_dealer_cards = [card.show() for card in dealer_cards]
        while len(display_dealer_cards) >len(display_player_cards):
            display_player_cards.append(" ")
            pass
        pass
    print("Player's Cards" + " "*(50 - len("player cards")) + "Dealer's cards")
    if game_ended :
        #displaying all cards of player and dealer
        for player_card,dealer_card in list(zip(display_player_cards,display_dealer_cards)):
            print(player_card + " "*(50-len(player_card)) + dealer_card)
            pass
        print("\n")
        print ("The sum of player is : %d \nThe sum of the dealer is : %d "  %(player_sum(),dealer_sum()))
        print("\n")
        pass 
    else :
        #masking the face down card of dealer
        display_dealer_cards.reverse()
        display_dealer_cards.pop()
        display_dealer_cards.append("xxxxxxxxxxxxx")
        display_dealer_cards.reverse()
        #displaying all the face up cards
        for player_card,dealer_card in list(zip(display_player_cards,display_dealer_cards)):
            print(player_card + " "*(50-len(player_card)) + dealer_card)
            pass
        print("\n")
        #only showing the sum of player's cards and sum of face up cards of dealer
        print ("The sum of player is : %d \nThe sum of the dealer is : %d + something"  %(player_sum(),display_dealer_sum()))
        print("\n")
        pass
    pass
 

    


def rules() :
    print(" ")
    print(" " + "_"*75)
    print("|" + " "*75 + "|")
    print("|" + " "*30 +"RULES of BACKJACK"+ " "*28 + "|")
    print("|" + " "*75 + "|")
    print("|" + " #This is simplified version of back Jack" + " "*34+ "|")
    print("|" + " #The game has 2 players player(i.e you) and dealer(in this case computer) " + "|")
    print("|" + " #The game begins with 2 players recieving 2 cards from a shuffeled deck   " + "|")
    print("|" + " #Both of the player cards are faced up and dealer's cards one is faceup   " + "|")
    print("|" + "  and other is face down" + " "*51 + "|")
    print("|" + " #The palyer now places his bet" + " "*44 + "|")
    print("|" + " #The player goes first he has to choose to hit or stay" + " "*20 +"|")
    print("|" + " #Hit means the player needs to draw a card from deck" + " "*22 + "|")
    print("|" + " #At some point player chooses to Stay" + " "*37 + "|")
    print("|" + " #The dealer starts hitting until he beats the player or busts" + " "*13 + "|")
    print("|" + " #Busting means going over sum of 21" + " "*39 + "|")
    print("|" + " #The objective of player is to get as close to sum 21 than dealer does" + " "*4 + "|")
    print("|" + "  without busting" + " "*58 + "|")
    print("|" + " #And vice versa for the dealer" + " "*44 + "|")
    print("|" + " #All numbered card have their value as the number itself" + " "*18 + "|")
    print("|" + " #jack, queen , king have a value as 10" + " "*36 + "|")
    print("|" + " #aces can have value of 1 or 11 whichever is suitable for dealer or player" + "|")
    print("|" + " #if player wins the game he gets 2 times the bet as the reward            " + "|")
    print("|" + " #if the player loses then he loses his bet                                " + "|")
    print("|" + " # GOOD LUCK                                                               " + "|")     
    print("|" + " "*75 + "|")
    print(" " + "-"*75)
    pass
player_cards = []
dealer_cards = []

def start_game() :
    
   
    #print rules of the game and also how to play the game
    rules()
    # using module keyboard
    import keyboard 
    print("a to continue")
    #listening for a keypress on key board
    while True :
        try :
            if keyboard.is_pressed("a") :
                player_cards.append(shuffle_deck[0])
                shuffle_deck.pop(0)
                player_cards.append(shuffle_deck[0])
                shuffle_deck.pop(0)
                dealer_cards.append(shuffle_deck[0]) 
                shuffle_deck.pop(0)
                dealer_cards.append(shuffle_deck[0])
                shuffle_deck.pop(0)
                break
        except:
            pass
    game_ended = False #This variable is created to tell the function the stage of game 
    #lets display the game to the player
    display_game(game_ended)
    # NOW it is the players turn 
    is_player = True #This variable is to tell the hit function who is hitting
    #asking the player to place his bet
    while True :
        try :
            players_bet = int(input("please enter your bet : \n"))
            print("your bet is %d" %(players_bet))
            break
        except : 
            print("please enter you bet in numbers")
            pass
        else :
            print("please enter you bet in numbers")
            pass
    #asking player to choose to hit or stay 
    while True  :
        players_choice = str(input("choose Hit or Stay : \n"))
        if players_choice.upper() == "HIT" :
            hit(is_player)
            clear()
            display_game(game_ended)
            if  player_sum() <= 21 :
                print("you are still in the game do you ")
            else :
                clear()
                game_ended = True
                display_game(game_ended) 
                print ("you lost the game as your sum value went over 21")
                print("you were busted")
                print ("you lost your bet \n better luck next time")
                break
        #as player choose to stay now we are letting computer dealer play
        elif players_choice.upper() == "STAY" :
            is_player = False
            if (dealer_sum() > player_sum() ) :
                clear()
                game_ended = True
                display_game(game_ended)
                print ("you lost the game as the dealer's sum value was greater than yours and less than 21")
                print("the dealer beat you")
                print ("you lost your bet \n better luck next time")
            else :
                while dealer_sum() <= player_sum() :
                    hit(is_player)
                    clear()
                    display_game(game_ended)
                    if (dealer_sum() > player_sum()) and (dealer_sum() <= 21) :
                        clear()
                        game_ended = True
                        display_game(game_ended)
                        print ("you lost the game as the dealer's sum value was greater than yours and less than 21")
                        print("the dealer beat you")
                        print ("you lost your bet \n better luck next time")
                        break
                    elif (dealer_sum() > 21) :
                        clear()
                        game_ended = True
                        display_game(game_ended)
                        print("you won the game")
                        print("you won %s "%(2*players_bet))                    
                        break
                    else : 
                        pass

            break
        #if player typed in neither hit nor stay
        else :
            clear()
            print("error")
            print("please either Type in Hit or Stay")
            pass
    pass  #end game

#starting the game
start_game()
