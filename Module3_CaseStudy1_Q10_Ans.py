# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence
# after sorting them alphabetically.

words = [x for x in raw_input('Enter comma separated words:').split(',')]
words.sort()
print ','.join(words)