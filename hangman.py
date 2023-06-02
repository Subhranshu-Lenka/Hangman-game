# https://www.youtube.com/watch?v=LBczOO5hOKc
import random
import word_list

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
list_of_words = word_list.word_lists
word = random.choice(list_of_words)
print(logo)
lives = len(stages)

# print(word)
empty = ["_"]*len(word)

while(True):
    if "_" not in empty:
        print("You won !!")
        break

    print(empty)

    guess = input("\nGuess the letters of the word.\t").lower()
    # if guess is in word:
    if guess not in word:
        lives -= 1
        print(stages[lives])
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            print("You lose!!")
            print(f"The word was {word}")
            break
    elif guess in empty:
        print(f"You already guessed {guess}")
    else:
        for i in range(0, len(word)):
            if word[i] == guess:
                empty[i] = guess
