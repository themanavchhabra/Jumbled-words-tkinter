from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
import random
import time
from playsound import playsound
from nltk.corpus import words   # imports a list of 236736 words 

word_list = []  #initializes list
word=""

def checkword(QuestionWord,UserWord):
	if UserWord == QuestionWord:
		return True 
	else:
		return False

def scramble(word):
	l = len(word)
	ScrambledList = random.sample(word,l)
	ScrambledWord = "".join(ScrambledList)
	return ScrambledWord

def creategame():
	global add_word

	load_title.destroy()
	one_player_button.destroy()
	two_player_button.destroy()

	creategame.add_word = Entry(root)
	creategame.add_word.pack(pady=20)
	creategame.add_word_button = Button(text="Add word to list", command=add_to_list, height=2, width=15)
	creategame.add_word_button.pack(pady=20)
	creategame.start_game_button = Button(text="Start game", command=intermediate, height=2, width=10)
	creategame.start_game_button.pack(pady=20)
	creategame.error_label = Label(text="")
	creategame.error_label.pack()
	creategame.show_list = Label(root,text=word_list, font=("Lucida Sans","12"))
	creategame.show_list.pack()

def add_to_list():
	new_word = creategame.add_word.get()
	if len(new_word) > 0:
		creategame.error_label.configure(text="")
		creategame.error_label.update()
		word_list.append(new_word)
		creategame.show_list.configure(text=word_list)
		creategame.show_list.update()
		creategame.add_word.delete(0,END)
	else:
		creategame.error_label.configure(text="Enter a word!")
		creategame.error_label.update()

def intermediate():
	creategame.add_word.destroy()
	creategame.add_word_button.destroy()
	creategame.start_game_button.destroy()
	creategame.show_list.destroy()
	startgame()

def oneplayer():
	global word_list

	load_title.destroy()
	one_player_button.destroy()
	two_player_button.destroy()

	word_list = words.words()
	startgame()

def startgame():
	global word,word_list

	word=random.choice(word_list)
	startgame.S = Label(root, text=scramble(word), font=("Algerian","20"))

	C.pack(anchor="e", pady=0)
	R.pack(anchor="w", side="top", pady=0)
	L.pack(anchor="n", pady=10)
	startgame.S.pack()
	E.pack(pady=10)
	M.pack()
	B.pack(pady=10)
	N.pack(pady=10)
	H.pack(pady=10)
	X.pack()
	G.pack(pady=20)

def check():
	global word, score, correct, incorrect, hint_taken
	if len(E.get())>0:
		entered_word = E.get()

		if entered_word == word:
			if hint_taken == True:
				score+=0.5
				hint_taken = False
			else:
				score+=1
			correct+=1
			M.configure(text="result --> Correct", bg="green")
			M.update()
			startgame.S.configure(text=word)
			startgame.S.update()
			C.configure(text="Score = "+str(score))
			C.update()

			time.sleep(3)

			E.delete(0,END)
			M.configure(text="result --> ", bg="white")
			M.update()

			G.configure(text="")
			G.update()

			word=random.choice(word_list)

			startgame.S.configure(text=scramble(word))
			startgame.S.update()

		else:
			score-=1
			incorrect+=1
			M.configure(text="result --> Wrong", bg="red")
			M.update()
			startgame.S.configure(text=word)
			startgame.S.update()
			C.configure(text="Score = "+str(score))
			C.update()

			time.sleep(3)

			E.delete(0,END)
			M.configure(text="result --> ", bg="white")
			M.update()

			G.configure(text="")
			G.update()

			word=random.choice(word_list)

			startgame.S.configure(text=scramble(word))
			startgame.S.update()
	else:
		M.configure(text="Enter a word!")
		M.update()

def skip():
	global word,skipctr
	skipctr+=1
	if skipctr > 3:
		messagebox.showinfo("Message","Maximum number of skips were used")
	else:
		word=random.choice(word_list)
		startgame.S.configure(text=scramble(word))
		startgame.S.update()		

def isVowel(letter):
	vowels = ["a","e","i","o","u"]
	if letter in vowels:
		return True
	else:
		return False

def hint():
	global word,hint_taken,number_of_hints
	hint=""
	number_of_hints+=1
	for i in word:
		if isVowel(i) == True:
			hint = hint+i+" "
		else:
			hint = hint+"_ "
	hint_taken = True
	G.configure(text=hint)
	G.update()

def rules():
	messagebox.showinfo("Rules","""1.  A jumbled word will be shown on the screen, your objective is to unscramble it
						\n2.  1 hint is available for each word
						\n3.  For every correct answer, 1 point is added
						\n4.  If hint is used,and correct answer is given, only 0.5 points are added 
						\n5.  For every wrong answer, 1 point is deducted""")

def end():
	global score, correct, incorrect,number_of_hints
	messagebox.showinfo("Quit", "Final results =\nCorrect answered: "+str(correct)+"\nIncorrect answered: "+str(incorrect)+"\nHints taken: "+str(number_of_hints)+"\nTotal score: "+str(score))
	root.destroy()

#list_of_words = ['india', 'apple', 'elephant', 'cushion', 'building', 'random', 'computer', 'drawer', 'cupboard']
hint_taken = False
number_of_hints = 0
score=0
correct=0
incorrect=0
skipctr=0

root = Tk(className = "Game")
root.geometry("400x600")
root.resizable(False, False)


C = Label(root, text="Score = "+str(score), font=("Arial","12"), bg="yellow", fg="black")

R = Button(root, text="How to play", command=rules, bg="blue", fg="white")

L = Label(root,text="Scrambled word game", font=("Arial","20"))

E = Entry(root, width=30)

M = Label(root, text="result --> ", font=("Calibri","15"))

B = Button(text="Check", command=check, height=1, width=10, font=("Arial","12"))

N = Button(text="Skip", command=skip, height=1, width=10, font=("Arial","12"))

H = Button(text="Hint",command=hint, height=1, width=5)

X = Button(text="End", command=end)

G = Label(text="", font=("Comic Sans MS","20"))


load_title = Label(root, text="JUMBLED WORD GAME", font=("Cooper Black", "20"))
load_title.pack(pady=20)
one_player_button = Button(root, text="One player", command=oneplayer)
two_player_button = Button(root, text="Create game", command=creategame)
one_player_button.pack(pady=20, padx=10)
two_player_button.pack(pady=20, padx=10)
root.mainloop()