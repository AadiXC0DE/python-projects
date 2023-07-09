def count_word_occurrences(text, target_word):
    word_count = 0
    words = text.split()

    for word in words:
        if word == target_word:
            word_count += 1

    return word_count

# Test the function
paragraph = "This is a sample paragraph. It contains multiple sentences. The word 'sample' appears multiple times in this paragraph."
target = "sample"
result = count_word_occurrences(paragraph, target)
print(f"The word '{target}' appears {result} times in the paragraph.")
