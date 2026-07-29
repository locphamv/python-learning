sentence = "python is useful and python is popular for ai"

words = sentence.split()
word_counts = {}

for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

for word,count in word_counts.items():
    print(f"{word}: {count}")
