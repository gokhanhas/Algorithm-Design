# Gokhan HAS - 161044067
# Introduction to Algorithm - HW03 


# -----------------------------------------------------------
# Question 3 ...
# -----------------------------------------------------------

# Global variables for sort algorithm's swaps count ...
quickSort_count = 0
insertionSort_count = 0

###########  Quick Sort Algorithm ########### 
def quick_sort(array, l, r):
    if l < r:
        s = hoare_partition(array, l, r)
        quick_sort(array, l, s)
        quick_sort(array, s + 1, r)


# This is the Hoare Partition methods which we were written pseudocode in 28.11.2019 Lecture ...
def hoare_partition(array, l, r):
    global quickSort_count
    p = array[l]
    i = l - 1
    j = r + 1

    while True:

        i += 1
        while array[i] < p:
            i += 1
        
        j = j - 1
        while array[j] > p:
            j = j - 1
       
        if i >= j:
            return j

        array[i],array[j]=array[j],array[i]     # swap the elements ...
        quickSort_count += 1
        

########### Insertion Sort Algorithm ########### 
def insertion_sort(array):
    global insertionSort_count
    for i in range(1,len(array)):
        v = array[i]
        j = i - 1

        while j >= 0 and array[j] > v:
            array[j + 1] = array[j]     # swap the elements ...
            j -= 1
            insertionSort_count += 1
        array[j + 1] = v



# -----------------------------------------------------------
# Question 4 ...
# -----------------------------------------------------------

def find_median(array):
    ## Call insertion sort.
    ## Because insertion sort algorithm is decrease-and-conquer algorithm ...
    insertion_sort(array)
    length = len(array)
    
    if length % 2 == 0: 
        return float( ( array[int((length - 1) / 2)] + array[int(length / 2)] ) / 2.0)
    
    return float(array[int(length/2)]) 
      


# -----------------------------------------------------------
# Question 5 ...
# -----------------------------------------------------------

# Calculates SumB function according to hw pdf ...
def calculate_sum(array):
    n = len(array)
    minElement = min(array)
    maxElement = max(array)

    return float((minElement + maxElement) * (n / 4.0))

# It is a recursive function that find all sublist in a list ...
def nth_sublist(array, n):
    return_list = []
    if n > 0:
        for i in range(0, len(array)):
            new_array = array[0:i] + array[i+1:]
            return_list += [new_array]
            return_list.extend(nth_sublist(new_array, n - 1))
    return return_list

# Clear the sublists array 
def clear_duplicates(array): 
    output_list = [] 
    for i in array: 
        if i not in output_list: 
            output_list.append(i) 
    return output_list 

# It is the helper function that multp. array (list) elements ...
def multiplyList(array) : 
      
    result = 1
    for i in array: 
         result = result * i  
    return result 

# Return optimal sub-array ...
def find_optimal(array):
    sumB = calculate_sum(array)
    tempList = nth_sublist(array,len(array))
    subLists = clear_duplicates(tempList)
    optimumSubList = []
    multiply_list = []
    
    for i in range(0,len(subLists)):
        
        if(sum(subLists[i]) >= sumB):
            optimumSubList.append(subLists[i])
            multiply_list.append(multiplyList(subLists[i]))

    return optimumSubList[multiply_list.index(min(multiply_list))]



########################## DRIVER CODE ##############################

### Test QuickSort and InsertionSort ...
print("############ TEST QUICK-INSERTION SORTS ############\n")

quickSort_count = 0
insertionSort_count = 0

arr1 = [50,49,48,47,46,45]
arr2 = [50,49,48,47,46,45]

quick_sort(arr1,0,len(arr1)-1)
insertion_sort(arr2)

print("FOR EXAMPLE 1 : [50,49,48,47,46,45]")
print("Quick Sort Swaps Count       : %d     " %quickSort_count, arr1)
print("Insertion Sort Swaps Count   : %d     " %insertionSort_count, arr2)
print("\n")

quickSort_count = 0
insertionSort_count = 0

arr1 = [50,49,48,47,46,45,44,43,42,41,40]
arr2 = [50,49,48,47,46,45,44,43,42,41,40]

quick_sort(arr1,0,len(arr1)-1)
insertion_sort(arr2)

print("FOR EXAMPLE 2 : [50,49,48,47,46,45,44,43,42,41,40]")
print("Quick Sort Swaps Count       : %d     " %quickSort_count, arr1)
print("Insertion Sort Swaps Count   : %d     " %insertionSort_count, arr2)
print("\n")


quickSort_count = 0
insertionSort_count = 0

arr1 = [50,49,48,47,46,45,44,43,42,41,40,39,38,37,36,35]
arr2 = [50,49,48,47,46,45,44,43,42,41,40,39,38,37,36,35]

quick_sort(arr1,0,len(arr1)-1)
insertion_sort(arr2)

print("FOR EXAMPLE 3 : [50,49,48,47,46,45,44,43,42,41,40,39,38,37,36,35]")
print("Quick Sort Swaps Count       : %d     " %quickSort_count, arr1)
print("Insertion Sort Swaps Count   : %d     " %insertionSort_count, arr2)
print("\n")



### Test Find Median ...
print("\n############ TEST FIND MEDIAN ############\n")

arr = [2,3,5,8,9,10,1,4,7,6]
print("Find Median for [2,3,5,8,9,10,1,4,7,6] : %f" %find_median(arr))

arr = [4,5,6,11,12,13,8,9,10,14,15,2,3,1,7]
print("Find Median for [4,5,6,11,12,13,8,9,10,14,15,2,3,1,7] : %f\n" %find_median(arr))


### Test Optimum Sub-Array ...
print("\n############ TEST OPTIMUM SUB-ARRAY ############\n")

arr = [2,4,7,5,22,11]
print("The array is [2,4,7,5,22,11]. The optimum sub-array is %a." %find_optimal(arr))

arr = [3,5,7,9,10]
print("The array is [3,5,7,9,10]. The optimum sub-array is %a." %find_optimal(arr))
