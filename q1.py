# ### Problem 1
# Ask the user to enter a number. 
# Using the provided list of numbers, use a for loop to iterate the array and print out all the values that are smaller than the user input and print out all the values that are larger than the number entered by the user.


useNum = int(input("Enter a number: "))
# ```
# # Start with this List
list_of_many_numbers = [12, 24, 1, 34, 10, 2, 7]
# Comparing useNum to the number list

for eachNumber in list_of_many_numbers:
    # for the smaller numbers
    if eachNumber < useNum:
        print(f'{eachNumber} are smaller than {useNum}')
        # for the larger numbers
    if eachNumber > useNum:
        print(f'{eachNumber} are larger than {useNum}')
# ```
# Example Input/Output if the user enters the number 9:
# ```
# The User entered 9
# 1  2  7 are smaller than 9
# 12  24  34  10 are larger than 9
# ```
