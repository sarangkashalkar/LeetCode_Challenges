#Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.

nth_index_of_list = int(input("Enter the list size: "))

list_of_values_list = []

for i in range(nth_index_of_list):

    value_to_append = input("Enter the value for list:")
    value_to_append = int(value_to_append)
    list_of_values_list.append(value_to_append)

list_of_values_list.sort()
print(list_of_values_list)