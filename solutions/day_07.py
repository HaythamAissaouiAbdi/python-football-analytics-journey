# Python Day 7: Review Challenge

# Goal:
# Build a menu-based points tracker using everything from Days 1-6.


# Project: points tracker
#
# Create an empty list called scores.
#
# Keep showing this menu until the user quits:
#
# 1. Add score
# 2. View scores
# 3. View stats
# 4. Remove score
# 5. Quit
#
# Requirements:
#
# Option 1:
# - Ask the user for a score as an integer.
# - Add it to the scores list.
# - Print a confirmation.
#
# Option 2:
# - Print the full scores list.
# - Then loop through the list and print each score on its own line.
#
# Option 3:
# - If the list is empty, print "No scores yet".
# - Otherwise print:
#   - total
#   - average
#   - highest score
#   - lowest score
#
# Option 4:
# - Ask the user which score they want to remove.
# - If that score is in the list, remove it.
# - Otherwise print "Score not found".
#
# Option 5:
# - Print "Goodbye".
# - Stop the loop.
#
# Any other option:
# - Print "Invalid option".
#
# Bonus:
# Make the menu output clean with f-strings and \n.

scores = []

while True:
    print(f'1. Add scores \n2. View Scores \n3. View Stats \n4. Remove Score \n5. Quit')
    choice = int(input('Choose: '))

    if choice == 1:
        score = int(input('Score: '))
        scores.append(score)
        print(f'{score} was succesfully added!')
    elif choice == 2:
        print(scores)
        for i in scores:
            print(i)
    elif choice == 3:
        if len(scores) == 0:
            print('No scores added yet!')
        else:
            print(f'Total: {sum(scores)} \nAverage: {sum(scores) / len(scores)} \nHighest score: {max(scores)} \nLowest score: {min(scores)}')
    elif choice == 4:
        remove_score = int(input('What score to remove: '))

        if remove_score in scores:
            scores.remove(remove_score)
            print(f'{remove_score} removed succesfully!')
        else:
            print('Score not found')
    elif choice == 5:
        print('Goodbye')
        break
    else:
        print('Invalid option')



















