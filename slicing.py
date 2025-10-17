import numpy as np

array = np.array([10, 20, 30, 40, 50])

two_d_array = np.array([[0,1,2,3],
                        [4,5,6,7],
                        [8,9,10,11],
                        [12,13,14,15]])


##array[start:stop:step] --------->one dimensional slicing 1d array

 ##array slicing examples
print(array[1:4])  #slicing from index 1 to 3 
print(array[:3])   #slicing from start to index 2

print(array[-1::-1]) #array slicing in reverse order array[start:stop:step] , here start is -1 (last index) and step is -1 (reverse order)
#and stop is empty means go till the start of the array.


# ##array([start:stop:step,start:stop:step] --------->one dimensional slicing 2d array

# print(two_d_array[1:3, 0:2])  #slicing rows from index 1 to 2 and columns from index 0 to 1
# print(two_d_array[:2, 2:])    #slicing first two rows and columns from index 2 to end
# print(two_d_array[::2, ::2])  #slicing every second row and every second column
# print(two_d_array[1::2, 0::2]) #slicing every second

print(two_d_array[1:3,2:])  #slicing rows from index 1 to 2 and columns from index 2 to end
print(two_d_array[0:,0:])   #slicing all rows and all columns ,,,,,,it is same to print(two_d_array)
print(two_d_array[::,::])   #slicing all rows and all columns ,,,,,,it is same to print(two_d_array)

print(two_d_array[-1::-1,-1::-1]) #slicing 2d array in reverse order for both rows and columns #here start is -1 (last index) and step is -1 (reverse order)
#and stop is empty means go till the start of the array.
   
###array[row_index,column_index] --------->accessing single element in 2d array
##slicing defination : Slicing in NumPy refers to the process of extracting a portion of an array by specifying a range of indices along each dimension. It allows you to create sub-arrays or views of the original array without copying the data.