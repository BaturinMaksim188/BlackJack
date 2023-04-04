from random import randrange
from tkinter import *
from PIL import *
from PIL import Image, ImageTk


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
global p
p = False


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
def play():
    print("игра началась")
    betbutton.config(state='disabled')
    takebutton.config(state='active')
    doublebutton.config(state='active')
    stopbutton.config(state='active')

def take_card():
    global player
    player.append(pick_a_card())
    print(player)

def double_bet():
    pass

def do_bet():
    global chip, bet
    if int(text.get(1.0, END)) <= chip:
        chip -= int(text.get(1.0, END))
        bet = int(text.get(1.0, END))
        text.delete(1.0, END)
        havechip.config(text = "У вас осталось {} фишек!".format(chip))
        betchip.config(text="Вы поставили {} фишек!".format(bet))
        play()

#interface block
havechip = Label(width=30, heigh=4, text="У вас осталось {} фишек!".format(chip))
havechip.pack(anchor=NW)

betchip = Label(width=30, heigh=4, text="Вы поставили {} фишек!".format(bet))
betchip.pack(anchor=NW)


frame = Frame()
frame.pack(anchor=SW)
text = Text(frame, width=40, height=10)
text.pack(side=LEFT)
betbutton = Button(frame, text="Ставка", command=do_bet, height=5, width=30, state='active')
betbutton.pack(side=LEFT)
takebutton = Button(frame, text="Взять", command=take_card, height=5, width=30, state='disabled')
takebutton.pack(side=LEFT)
doublebutton = Button(frame, text="Удвоить", command=pick_a_card, height=5, width=30, state='disabled')
doublebutton.pack(side=LEFT)
stopbutton = Button(frame, text="Стоп", command=pick_a_card, height=5, width=30, state='disabled')
stopbutton.pack(side=LEFT)




window.mainloop()
