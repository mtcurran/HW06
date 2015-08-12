#!/usr/bin/env python
# HW06_ex09_04.py

# (1)
# Write a function named uses_only that takes a word and a string of letters,
# and that returns True if the word contains only letters in the list.
#   - write uses_only
# (2)
# Can you make a sentence using only the letters acefhlo? Other than "Hoe
# alfalfa?"
#   - write function to assist you
#   - type favorite sentence(s) here:
#       1: Hello fool
#       2: Flee alcohol cafe oaf
#       3: All aloe feel local
##############################################################################
# Imports

# Body

#Part (1)
def uses_only(word, letters):
	i = 0
	while i < len(word):
		if word[i] in letters:
			i += 1
		else:
			return False
	return True


#Part (2) This function will print words from "words.txt" that only use letters in "acefhlo"
#Words can then be chosen from this list that form sentences
def generate_words():

	with open("words.txt") as f:
		all_words = f.readlines()

	for line in all_words:
		if uses_only(str(line.strip()), "acefhlo"):
			print line.strip()

##############################################################################
def main():
    
    print uses_only("cinnamon", "cinamo")
    print uses_only("equestrian", "esn")
    print uses_only("xylaphone", "q")

    generate_words()

if __name__ == '__main__':
    main()
