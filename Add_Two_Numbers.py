# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.



nth_index_of_list_1 = int(input("Enter the list1 size: "))
nth_index_of_list_2 = int(input("Enter the list2 size: "))

list_of_values_list_1 = []
list_of_values_list_2 = []


for i in range(nth_index_of_list_1):

    value_to_append = input("Enter the value for list1:")
    value_to_append = int(value_to_append)
    list_of_values_list_1.append(value_to_append)



for i in range(nth_index_of_list_2):

    value_to_append = input("Enter the value for list2:")
    value_to_append = int(value_to_append)
    list_of_values_list_2.append(value_to_append)



first_joined_number = ''.join(map(str, list_of_values_list_1))
second_joined_number = ''.join(map(str, list_of_values_list_2))

final_added_number = int(first_joined_number) + int(second_joined_number)

print(final_added_number)

