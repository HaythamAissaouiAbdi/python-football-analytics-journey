# Python Day 4: Loops

# Goal:
# Use for loops and while loops to repeat code.


# 1. Count from 1 to 10
# Use a for loop to print the numbers from 1 to 10.

for number in range (1,11):
    print(number)

# 2. Countdown
# Use a for loop to print:
# 5
# 4
# 3
# 2
# 1
# Go!

for countdown in range (5,0,-1):
    print(countdown)
print('Go')

# 3. Repeat a message
# Ask the user for a message.
# Ask how many times to repeat it.
# Use a for loop to print the message that many times.

message = input('Say something: ')
times = int(input('How many times do you want it: '))

for i in range (times):
    print(message)

# 4. Sum of numbers
# Ask the user for a number.
# Use a for loop to add all numbers from 1 up to that number.
# Example: if the user enters 5, calculate 1 + 2 + 3 + 4 + 5.
# Print the total.

user_number = int(input('Say a number: '))
total = 0

for i in range (1, user_number + 1):
    total = total+i
print(f"The total is {total}")


# 5. Password loop
# Keep asking the user for a password until they type "python".
# When they get it right, print "Unlocked".

password = ''

while password != 'python':
    password = input('Password: ')
print('Unlocked')


# 6. Menu loop
# Keep showing this menu:
# 1. Say hello
# 2. Say bye
# 3. Quit
#
# If the user chooses 1, print "Hello".
# If the user chooses 2, print "Bye".
# If the user chooses 3, print "Closing menu" and stop the loop.
# Otherwise, print "Invalid option".

while True:
    choice = input("Choose 1, 2, or 3: ")

    if choice == '1':
        print('Hello')    
    elif choice == '2':
        print('Bye')
    elif choice == '3':
        print('Closing menu')
        break
    else:
        print('Invalid option')
    



# Challenge: guessing game
# Set secret_number = 7.
# Keep asking the user to guess the number.
# If the guess is too high, print "Too high".
# If the guess is too low, print "Too low".
# If the guess is correct, print "Correct" and stop.

secret_number = 7
guess = int(input("Guess the number: "))

while guess != secret_number:
    if guess > secret_number:
        guess = int(input("Too high, try again: "))
    else:
        guess = int(input("Too low, try again: "))

print("Correct")