# a console game
# date: aug 7,8,9 2021
from random import choice

word_i = str()
counter = int()
pattern = [' |-------', ' |   |', ' |    ', r' |      ', ' |    ', r' |      ', ' |']


def fun_pattern(word:str, *args):
	global word_i
	global counter
	
	
	if len(args) == 2:
		guess, index_nums = args
		word_i = edit_word_i(word_i, guess, index_nums)
	elif len(args) == 1:
		counter += 1
		#TODO increase counter and then change the pattern if counter max return you lose:
		
	else:
		word_i = "__ "*len(word)
		
	global pattern
	if len(pattern) == 8:
		pattern.pop(-1)
	pattern.append(f'---\t\t word: {word_i}')
	
	if counter == 1: 
		pattern[2] = ' |   O'
	elif counter == 2: 
		pattern[3] = ' |   |'
	elif counter == 3: 
		pattern[3] = ' |  /|'
	elif counter == 4:
		pattern[3] = ' |  /|\ '
	elif counter == 5:
		pattern[4] = ' |   |'
	elif counter == 6:
		pattern[5] = ' |  /'
	elif counter == 7:
		pattern[5] = ' |  / \ '

	
	for i in pattern:
		print(i)

def edit_word_i(word_i:str, guess:str, index_nums:list) -> str:
	word_a = word_i.split()

	for j in index_nums:
		word_a[j] = guess

	word_a = ' '.join(word_a)

	return word_a

def get_a_word() -> str:
	word_list = ['python', 'tkinter', 'pygame', 'asus', 'msi', 'lale']
	return choice(word_list)


def get_guess() -> str:	
	while 1:
		word_or_letter = input('Guess a letter (1)\nGuess the word (2) : ')
		
		if word_or_letter == '1':
			while 1:
				guess = input('Type a letter :')
				if len(guess) != 1:
					print('Please just type one letter!') 
					continue
				else: break
			break
		elif word_or_letter == '2':
			guess = input('Type the word :')
			break
		elif word_or_letter in 'qQ':
			exit()
		else:
			print('Do Not Type Other Things!(for quit (q))')
			continue
	return guess


def get_index_nums(letter, word:str ) -> list:
	'''
	:aim     : finds index numbers of given letter in the word:
	:param   : letter: required
	:param   : word  : required
	:returns : a list ?:
	'''
	index_nums = list()

	while 1:
		try:
			index = word.find(letter, index_nums[-1] + 1)
			if index == -1:
				break
			index_nums.append(index)
			#TODO HOW TO QUIT THIS LOOP?(handled)
		except IndexError:
			index_nums.append(word.find(letter, 0))
	
	return index_nums


#game play
def main() -> None:
	word = get_a_word().upper()
	fun_pattern(word)
	global word_i

	while 1:
		
		guess = get_guess().upper().strip()
		if guess == word:
			print('YOU WON!')
			break
		
		elif guess in word and len(guess) == 1:
			index_nums = get_index_nums(guess, word)
			fun_pattern(word, guess, index_nums)
			#TODO conditions check 
			if word_i.replace(' ', '').isalpha():
				print('YOU WON!')
				break
		else:
			fun_pattern(word, False)
			if counter == 7:
				print('GAME OVER!')
				break


if __name__ == '__main__':
	print('Welcome to hangman game!')
	print('Guess the word!')
	main()