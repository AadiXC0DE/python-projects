def count_word_occurrences(text, target_word):
    word_count = 0
    letter_count = 0
    number_count = 0
    words = text.split()

    for word in words:
        if word == target_word:
            word_count += 1

        for char in word:
            if char.isalpha():
                letter_count += 1
            elif char.isdigit():
                number_count += 1

    return word_count, letter_count, number_count

paragraph = "This is a sample paragraph. It contains multiple sentences. The word 'sample' appears multiple times in this paragraph. There are 123 numbers in this paragraph."
target = "sample"
word_result, letter_result, number_result = count_word_occurrences(paragraph, target)

print(f"The word '{target}' appears {word_result} times in the paragraph.")
print(f"The paragraph contains {letter_result} letters and {number_result} numbers.")
