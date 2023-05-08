#finding n-th number of the fibonacci series

nth_value = int(input("Enter the number: "))

zero = 0
one = 1

the_list_of_elements = []

the_list_of_elements.append(zero)
the_list_of_elements.append(one)

for i in range(nth_value):
    new_value_to_append = zero + one 
    the_list_of_elements.append(new_value_to_append)
    zero = one 
    one = new_value_to_append


print(the_list_of_elements[nth_value])
    
