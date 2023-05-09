#Given an unsorted array arr[] of size N having both negative and positive integers. 
# The task is place all negative element at the end of array without changing the order of positive element and 
# negative element.

nth_index_of_list = int(input("Enter the list size: "))

list_of_values_list = []

for i in range(nth_index_of_list):

    value_to_append = input("Enter the value for list:")
    value_to_append = int(value_to_append)
    list_of_values_list.append(value_to_append)

positive_element_list = []
negative_element_list = []

for element in range(len(list_of_values_list)):
    if list_of_values_list[element]<0:
        negative_element_list.append(list_of_values_list[element])

    else:
        positive_element_list.append(list_of_values_list[element])

negative_element_list.sort(reverse=True)
positive_element_list.sort()

new_list_final = positive_element_list+negative_element_list

print(new_list_final)