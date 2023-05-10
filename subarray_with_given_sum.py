
nth_index_of_list = int(input("Enter the list size: "))
target_value = int(input("Enter the target value: "))

list_of_values_list = []

current_value = None

for i in range(nth_index_of_list):

    value_to_append = input("Enter the value for list1:")
    value_to_append = int(value_to_append)
    list_of_values_list.append(value_to_append)

for element in range(len(list_of_values_list)):

    if list_of_values_list[element] == target_value:
        print("Found at index", list_of_values_list[element])
        break

    else:
        current_value = list_of_values_list[element] + list_of_values_list[element+1]
        if current_value == target_value:
            print("Found at index ", list_of_values_list[element], " and index ", list_of_values_list[element+1])
            break
        else:
            first_element = element.copy()
            next_element = (element+1).copy()

            list_of_values_list[element] = list_of_values_list[element+1]
            list_of_values_list[element + 1] = new_temp