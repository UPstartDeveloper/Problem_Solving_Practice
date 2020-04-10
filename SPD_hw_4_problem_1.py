"""
Problem:
Given a string of text and a number k, find the k words in the given text that appear most frequently. Return the words in a new array sorted in decreasing order.

Problem Solving:
“My name is Zain I love coding and I love playing b-ball.”
“One fish two fish red fish blue fish”

1 - form a histogram of the distribution of the word
{
‘One’: 1,
‘Fish’: 4,
‘Two’: 1

}

2 - convert a list of lists
.items():
[ (‘fish’, 4), (‘fishstick’, 5)]

[ (‘fishstick’, 5), (‘fish’, 4)]

[‘fishstick’, ‘fish’]
"""


def get_duplicate_words(text):
	histogram = {}
	words = text.split()
	# make a distribution of word types and count of tokens
	for word in words:
		if word not in histogram:
			histogram[word] = 1
		else:  # word type already seen before in histogram
			Histogram[word] += 1
	#
