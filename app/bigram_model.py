from collections import defaultdict

def BigramModel(sentences: list):
    bigram_counts, unigram_counts = defaultdict(int), defaultdict(int)
    bigram_probabilities = {}

    for sentence in sentences:
        for i in range(len(sentence) - 1):
            bigram = (sentence[i], sentence[i + 1])
            bigram_counts[bigram] += 1
            unigram_counts[sentence[i]] += 1
        unigram_counts[sentence[-1]] += 1  # Count the last word in the sentence

    for bigram, count in bigram_counts.items():
        bigram_probabilities[bigram] = count / unigram_counts[bigram[0]]

    return bigram_probabilities