#Step 3

import random
word_list = ["aardvark", "baboon", "camel"]
random_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {random_word}.')

#TODO-1: - Create an empty List called display.
display = []

#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

for words in random_word:
  display.append("_")
print(display)
  
#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
  
end_game = False

while not end_game:
    guess = input('Please guess a letter\n').lower()

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
    for position in range(len(random_word)):
      words = random_word[position]
      if guess in words:
        display[position] = guess


#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
    print(display)
  
#Check guessed letter
    if "_" not in display:
      end_game = True
      print("You win!")