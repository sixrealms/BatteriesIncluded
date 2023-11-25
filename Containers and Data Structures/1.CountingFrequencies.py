'''Suppose we want to track the frequency of words in text
we can use collections.Counter'''
from collections import Counter

txt = "Nory was a Catholic because her mother was a Catholic and Nory’s mother was a Catholic because her father was"

counts = Counter(txt.split())
print(counts)

most_common_2 = counts.most_common(2)
print(most_common_2)

word_frequency = counts['Catholic']
print(word_frequency)

total_words = sum(counts.values())
print(total_words)
