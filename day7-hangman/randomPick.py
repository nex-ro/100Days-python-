import random
import hangman_art 

word=['Banana', 'galaxy', 'bicycle', 'dragon', 'pineapple', 'universe', 'waterfall', 'laptop', 'moon', 'forest', 'guitar', 'book', 'coffee', 'mountain', 'dolphin', 'star', 'rainbow', 'cat', 'beach']
Picked=random.choice(word)
guessWord=list(Picked)
for a in range(len(guessWord)):
    guessWord[a]="_"
hp=5
print(hangman_art.logo)
print("Welcome to HangMan ")
print(f"Your Word :{guessWord}")
while(True):
    status=False
    guess=input("take a guess :")[:1].lower()
    if(guess in guessWord):
            print(f"you have guess{guess} and it already in the word")
            continue
    for i in range(len(Picked)):
        if(Picked[i]==guess):
            status=True
            guessWord[i]=guess
    if(status==False):
        hp-=1
        print('Your Guess is not in the word.')
    else:
        print('your guess is in the word you are correct ')
    print(hp)
    print(hangman_art.HangmanArt[(hp)])
    print(guessWord)
    if("_" not in guessWord):
        print( " You complete the word You WON")
        break
    if(hp<=0):
        print("You running out hp heart you lose")
        print("game Over")
        break






