#Here create an initial variable which will be added to the end of every input
pyg = 'ay'

# Here create a variable and define it as the raw input
original = raw_input('Enter a word:')

# Here create another variable that enables the translator to return any valid input as lowercase
word = (original).lower()

# Here create a third variable to single out the first character of any valid input
first = word[0]

#Here create a fourth variable to single out the remaining characters of any valid input( the second character to whatever length the input possesses)
second = word[1:len(word)]

#Here create a fifth variable that will be equal to the sums of the fourth, third and initial variables
new_word = second + first + pyg

#In english: If the length of any valid input is greater than zero and it's a string of letters, print out the fifth variable. Or else, print nothing....
if len(original) > 0 and original.isalpha():
    print new_word
else:
    print 'empty'
	
