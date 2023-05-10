def cyclicRotate(list_to_rotate):
     print ([list_to_rotate[-1]] + list_to_rotate[0:-1])
 
# Driver program
if __name__ == "__main__":
    list_to_rotate = [1, 2, 3, 4, 5]
    cyclicRotate(list_to_rotate)