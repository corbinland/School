import string

# Input and Output file names
input_file = "alice_in_wonderland.txt"
output_file = "alice_words.txt"

# Dictionary to hold word counts
word_counts = {}

# Read and process the file
with open(input_file, 'r', encoding='utf-8') as file:
    for line in file:
        # Remove punctuation and convert to lowercase
        line = line.translate(str.maketrans('', '', string.punctuation))
        words = line.lower().split()

        for word in words:
            word_counts[word] = word_counts.get(word, 0) + 1

# Sort words alphabetically
sorted_words = sorted(word_counts.items())

# Write output file with formatting
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(f"{'Word':<18}Count\n")
    file.write("=" * 25 + "\n")

    for word, count in sorted_words:
        file.write(f"{word:<18}{count}\n")

# Print how many times 'alice' appears
alice_count = word_counts.get('alice', 0)
print(f"The word 'alice' occurs {alice_count} times in the book.")
