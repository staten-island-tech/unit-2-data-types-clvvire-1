""" # Start the program
user_input = input("enter a sentence: ")

# a function to count the number of words
def count_words(sentence):
    words = sentence.split()
    # Count the number of words
    return len(words)

# Call the function with the user input and print the result
word_count = count_words(user_input)
print(f"The number of words in your sentence is: {word_count}") """

