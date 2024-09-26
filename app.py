#CHALLENGE 1
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

#CHALLENGE 2
""" x = 16
if x % 2 == 0:
    print("x is even")
else: 
    print("x is not") """

#CHALLENGE 3
""" service = input("how was the servie? ")
if service == "bad":
    print("0% tip")
if service == "okay":
    print("15% tip")
if service == "good":
    print("20% tip")
if service == "great":
    print("25% tip") """

#CHALLENGE 4
def find_factors(n):
    if n < 1:
        return "enter a number."
    
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    
    return factors

# Example usage:
number = 28
print(f"The factors of {number} are: {find_factors(number)}")