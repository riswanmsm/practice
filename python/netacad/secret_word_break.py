# Loop continuously and ask the user to enter a word.
SECRET_WORD = 'chupacabra'
while True:
    word = input('Enter a word, if you enter the secret word you will be released: ')
    if word == 'chupacabra':
        break
print('\nYou\'ve successfully left the loop.\n')