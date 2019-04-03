# Regex library
import re

import collections

text = open('book.txt').read().lower()
"""
The w denotes anything that is not whitespace
+ denotes one or more
So, every occurence of one or more characters
that is not whitespace, it counts it as a word
"""
words = re.findall('\w+', text)
print(collections.Counter(words).most_common(10))
