# Write a program that accepts a sequence of whitespace separated words as inputtext
# and   prints   the   words   after   removing   all   duplicate   words   and   sorting   them alphanumerically.
s = raw_input('Enter a sentence:')
words = [word for word in s.split(" ")]
print " ".join(sorted(list(set(words))))