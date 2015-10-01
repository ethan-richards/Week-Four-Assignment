_author_ = "Ethan Richards"
# CIS 125
#pigify
# pigify.py
#Converts words to pig latin.

# Define vowels

vowels = "aeiouAEIOU"

# Ask for word

word = input("Please enter a word: ")

# Loop through word, one letter at a time

for letter in word:
	# Check if letter is a vowel
	if letter in vowels:
		# True?  We are done
		pig = word + "yay"
	else:
		# False? Consonant
		pig = word[1:] + word[0] + "ay"
		
print(pig)