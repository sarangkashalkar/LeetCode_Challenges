# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]

target_value = int(input("Enter the target number: "))


nth_index_of_list = int(input("Enter the list size: "))
list_of_values = []
for i in range(nth_index_of_list):
    # value_to_append = int(input("Enter the value:"))
    value_to_append = input("Enter the value:")
    value_to_append = int(value_to_append)
    list_of_values.append(value_to_append)


for element in list_of_values:
    temp_list = list_of_values[int(element):]

    for i in range(len(temp_list)):


        test_value = list_of_values[element] + temp_list[i]

        try:

            if test_value == target_value:
                print("Hurray!! Found and Done")
                break

        except:
            print("Nah")

        finally:
            print("Bye")
    break