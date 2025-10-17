import numpy as np

print(np.__version__)

my_list = [1, 2, 3, 4, 5]

print("my_list = ", my_list)

print("my_list*2 = ", my_list*2)

# in numpy array multiplication is element-wise
my_array = np.array(my_list)


print("my_array type ", type(my_array))
print("my_array = ", my_array)
print("my_array * 2 = ", my_array*2)