# Python Day 6: List Methods and Simple Stats

# Goal:
# Use list methods and calculate total, average, max, and min.


# 1. Watchlist manager
# Create a list called watchlist with 4 movies or shows.
# Print the list.

watchlist = ['spiderman','batman','invincible','suits','gumball']
print(watchlist)

# 2. Add and remove
# Ask the user for a movie/show to add.
# Add it with .append().
# Ask the user for a movie/show to remove.
# Remove it with .remove().
# Print the updated list.

user_new_movie = input('Add a movie to the watchlist: ').lower()
watchlist.append(user_new_movie)
print(watchlist)

user_remove_movie = input('Do you want to remove a movie from the watchlist? (if no type "No"): ').lower()
if user_remove_movie != 'no':
    watchlist.remove(user_remove_movie)
    print(watchlist)
else: print(watchlist)


# 3. Sort the list
# Sort the watchlist alphabetically using .sort().
# Print the sorted list.

watchlist.sort()
print(f'Heres is the list sorted alphabetically: \n{watchlist}')


# 4. Search the list
# Ask the user for a movie/show to search for.
# If it is in the watchlist, print "Found".
# Otherwise, print "Not found".
#
# Bonus:
# Make the search case-insensitive if you can.

user_search = input("Search for movie in watchlist: ").strip().lower()

lower_watchlist = []

for movie in watchlist:
    lower_watchlist.append(movie.lower())

if user_search in lower_watchlist:
    print(f"{user_search} was found!")
else:
    maybe_new_movie = input(f"{user_search} wasnt found! Would you like to add it? (yes or no) ").lower()

    if maybe_new_movie == "no":
        print(f"{user_search} wont be added.")
    elif maybe_new_movie == "yes":
        watchlist.append(user_search)
        watchlist.sort()
        print(f"{user_search} was added successfully\n{watchlist}")
    else:
        print("Wrong answer bro")

# 5. Score stats
# Create a list called scores with 6 numbers.
# Use a for loop to calculate the total.
# Then calculate the average.
# Print:
# - total
# - average
# - highest score using max()
# - lowest score using min()

scores = [1,5,2,3,4,6]
total = 0

for number in scores:
    total = number+total

print(f'The average is {total/len(scores)} \nTotal is {total} \nHighest score is {max(scores)} \nLowest score is {min(scores)}')

# 6. Build a list from user input
# Create an empty list called names.
# Ask the user for 3 names.
# Add each name to the list.
# Print the full list.
# Then print each name on its own line.

names = []

for i in range(3):
    answer = input('Give me a name: ')
    names.append(answer)
    
print(f'{names} \n{names[0]} \n{names[1]} \n{names[2]}')


# Challenge: simple expense tracker
# Create an empty list called expenses.
# Ask the user for 5 expenses as decimal numbers.
# Add each expense to the list.
#          
# Then calculate and print:
# - full expense list
# - total spent
# - average expense
# - biggest expense
# - smallest expense

expenses = []

for i in range(5):
    thing = float(input('Add an expense: '))
    expenses.append(thing)

print(f'Full expense list: {expenses} \nTotal spent: {sum(expenses)} \nAverage expense: {sum(expenses)/len(expenses)} \nBiggest expense: {max(expenses)} \nSmallest expense: {min(expenses)}')




