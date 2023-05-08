# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

 

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.




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

final_list.sort()  

mid = len(final_list) // 2
res = (final_list[mid] + final_list[~mid]) / 2
 

print("Median of list is : " + str(res))


