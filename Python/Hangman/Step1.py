#Step 1 

word_list = ["ardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
import random
chosen_word = random.choice(word_list)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
'''i = 0 #To get hold of index of the chosen_word
while (i<=len(chosen_word)):
  if (guess == chosen_word[i]):
    print("Right")
  else :
    print("Wrong")
  i+=1'''
for letter in chosen_word:
  if guess == letter:
    print("Right")
  else:
    print("Wrong")
