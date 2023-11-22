my_sentence = "Today is such a beautiful day!"
alphabet_vowels = 'aeiou'
my_sentence_vowels = [char for char in my_sentence if char in alphabet_vowels]  # Your list comprehension here
print(my_sentence_vowels)
# Note: the letter 'A' from the sentence start is missing: 'a' != 'A', and 'A' not in alphabet_vowels, so ignore it
