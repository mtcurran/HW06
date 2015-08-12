#!/usr/bin/env python
# HW06_ex09_02.py

# (1)
# Write a function called has_no_e that returns True if the given word doesn't
# have the letter "e" in it.
#   - write has_no_e
# (2)
# Modify your program from 9.1 to print only the words that have no "e" and
# compute the percentage of the words in the list have no "e."
#   - print each approved word on new line, followed at the end by the %
##############################################################################
# Imports

# Body
#Part (1)
def has_no_e(s):
	for letter in s:
		if "e" in letter:
			return False
	return True

def percent_no_e():
	fin = open("words.txt")

	total_count = 0
	for line in fin:
		total_count += 1

	fin.close()

	with open("words.txt") as f:
		all_words = f.readlines()

	num_e_words = 0
	list_e_words = []

	for line in all_words:
		if "e" in line:
			num_e_words += 1
			print line

	percent_e_words = round(100*(num_e_words / float(total_count)), 3)

	print percent_e_words


##############################################################################
def main():
  # Call your function(s) here.

    print has_no_e("Elephant")
    print has_no_e("Aardvark")

    percent_no_e()


if __name__ == '__main__':
    main()
