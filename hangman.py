# a console game
# date: aug 7 2021
from random import choice


word_list = ['dance', 'python', 'pygame', 'tkinter', 'basketball']

def get_a_word() -> str:
	...
	return choice(word_list)

def main() -> None:
	word = get_a_word()
	return word



if __name__ == '__main__':
	print('Welcome to hangman game!')
	print('Guess the word!')
	print(main())