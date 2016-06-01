# __author__ = "Propupul"
import random
import re
# hangman

print('Welcome to hangman')
print('The computer will pick a random word')
print('If you type a letter and it is correct, it will automatically fill the other blanks')

word_list = ['paper', 'constitution', 'america', 'bandwidth']
random_num = random.randint(0, 2)

for words in word_list:
    random_word = word_list[random_num]

answer = random_word

print('The word has bee chosen')
print("The word is", len(answer), "letters long")

answer_word = []
for letters in answer:

    answer_word.append('_')

hangman_figure = ['|','O',
                  '-|-',
                  '/|']
var_count = 0
print(answer_word)

while '_' in answer_word:
    player_answer = input("Please chose a letter: ")
    index = 0
    if len(player_answer) > 1:
        player_answer = player_answer[:1]
        print("please only use 1 letter")
        print(player_answer)

    if player_answer in answer:
        for m in re.finditer(player_answer, answer):
            answer_word.remove('_')
            answer_word.insert(m.start(), player_answer)
            print(answer_word)

            if '_' not in answer_word:
                print('Congratulations! You guessed the word:', answer)


    else:
        print("oops letter is not part of the word..")

        print(hangman_figure[var_count])
        var_count += 1
        if var_count == 4:
            for parts in hangman_figure:
                print(parts)
            print('The stick man has been hanged! You lose..')
            exit()


