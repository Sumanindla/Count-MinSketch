import mmh3  # A non-cryptographic hash function library
import numpy as np

class CountMinSketch:
    def __init__(self, num_hash_functions, num_counters):
        self.num_hash_functions = num_hash_functions
        self.num_counters = num_counters
        self.counters = np.zeros((num_hash_functions, num_counters), dtype=int)

    def hash_indices(self, item):
        return [mmh3.hash(item, i) % self.num_counters for i in range(self.num_hash_functions)]

    def increment(self, item):
        indices = self.hash_indices(item)
        for i, index in enumerate(indices):
            self.counters[i][index] += 1

    def estimate_frequency(self, item):
        indices = self.hash_indices(item)
        min_count = min(self.counters[i][index] for i, index in enumerate(indices))
        return min_count

# Create a CountMinSketch with 3 hash functions and 100 counters
cms = CountMinSketch(num_hash_functions=3, num_counters=100)

# Simulate a stream of words and update the sketch
word_stream = ["apple", "banana", "apple", "cherry", "banana", "apple", "apple"]
for word in word_stream:
    cms.increment(word)

# Estimate the frequencies of different words
print("Estimated frequencies:")
print("apple:", cms.estimate_frequency("apple"))
print("banana:", cms.estimate_frequency("banana"))
print("cherry:", cms.estimate_frequency("cherry"))
print("grape:", cms.estimate_frequency("grape"))
