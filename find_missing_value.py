starting_index = int(input("Enter the first number: "))
last_index = int(input("Enter the second number: "))

range_list = range(starting_index,last_index)


elements_in_your_list = int(input("Enter your list size: "))

your_list = []

for i in range(elements_in_your_list):

    value_to_append = input("Enter the value for list1:")
    value_to_append = int(value_to_append)
    your_list.append(value_to_append)


print([element for element in range_list if element not in your_list])