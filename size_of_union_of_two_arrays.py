# Given two arrays a[] and b[] of size n and m respectively. 
# The task is to find the number of elements in the union between these two arrays.

# Union of the two arrays can be defined as the set containing distinct elements from both the arrays. 
# If there are repetitions, then only one occurrence of element should be printed in the union.

# Note : Elements are not necessarily distinct.


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

final_list = list_of_values_list_1 + list_of_values_list_2  

final_list_set_size = len(set(final_list))

print(final_list_set_size)

