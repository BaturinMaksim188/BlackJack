from random import randrange
from tkinter import *
from tkinter import messagebox
from PIL import *
from PIL import Image, ImageTk
import time


window = Tk()
window.state('zoomed')
window.title("Blackjack")
icon = PhotoImage(file = "blackjack.png")
window.iconphoto(False, icon)


#identify variable
global chip
chip = 10000
global bet
bet = 0
global dealer
dealer = []
global player
player = []
global playerscore
playerscore = 0
global dealerscore
dealerscore = 0
global doubleopport
doubleopport = False
global takecount
takecount = 0
global wins, loses
wins, loses = 0, 0


#identify cards
deck = {"2 of Diamonds":2, "3 of Diamonds":3, "4 of Diamonds":4, "5 of Diamonds":5, "6 of Diamonds":6, "7 of Diamonds":7, "8 of Diamonds":8, "9 of Diamonds":9, "10 of Diamonds":10,
        "Jack of Diamonds":10, "Queen of Diamonds":10, "King of Diamonds":10, "Ace of Diamonds":11,
        "2 of Hearts":2, "3 of Hearts":3, "4 of Hearts":4, "5 of Hearts":5, "6 of Hearts":6, "7 of Hearts":7, "8 of Hearts":8, "9 of Hearts":9, "10 of Hearts":10,
        "Jack of Hearts":10, "Queen of Hearts":10, "King of Hearts":10, "Ace of Hearts":11,
        "2 of Clubs":2, "3 of Clubs":3, "4 of Clubs":4, "5 of Clubs":5, "6 of Clubs":6, "7 of Clubs":7, "8 of Clubs":8, "9 of Clubs":9, "10 of Clubs":10,
        "Jack of Clubs":10, "Queen of Clubs":10, "King of Clubs":10, "Ace of Clubs":11,
        "2 of Spades":2, "3 of Spades":3, "4 of Spades":4, "5 of Spades":5, "6 of Spades":6, "7 of Spades":7, "8 of Spades":8, "9 of Spades":9, "10 of Spades":10,
        "Jack of Spades":10, "Queen of Spades":10, "King of Spades":10, "Ace of Spades":11}
names = list(deck.keys())
picked = []

def pick_a_card():
    pick = False
    while pick == False:
        card = names[randrange(len(names))]
        if card not in picked:
            picked.append(card)
            pick = True
        else:
            continue
    return card


#functions
def win():
    end = messagebox.askyesno(
        title="Победа! Поздравляем!",
        message="Ещё разок?")
    if end:
        return True
    else:
        return False

def lose():
    end = messagebox.askyesno(
        title="О нет, вы всё проиграли(",
        message="Ещё разок? (Если у вас ещё что-то осталось...)")
    if end:
        return True
    else:
        return False


        
def play():
    global player, dealer
    player, dealer = [], []
    picked = []
    playercardlabel.config(text="")
    dealercardlabel.config(text="")
    dealerscorelabel.config(text="У диллера нет карт.")
    betbutton.config(state='disabled')
    takebutton.config(state='active')
    doublebutton.config(state='disabled')
    stopbutton.config(state='active')

def end_hand():
    global playerscore, dealerscore, chip, bet, doubleopport, takecount, wins, loses
    doubleopport = False
    takecount = 0
    betbutton.config(state='active')
    takebutton.config(state='disabled')
    doublebutton.config(state='disabled')
    stopbutton.config(state='disabled')
    playerscorelabel.config(text="У вас нет карт.")

    if playerscore >= 21:
        if playerscore == 21:
            if dealerscore == 21:
                chip += bet
                bet = 0
                playercardlabel.config(text="Ничья! {}".format(playerscore))
                havechip.config(text = "У вас осталось {} фишек!".format(chip))
                betchip.config(text="Вы поставили {} фишек!".format(bet))
                playerscore = 0
                dealerscore = 0
                return
            chip += bet * 3
            bet = 0
            playercardlabel.config(text="BlackJack! {}".format(playerscore))
            havechip.config(text = "У вас осталось {} фишек!".format(chip))
            betchip.config(text="Вы поставили {} фишек!".format(bet))
            playerscore = 0
            dealerscore = 0
            if chip >= 100000:
                again = win()
                if again:
                    chip = 10000
                    wins += 1
                    winlabel.config(text="Победы: {}".format(wins))
                    havechip.config(text = "У вас осталось {} фишек!".format(chip))
                    dealercardlabel.config(text="")
                    dealerscorelabel.config(text="У диллера нет карт.")
                    playercardlabel.config(text="")
                    playerscorelabel.config(text="У вас нет карт.")
                else:
                    window.destroy()
            return
        if playerscore > 21:
            bet = 0
            playercardlabel.config(text="Вы проиграли! {}".format(playerscore))
            havechip.config(text = "У вас осталось {} фишек!".format(chip))
            betchip.config(text="Вы поставили {} фишек!".format(bet))
            playerscore = 0
            dealerscore = 0
            if chip <= 0:
                again = lose()
                if again:
                    chip = 10000
                    loses += 1
                    loselabel.config(text="Поражения: {}".format(loses))
                    havechip.config(text = "У вас осталось {} фишек!".format(chip))
                    dealercardlabel.config(text="")
                    dealerscorelabel.config(text="У диллера нет карт.")
                    playercardlabel.config(text="")
                    playerscorelabel.config(text="У вас нет карт.")
                else:
                    window.destroy()
            return
    if dealerscore >= 21:
        if dealerscore == 21:
            bet = 0
            playercardlabel.config(text="Вы проиграли! {}".format(playerscore))
            havechip.config(text = "У вас осталось {} фишек!".format(chip))
            betchip.config(text="Вы поставили {} фишек!".format(bet))
            playerscore = 0
            dealerscore = 0
            if chip <= 0:
                again = lose()
                if again:
                    chip = 10000
                    loses += 1
                    loselabel.config(text="Поражения: {}".format(loses))
                    havechip.config(text = "У вас осталось {} фишек!".format(chip))
                    dealercardlabel.config(text="")
                    dealerscorelabel.config(text="У диллера нет карт.")
                    playercardlabel.config(text="")
                    playerscorelabel.config(text="У вас нет карт.")
                else:
                    window.destroy()
            return
        if dealerscore > 21:
            chip += bet * 2
            bet = 0
            playercardlabel.config(text="Вы выиграли! {}".format(playerscore))
            havechip.config(text = "У вас осталось {} фишек!".format(chip))
            betchip.config(text="Вы поставили {} фишек!".format(bet))
            playerscore = 0
            dealerscore = 0
            if chip >= 100000:
                again = win()
                if again:
                    chip = 10000
                    wins += 1
                    winlabel.config(text="Победы: {}".format(wins))
                    havechip.config(text = "У вас осталось {} фишек!".format(chip))
                    dealercardlabel.config(text="")
                    dealerscorelabel.config(text="У диллера нет карт.")
                    playercardlabel.config(text="")
                    playerscorelabel.config(text="У вас нет карт.")
                else:
                    window.destroy()
            return
    if playerscore > dealerscore:
        chip += bet * 2
        bet = 0
        playercardlabel.config(text="Вы выиграли! {}".format(playerscore))
        havechip.config(text = "У вас осталось {} фишек!".format(chip))
        betchip.config(text="Вы поставили {} фишек!".format(bet))
        playerscore = 0
        dealerscore = 0
        if chip >= 100000:
            again = win()
            if again:
                chip = 10000
                wins += 1
                winlabel.config(text="Победы: {}".format(wins))
                havechip.config(text = "У вас осталось {} фишек!".format(chip))
                dealercardlabel.config(text="")
                dealerscorelabel.config(text="У диллера нет карт.")
                playercardlabel.config(text="")
                playerscorelabel.config(text="У вас нет карт.")
            else:
                window.destroy()
        return
    elif playerscore < dealerscore:
        bet = 0
        playercardlabel.config(text="Вы проиграли! {}".format(playerscore))
        havechip.config(text = "У вас осталось {} фишек!".format(chip))
        betchip.config(text="Вы поставили {} фишек!".format(bet))
        playerscore = 0
        dealerscore = 0
        if chip <= 0:
            again = lose()
            if again:
                chip = 10000
                loses += 1
                loselabel.config(text="Поражения: {}".format(loses))
                havechip.config(text = "У вас осталось {} фишек!".format(chip))
                dealercardlabel.config(text="")
                dealerscorelabel.config(text="У диллера нет карт.")
                playercardlabel.config(text="")
                playerscorelabel.config(text="У вас нет карт.")
            else:
                window.destroy()
        return
    elif playerscore == dealerscore:
        chip += bet
        bet = 0
        playercardlabel.config(text="Ничья! {}".format(playerscore))
        havechip.config(text = "У вас осталось {} фишек!".format(chip))
        betchip.config(text="Вы поставили {} фишек!".format(bet))
        playerscore = 0
        dealerscore = 0
        return

            
def take_card():
    global player, playerscore, doubleopport, takecount
    winorloselabel.config(text="")
    takecount += 1
    doubleopport = True
    if takecount >= 2:
        doubleopport = False
    if doubleopport:
        doublebutton.config(state='active')
    if not doubleopport:
        doublebutton.config(state='disabled')
    card = pick_a_card()
    player.append(card)
    for i in player: 
        playercardlabel.config(text="{}".format(i))
    if playerscore + deck[card] >= 21:
        if playerscore + deck[card] == 21:
            playerscore += deck[card]
            playerscorelabel.config(text="{}".format(playerscore))
            stop()
        if playerscore + deck[card] > 21:
            playerscore += deck[card]
            playerscorelabel.config(text="{}".format(playerscore))
            stop()
    else:
        playerscore += deck[card]
        playerscorelabel.config(text="{}".format(playerscore))

def double_bet():
    global playerscore, dealerscore, chip, bet, doubleopport, isdouble
    if bet * 2 <= chip:
        doubleopport = False
        card = pick_a_card()
        player.append(card)
        playerscore += deck[card]
        chip -= bet
        bet += bet
        havechip.config(text = "У вас осталось {} фишек!".format(chip))
        betchip.config(text="Вы поставили {} фишек!".format(bet))
        stop()
    else:
        winorloselabel.config(text="Вы не можете поставить больше, чем у вас есть!")


def stop():
    global dealer, dealerscore

    taken = "||"
    card = pick_a_card()
    dealer.append(card)
    dealerscore += deck[card]
    for i in dealer:
        taken += i
        taken += "||"
    dealercardlabel.config(text="{}".format(taken))
    dealerscorelabel.config(text="{}".format(dealerscore))

    
    card = pick_a_card()
    dealer.append(card)
    dealerscore += deck[card]
    taken = "||"
    for i in dealer:
        taken += i
        taken += "||"
    dealercardlabel.config(text="{}".format(taken))
    dealerscorelabel.config(text="{}".format(dealerscore))

    
    while dealerscore < 16:
        card = pick_a_card()
        dealer.append(card)
        dealerscore += deck[card]
        taken = "||"
        for i in dealer:
            taken += i
            taken += "||"
        dealercardlabel.config(text="{}".format(taken))
        dealerscorelabel.config(text="{}".format(dealerscore))
    end_hand()

def do_bet():
    global chip, bet
    try:
        field = int(text.get(1.0, END))
    except:
        winorloselabel.config(text="Введите число!")        
        return

    if int(text.get(1.0, END)) > 0:
        winorloselabel.config(text="")   
        if int(text.get(1.0, END)) <= chip:
            chip -= int(text.get(1.0, END))
            bet = int(text.get(1.0, END))
            text.delete(1.0, END)
            havechip.config(text = "У вас осталось {} фишек!".format(chip))
            betchip.config(text="Вы поставили {} фишек!".format(bet))
            play()
        else:
            winorloselabel.config(text="Вы не можете поставить больше, чем у вас есть!")
    else:
        winorloselabel.config(text="Вы не можете поставить меньше чем 1 фишку!")


#interface block
havechip = Label(width=30, heigh=4, text="У вас осталось {} фишек!".format(chip))
havechip.pack(anchor=NW)
betchip = Label(width=30, heigh=4, text="Вы поставили {} фишек!".format(bet))
betchip.pack(anchor=NW)


dealerframe = Frame()
dealerframe.pack(anchor=N)
dealerview = Label(dealerframe, width=30, text="ДИЛЛЕР:")
dealerview.pack(anchor=N)
blanklabel = Label(dealerframe, width=30, height = 1, text="")
blanklabel.pack()


scoreframe = Frame()
scoreframe.pack(anchor=N)
dealercardlabel = Label(scoreframe, width=800, text="")
dealercardlabel.pack(anchor=N)
dealerscorelabel = Label(scoreframe, width=30, text="У диллера нет карт.")
dealerscorelabel.pack(anchor=N)

winorloselabel = Label(scoreframe, width=800, height = 24, text="")
winorloselabel.pack()

playercardlabel = Label(scoreframe, width=30, text="")
playercardlabel.pack(anchor=S)
playerscorelabel = Label(scoreframe, width=30, text="У вас нет карт.")
playerscorelabel.pack(anchor=S)


frame = Frame()
frame.pack(anchor=SW)
text = Text(frame, width=40, height=10)
text.pack(side=LEFT)
betbutton = Button(frame, text="Ставка", command=do_bet, height=5, width=30, state='active')
betbutton.pack(side=LEFT)
takebutton = Button(frame, text="Взять", command=take_card, height=5, width=30, state='disabled')
takebutton.pack(side=LEFT)
doublebutton = Button(frame, text="Удвоить", command=double_bet, height=5, width=30, state='disabled')
doublebutton.pack(side=LEFT)
stopbutton = Button(frame, text="Стоп", command=stop, height=5, width=30, state='disabled')
stopbutton.pack(side=LEFT)

winorlosescore = Frame(frame)
winorlosescore.pack(anchor=SW)
winlabel = Label(frame, width=30, text="Победы: {}".format(wins))
winlabel.pack()
loselabel = Label(frame, width=30, text="Поражения: {}".format(loses))
loselabel.pack()


