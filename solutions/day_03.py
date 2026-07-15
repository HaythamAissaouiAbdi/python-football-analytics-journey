
# Python Day 3: Conditionals

# Goal:
# Use if, elif, and else to make programs choose what to do.


# 1. Password check
# Ask the user for a password.
# If it equals "python123", print "Access granted".
# Otherwise, print "Access denied".

password = input("password: ")

if password == "python123":
    print(f"Access Granted")
else:
    print(f"Access Denied")

# 2. Simple age check
# Ask the user for their age.
# If they are 18 or older, print "You can enter".
# Otherwise, print "You are too young".

age = int(input("AGE: "))

if age >= 18:
    print(f"You can enter")
else:
    print("You are too young")

# 3. Game health system
# Create a variable called health.
# If health is greater than 70, print "Strong".
# If health is between 30 and 70, print "Careful".
# If health is below 30, print "Danger".

health = int(input("Health: "))

if health > 70:
    print("Strong")
elif health >=30:
    print("Careful")
else:
    print("Danger")

# 4. Temperature advice
# Ask the user for the temperature.
# If it is 30 or more, print "Wear light clothes".
# If it is between 15 and 29, print "Normal weather".
# Otherwise, print "Take a jacket".

temperature = int(input("temperature: "))

if temperature >=30:
    print("Wear light clothes")
elif temperature >=15:
    print("Normal weather")
else:
    print("Take a jacket")

# 5. Number comparison
# Ask for two numbers.
# Print which number is bigger, or print "They are equal".

Num1 = int(input("say a number "))
Num2 = int(input("say another number "))

if Num1 > Num2:
    print(f'{Num1} is bigger')
elif Num1 < Num2:
    print(f'{Num2} is bigger')
else:
    print('they are the same')


# 6. Mini shop discount
# Ask the user for the price of an item.
# If the price is 100 or more, apply a 20% discount.
# If the price is 50 or more, apply a 10% discount.
# Otherwise, no discount.
# Print the final price.

item_price = float(input("Item price: "))

if item_price >= 100:
    print(f'new cost is {item_price *0.8}')
elif item_price >=50:
    print(f'new cost is {item_price *0.9}')
else:
    print(f"No discount. Final price is {item_price}")

# Challenge: mini decision game
# Ask the player:
# "You find a locked door. Do you choose key, kick, or leave?"
#
# If they choose "key", print that the door opens.
# If they choose "kick", print that they hurt their foot.
# If they choose "leave", print that they walk away safely.
# Otherwise, print "Invalid choice".
#
# Bonus:
# Use .lower() so "KEY", "Key", and "key" all work.

game = input("You find a locked door. Do you choose key, kick, or leave? ").lower()

if game == 'key':
    print('The door opens')
elif game == 'kick':
    print('You hurt your foot')
elif game == 'leave':
    print('You walk away safely')
else:
    print('Invalid choice')