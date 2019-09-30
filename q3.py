# ### Problem 3
# Given 2 lists of claim numbers, write the code to merge the 2 lists provided to produce a new list by alternating values between the 2 lists. Once the merge has been completed, print the new list of claim numbers (DO NOT just print the array variable!)
# ```
# # Start with these lists
list_of_claim_nums_1 = [2, 4, 6, 8, 10]
list_of_claim_nums_2 = [1, 3, 5, 7, 9]
# making new list
claims = []
# creating function to merge numbers
def merger(list1, list2):
    for eachNum in list1:
        claims.append(eachNum)
    for eachNum in list2:
        claims.append(eachNum)
    return claims
# calling fucntion
merger(list_of_claim_nums_1, list_of_claim_nums_2)
for i in claims:
    print(f'The new list contains {i}')
# ```
# Example Output:
# ```
# The newly created list contains:     2  1  4  3  6  5  8  7  10  9
# ```
