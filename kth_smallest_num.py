
kth_num = int(input("Enter the k'th term: "))

nth_index_of_list = int(input("Enter the list size: "))

list_of_values_list = []

for i in range(nth_index_of_list):

    value_to_append = input("Enter the value for list:")
    value_to_append = int(value_to_append)
    list_of_values_list.append(value_to_append)


new_list = list_of_values_list.copy()

new_list.sort()

the_value = new_list[kth_num-1]
print(the_value)