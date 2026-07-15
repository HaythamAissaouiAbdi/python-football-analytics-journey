#Print your name, school year, and football position.

name = "Haytham"
school_year = "4 eso"
football_position = "left winger"

print("Hello, my name is", name, "my position is", football_position, "and Im in", school_year)

#Create a variable for your current average grade and print it.

av_grade = 9.8
print("my avg grade is", av_grade)

#Ask the user for their name and greet them.

username = input("Whats your name? ")
print("sup bro nice to meet you", username)

#Ask for minutes trained today and print a sentence with that number.

time = int(input("How much time did you train today (hrs)? "))
print("you trained ", time, 'hours')

#Ask for two numbers, convert them with int(), and print their sum.

n1 = int(input('say a number '))
n2 = int(input('say another number '))
print('the addition of your numbers is ', n1 + n2)

#Challenge: ask for player name, training minutes, and intensity. Then print a training summary with load score.

chal_name= input('whats ur name? ')
training_mins= int(input('How much did you train?(hrs) '))
intesity= int(input('rate your intensity from 1-10?' ))
print(chal_name, 'your score is ', training_mins * intesity)
