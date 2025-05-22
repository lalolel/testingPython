# Import the random module to generate random numbers
import random

# Set up the person asking the question and their question
name = "Joe"
question = "Will I win the lottery?"

# Initialize an empty string to store the Magic 8 Ball's answer
answer = ""

# Generate a random integer between 1 and 9 (inclusive)
random_number = random.randint(1, 9)

# Uncomment the line below if you want to see what random number was generated
#print(random_number)

# Use conditional statements to assign an answer based on the random number
if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
else:
  # This else clause handles any unexpected values (though shouldn't occur with randint(1,9))
  answer = "Error"

# Display the question that was asked
print(name + " asks: " + question)

# Display the Magic 8 Ball's randomly selected answer
print("Magic 8 Ball's answer: " + answer)
