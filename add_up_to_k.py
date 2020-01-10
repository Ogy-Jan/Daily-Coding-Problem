"""
This Problem was asked by Google
Given a slit of numbers and a number k,
return whether two numbers from the list add up to k

Example:
    input list: [10, 15, 3, 7]
    input k: 17

    output: true

    explanation:  10 + 7 = 17
"""

# input_lst = [3, 15, 10, 7]
# input_lst = [1, 3, 3, 3, 4, 4]
# input_lst = []
# input_lst = [0]
input_lst = ['a']
k = 3

answer = False

for item1 in input_lst:
    if answer:
        break
    input_lst_reduced = input_lst.copy()
    input_lst_reduced.remove(item1)  # remove item1 form second list as not to check sum of number to itself
    for item2 in input_lst_reduced:
        if item1 + item2 == k:
            answer = True
            break
        else:
            answer = False
    input_lst.remove(item1)  # remove already checked item from first list as not to double check already checked sums

print("Do at least 2 items in the list add up to k?", answer)

#  achieved BigO of O{(N * (N-1)) / 2}
