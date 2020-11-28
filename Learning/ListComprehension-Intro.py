#ListComprehension-Intro.py
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = []
for word in words:
    if word != "the":
        word_lengths.append(len(word))
print(words)
print(word_lengths)

# using list comprehension to simplify
words2 = sentence.split()
word_lengths2 = [len(word) for word in words if word != "the"]
print()
print(words2)
print(word_lengths2)