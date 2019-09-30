# ### Problem 2
# Prompt the user with the message, ‘Is it better to be rude or kind to People?’ 
# Keeping prompting the user to enter an answer until they enter the word kind. 
# Each time they enter something other than kind, print the message, ‘That’s not the answer I had hoped to hear. Try again.’ and prompt the user again.
# Once the user enters kind, print, ’Now that’s what I wanted to hear!’ and exit the program.

# prompting user
ques = input("Is it better to be rude or kind to people? ").upper()
# starting while loop
while ques != "kind".upper():
    print("That's not the answer i hoped to hear.. Try again: ")
    ques = input("Is it better to be rude or kind to people? ").upper()
# out of the loop
print("Now that's what i want to hear!")
