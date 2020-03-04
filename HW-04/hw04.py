#########################################################################
##########                Gokhan HAS - 161044067               ##########
#########################################################################


#########################################################################

## QUESTION 1 ....

## A part is in the report file.

## B part 
def convert_special(array2D):
    for i in range(0, len(array2D) - 1):
        for j in range(0, len(array2D[0]) - 1):
            if(array2D[i][j] + array2D[i+1][j+1] > array2D[i][j+1] + array2D[i+1][j]):
                array2D[i][j+1] += (array2D[i][j] + array2D[i+1][j+1]) - (array2D[i][j+1] + array2D[i+1][j])
                                
## C part :
def merge(arr, l, m, r): 
    n1 = m - l + 1
    n2 = r- m 
  
    L = [0] * (n1) 
    R = [0] * (n2) 
  
    for i in range(0 , n1): 
        L[i] = arr[l + i] 
  
    for j in range(0 , n2): 
        R[j] = arr[m + 1 + j] 
   
    i = 0     
    j = 0    
    k = l     
  
    while i < n1 and j < n2 : 
        if L[i] <= R[j]: 
            arr[k] = L[i]; i += 1;
        else: 
            arr[k] = R[j]; j += 1;
        k += 1;
  
    while i < n1: 
        arr[k] = L[i]; i += 1; k += 1;
  
    while j < n2: 
        arr[k] = R[j]; j += 1; k += 1;
  
def mergeSort(arr,l,r): 
    if l < r: 
        m = (int)((l+(r-1))/2)

        mergeSort(arr, l, m) 
        mergeSort(arr, m+1, r) 
        merge(arr, l, m, r) 



def find_leftmost_minimum(array2D):
    returnArray = []
    for i in range(0, len(array2D)):
        mergeSort(array2D[i], 0, len(array2D[i]) - 1)
        returnArray.append(array2D[i][0])
    
    print("The leftmost minumum array is {}.".format(returnArray))


## D part is in the report file.






#########################################################################

## QUESTION 2 ....
# Actually, k is k - 1, attention to driver code ...
def find_kth(array1, array2, k):

    if (len(array1) == 0):
        return array2[k]
    elif (len(array2) == 0):
        return array1[k]

    mid1 = (int)(len(array1) / 2)
    mid2 = (int)(len(array2) / 2)

    if (mid1 + mid2 < k):
        if(array1[mid1] > array2[mid2]):
            return find_kth(array1, array2[mid2 + 1 : ], k - mid2 - 1)
        else:
            return find_kth(array1[mid1 + 1 : ], array2, k - mid1 - 1)
    else:
        if (array1[mid1] > array2[mid2]):
            return find_kth(array1[: mid1], array2, k)
        else:
            return find_kth(array1, array2[: mid2], k)
    

#########################################################################

## QUESTION 3 ....
## Global variable in this code ....
index1 = 0;
index2 = 0;

def find_max_crossing_subarray(array, low, mid, high):
    
    global index1,index2;

    sum_x = 0
    left_sum = -9999999   # negative infinite

    for i in range(mid, low-1, -1):
        sum_x += array[i]

        if(sum_x > left_sum):
            left_sum = sum_x
            index1 = i

    sum_x = 0
    right_sum = -9999999  # negative infinite

    for i in range(mid + 1, high + 1):
        sum_x += array[i]

        if(sum_x > right_sum):
            right_sum = sum_x
            index2 = i

    return left_sum + right_sum



def find_max_subarray(array, low, high):
    if (high == low):
        return array[low]
    else:
        mid = (int)((low + high) / 2)
        return max(find_max_subarray(array, low, mid), find_max_subarray(array, mid + 1, high), find_max_crossing_subarray(array, low, mid, high))


def return_max_subarray(array):
    global index1,index2;
    index1=0;
    index2=0;     
    n = len(array);
    subArray = []
    max_sum = find_max_subarray(array, 0, n-1)

    for i in range(index1, index2 + 1):
        subArray.append(array[i])
    
    print("The contiguous subset with the largest sum is {} whose sum is {}.".format(subArray, max_sum))


#########################################################################

## Question 4 .... 
## This algorithm mark 1 or 0 ( one and zero )

def determine_graph(graph_G, V, subArray, index, oneORzero):
    if (subArray[index] != -1 and subArray[index] != oneORzero):
        return False

    subArray[index] = oneORzero;   result = True;
    for i in range(0, len(graph_G)):
        if (graph_G[index][i]):
            if(subArray[i] == -1):
                result = result and determine_graph(graph_G,len(graph_G), subArray, i, 1 - oneORzero)

            if(subArray[i] != -1 and subArray[i] != 1 - oneORzero):
                return False
        
        if(not result):
            return False
    return True



def isBipartite_decreaseANDconquer(graph_G):
    return determine_graph(graph_G,len(graph_G), [-1] * len(graph_G), 0, 1)


#########################################################################

## Question 5 ....

def find_good_day_index(array, n):
    if (n == 1):
        return 0;
    elif (n == 2):
        if (array[0] > array[1]):
            return 0;
        else:
            return 1;
    else:
        middle = (int)(n / 2)
        leftArray = array[0:middle];    leftMax = find_good_day_index(leftArray, len(leftArray));
        rightArray = array[middle:n];    rightMax = find_good_day_index(rightArray, len(rightArray)) + middle;

        if(array[leftMax] > array[rightMax]):
            return leftMax
        else:
            return rightMax
        

def find_good_day(coinArray, priceArray):
    ## coinArray and priceArray lengths must be same.
    gainArray = []
    if(len(coinArray) == len(priceArray)):
        for i in range(0, len(coinArray)):
            gainArray.append(priceArray[i] - coinArray[i])
        print("The gain array is {}. And the buy the goods {}th day.".format(gainArray,find_good_day_index(gainArray,len(gainArray)) + 1))
    else:
        print("ERROR !")



#########################################################################


###########################################
###             DRIVER CODE             ###
###########################################


## Driver Code for Question 1-B ...
print("\n#################### DRIVER CODE FOR QUESTION 1-B ####################")
array = [[37, 23, 22, 32],
         [21, 6, 7, 10],
         [53, 34, 30, 31],
         [32, 13, 9, 6],
         [43, 21, 15, 8]]

print("Normal 2D Array : ")
print(array)
print("\nSpecial Array : ")
convert_special(array)
print (array)

print("\n#################### DRIVER CODE FOR QUESTION 1-C ####################")
find_leftmost_minimum(array)


## Driver Code for Question 2 ...
print("\n#################### DRIVER CODE FOR QUESTION 2 ####################")
arr1 = [2,3,6,7,9]
arr2 = [1,4,8,10]
k = 5
x = find_kth(arr1, arr2, k - 1)
print("Array 1 : ",arr1)
print("Array 2 : ",arr2)
print("K : ",k)
print("Result is : ",x)


## Driver Code for Question 3 ...
print("\n#################### DRIVER CODE FOR QUESTION 3 ####################")
arr = [5, -6, 6, 7, -6, 7, -4, 3]
print("Array : ", arr)
return_max_subarray(arr)


## Driver Code for Question 4 ...
print("\n#################### DRIVER CODE FOR QUESTION 4 ####################")
graph_Deneme = [[0,1,0,1],
                [1,0,1,0],
                [0,1,0,1],
                [1,0,1,0]]
print("Graph : ", graph_Deneme)
if isBipartite_decreaseANDconquer(graph_Deneme):
    print("Yes, Graph is BIPARTITE.\n")
else:
    print("Noi Graph is NOT BIPARTITE.\n")

graph_Deneme =  [ [1, 2], [2, 3], [2, 8], [3, 4], [4, 6], [5, 7],
		[5, 9], [8, 9], [2, 4]]

print("Graph : ", graph_Deneme)
if isBipartite_decreaseANDconquer(graph_Deneme):
    print("Yes, Graph is BIPARTITE.")
else:
    print("Noi Graph is NOT BIPARTITE.")

## Driver Code for Question 5 ...
print("\n#################### DRIVER CODE FOR QUESTION 5 ####################")
C = [5,11,2,21,5,7,8,12,13]
P = [7,9,5,21,7,13,10,14,20]
find_good_day(C,P)
print("\n")