# Python Day 5: Lists and Indexing

# Goal:
# Store multiple values in lists, access them with indexes, change them, and loop through them.


# 1. Create a playlist
# Create a list called playlist with 5 song names.
# Print the whole list.

playlist = ['Le goon','Mj ahh','Nigg','gut genug','king von']

# 2. Indexing
# Print:
# - the first song
# - the third song
# - the last song
#
# Remember: Python starts counting at 0.

print(f'{playlist[0]} \n{playlist[2]} \n{playlist[-1]}')

# 3. Changing a list
# Change the second song to a different song.
# Print the updated playlist.

playlist[1] = 'Mj grape'

print(f'{playlist}')

# 4. Adding items
# Ask the user for a new song.
# Add it to the playlist using .append().
# Print the updated playlist.

new_song = input('Tell me a song: ')
playlist.append(new_song)

print(f'{playlist}')

# 5. List length
# Print how many songs are in the playlist using len().

print(len(playlist))

# 6. Loop through the playlist
# Use a for loop to print each song on its own line.

for song in playlist:
    print(song)


# 7. Shopping cart total
# Create a list called prices with at least 5 decimal numbers.
# Use a for loop to calculate the total price.
# Print the total.

prices = [6.97, 12.22, 8.99, 2.93, 5.66, 23.2]
total = 0

for cost in prices:
    total = cost + total
print(total)


# Challenge: game inventory
# Create an empty list called inventory.
#
# Ask the user for 3 items.
# Add each item to the inventory.
#
# Then print:
# - the full inventory
# - the first item
# - the number of items
#
# Bonus:
# Loop through the inventory and print:
# "You have: item"

inventory = []

item1 = input('Ask for an item: ')
inventory.append(item1)

item2 = input('Ask for a second item: ')
inventory.append(item2)

item3 = input('Ask for a third item: ')
inventory.append(item3)

print(f'{inventory} \n{inventory[0]} \n{len(inventory)}')

for item in inventory:
    print(f"You have: {item}")