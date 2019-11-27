# Insert your code here
import sys

letters = input('Enter between 3 and 10 lowercase letters: ')
letters = letters.replace(' ', '')
if len(letters) not in range(3, 11) or not (letters.isalpha() and letters.islower()):
    print('Incorrect input, giving up...')
    sys.exit()

values = {'a':2,'b':5,'c':4,'d':4,'e':1,'f':6,
          'g':5,'h':5,'i':1,'j':7,'k':6,'l':3,
          'm':5,'n':2,'o':3,'p':5,'q':7,'r':2,
          's':1,'t':2,'u':4,'v':6,'w':6,'x':7,
          'y':5,'z':7}          
all_words = []
with open('wordsEn.txt') as file:
    for line in file:
        line = line.strip('\n')
        all_words.append(line)

words = []
for char in all_words:
    for e in char:
        if letters.count(e) < char.count(e):
            break
    else:
        words.append(char)
        
if not words:
    print('No word is built from some of those letters.')
else:
    highest_score = 0
    new_list = []
    for word in words:
        score = 0
        for e in word:
            score += values[e]
        if score > highest_score:
            highest_score = score
            new_list = []
            new_list.append(word)
        elif score == highest_score:
            new_list.append(word)
        else:
            pass
    print(f'The highest score is {highest_score}.')
    if len(new_list) == 1:
        print(f'The highest scoring word is {new_list[0]}')
    else:
        print('The highest scoring words are, in alphabetical order:')
        for e in new_list:
            print('    ' + e)
