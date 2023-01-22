# Prompt the user to enter a word
# and assign it to the user_word variable.
user_word = input('Enter a word in which you want to remove vowels: ')
count = 0
for letter in user_word:
    # Complete the body of the for loop.
    if letter.upper() in 'AEIOU':
        count += 1
        continue
    print(letter)
print('Thank You, your word contained', count, 'vowels')