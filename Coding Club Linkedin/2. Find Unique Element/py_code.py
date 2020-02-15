## Find Unique Element

def find_unique_element(arr):
   '''
   The function will find the only element which is unique in the array.

   Arguments:
   arr -- the integer array

   Returns:
   result -- the unique value in the array
   '''

   result = arr[0]

   for i in range(1, len(arr)):
       result = result ^ arr[i]
    
   return result

arr = [2, 2, 5, 5, 1, 6, 1]
print(find_unique_element(arr))