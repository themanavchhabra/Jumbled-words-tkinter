import random

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

wordlist = ['india', 'apple', 'elephant', 'cushion', 'building']

for word in wordlist:
	print ("heres is the scrambled word\n\n" + scramble(word)+"\n\n")
	while (True):
		answer = input("Your answer \n")
		if checkword(word,answer) == True:
			print("\ncorrect answer")
			break;
		else:
			print("\n incorrect answer \n")