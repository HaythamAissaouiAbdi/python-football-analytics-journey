# Python Day 2: Numbers, Strings, Conversion, and f-strings

# Goal:
# Practice strings, numbers, type conversion, and clean output with f-strings.


# 1. Review: create variables for your name, school year, and football position.
# Print them in one sentence using an f-string.

name = "Haytham"
school_yr = "4 Eso"
football_pos = "CAM"

print(f"Hello, my name is {name}, I study in {school_yr} and my football position is {football_pos}")

# 2. Create these variables:
# - average_grade as a float, for example 9.8
# - training_minutes as an int, for example 150
# - intensity as an int from 1 to 10
# Print each one with a clear label using f-strings.

avg_grade = float(input("Avg grade: "))
training_minutes = int(input("Training mins: "))
intensity = int(input("intensity (1-10): "))

print(f"My average grade {avg_grade} alongside it I trained {training_minutes} today with an intensity of {intensity}")

# 3. Ask the user for their name.
# Print:
# - the name normally
# - the name in uppercase
# - the number of characters in the name

user_name = input("name: ")
print(f"{user_name.capitalize()}\n{user_name.upper()}\n{len(user_name)}")

# 4. Ask the user for minutes trained today.
# Convert the answer to an integer.
# Print: "You trained for ___ minutes today."

mins_trained = int(input("mins trained: "))
print(f"you trained for {mins_trained} minutes")

# 5. Ask the user for their average grade.
# Convert the answer to a float.
# Print: "Your average grade is ___."

user_avg = float(input("avg grade: "))
print(f"Your average grade is {user_avg}")

# 6. Ask for two decimal numbers.
# Convert them with float().
# Print their sum, difference, product, and division.

two_decimals1 = float(input("Give me one decimal number "))
two_decimals2 = float(input("Give another decimal number "))
print(f"Sum {two_decimals1 + two_decimals2} \n Diff {two_decimals1 - two_decimals2} \n Product {two_decimals1 * two_decimals2}  \n Division {two_decimals1/two_decimals2}")

# Challenge: polished training report
# Ask for:
# - player name
# - minutes trained
# - intensity from 1 to 10
# - average grade
#
# Then calculate:
# - load_score = minutes * intensity
#
# Print a clean report using f-strings.
#
# Example:0
# Player: Haytham
# Minutes: 150
# Intensity: 8/10
# Load score: 1200
# Average grade: 9.8

player_name = input("Name: ")
min_trained = int(input("MIns trained: "))
user_intensity = int(input("intensity (1-10): "))
average_grade = float(input("Avg grade: "))

load_score = min_trained * user_intensity

print(f"My name is {player_name} i trained {min_trained} with an intensity of {user_intensity} giving me a load score of {load_score}. Btw my avg at school is {average_grade}")

