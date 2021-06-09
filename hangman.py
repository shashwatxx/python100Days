import random
import hangman_words
import hangman_art


end_of_game = False
chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)
display = []
for _ in chosen_word:
    display.append("_")
lives = 6
print(hangman_art.logo)
while not end_of_game:
    guessed_letter = input("Guess a letter\n").lower()
    for i in range(len(chosen_word)):
        letter = chosen_word[i]
        if letter == guessed_letter:
            display[i] = letter
    print(display)
    if guessed_letter not in chosen_word:
        lives = lives-1
        if(lives <= 0):
            print("You Lost!")
            print(f"the Correct Answer is {chosen_word}")
            end_of_game = True
        else:
            print(hangman_art.stages[lives])

    if('_' not in display):
        end_of_game = True
        print("You Won!")
