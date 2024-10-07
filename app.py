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

#CHALLENGE 2
""" x = 16
if x % 2 == 0:
    print("x is even")
else: 
    print("x is not") """

#CHALLENGE 3
""" def calculate_tip(bill):
    service = input("How was the service? (bad, okay, good, great): ")
    tip_percentages = {
        'bad': 0.0,
        'okay': 0.15,
        'good': 0.20,
        'great': 0.25
    }
    tip_percentage = tip_percentages.get(service)
    tip = bill * tip_percentage
    bill_tip = bill + tip
    print(f"For a bill of ${bill:.2f}, the tip is ${tip:.2f}, the whole bill (including tips) is ${bill_tip}.")

bill = 100.00
calculate_tip(bill) """

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
def greatest_common_factor(a,b):
    while b:
        a, b = b, a % b
    return abs(a)

try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
    gcf = greatest_common_factor(num1, num2)
    print(f"The greatest common factor of {num1} and {num2} is: {gcf}")
except ValueError:
    print("Please type a number: ")
