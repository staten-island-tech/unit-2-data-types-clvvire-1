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
""" def find_factors(n):
    if n <= 0:
        return "Please enter a number."
    
    factors = []
    for i in range(2, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

def factor():
    number = int(input("Enter a number: "))
    print(f"The factors of {number} are: {find_factors(number)}")
factor() """

#CHALLENGE 5

#Python Mad Libs Project

# Step 1: Receive user input
""" verb1 = input("Enter a verb: ")
verb2 = input("Enter another verb: ")
noun1 = input("Enter a noun: ")
number = input("Enter a number: ")
celebrity_guest = input("Enter a celebrity name: ")
food = input("Enter a food: ")

# Step 2: Create the madlib story using f-string
madlib = f """"""
First day of school and suddenly {celebrity_guest} showed up to lunch. And everyone was so surprised, but {noun1} punched {celebrity_guest} 
and they started to run after each other! {noun1} {verb1} and then she {verb2} and chased her through the playground. But when {noun1} tripped, {celebrity_guest} ranned away!
And then {celebrity_guest} went back to school to eat {number} amount of {food}
"""

""" # Step 3: Print the madlib
print(madlib) """