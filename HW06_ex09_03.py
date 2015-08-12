#!/usr/bin/env python
# HW06_ex09_03.py

# (1)
# Write a function named avoids that takes a word and a string of forbidden
# letters, and that returns True if the word doesn't use any of the forbidden
# letters.
#   - write avoids
# (2)
# Modify your program to prompt the user to enter a string of forbidden
# letters and then print the number of words that don't contain any of them.
#   - write function(s)
# (3)
# Can you find a combination of 5 forbidden letters that excludes the smallest
# number of words?
#   - write a function that finds this combination of letters
#   - have that function print the letters and print the # of words excluded
##############################################################################
# Imports

# Body

#Part (1)
def avoids(word, forb_letters):
	for letter in word:
		if letter in forb_letters:
			return False
	return True

#Part (2)
def percent_avoids():
	fin = open("words.txt")

	total_count = 0
	for line in fin:
		total_count += 1

	fin.close()

	forb_string = raw_input("Enter a string of forbidden letters: ")

	with open("words.txt") as f:
		all_words = f.readlines()

	num_clean = 0

	for line in all_words:
		if avoids(line, forb_string):
			num_clean += 1
			print line

	percent_clean_word = round(100*(num_clean / float(total_count)), 3)

	print num_clean
	print percent_clean_word

#Part (3)
"""I'm not sure how to write a function to help me find this other than testing every possible
combination of 5 letters and finding the minimum percent, however I'd guess that using all 5
common vowels "aeiou" as the forbidden letters would do the trick. Passing these letters to my
function in part 2 results in only 107 words (0.094%) being excluded"""

##############################################################################
def main():

    print avoids("cheerios", "se")
    print avoids("chex", "a")

    percent_avoids()

if __name__ == '__main__':
    main()
