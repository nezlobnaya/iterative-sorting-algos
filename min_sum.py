# Add up and print the sum of the all of the minimum elements of each inner array:
inner_array = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]

def sum_of_min(inner_array):
    total = 0
    for i in inner_array:
        total += min(i)
    print(total)

sum_of_min(inner_array)


# The expected output is given by:
# 4 + -1 + 9 + -56 + 201 + 18 = 175
# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code. 
# Run through the UPER problem solving framework while going through your thought process.