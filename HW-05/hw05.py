#########################################################################
##########                Gokhan HAS - 161044067               ##########
#########################################################################


#########################################################################
### QUESTION 1 ...

def optimalBusiness(n, M, ny_arr, sf_arr):
    ny = [0] * n;     
    sf = [0] * n;    

    for i in range(0, n):
        ny[i] = ny_arr[i] + min(ny[i-1], (M + sf[i-1]))
        sf[i] = sf_arr[i] + min(sf[i-1], (M + ny[i-1]))

    return min(ny[n-1], sf[n-1])

#########################################################################
### QUESTION 2 ...

def find_max_symposium(s_arr, f_arr):

    sorting = list(range(len(s_arr)))
    sorting.sort(key=lambda x: f_arr[x])
 
    return_arr = set()
    j = 0
    for i in sorting:
        if (s_arr[i] >= j):
            return_arr.add(i)
            j = f_arr[i]
 
    return return_arr
  
#########################################################################
### QUESTION 3 ...


def returnPositives(arr):
    sum_p = 0
    for i in range(0,len(arr)):
        if arr[i] > 0:
            sum_p += arr[i]
    return sum_p

def returnNegatives(arr):
    sum_n = 0
    for i in range(0,len(arr)):
        if arr[i] < 0:
            sum_n += arr[i]
    return sum_n     


def getSubset(booleanArr, arr, sum_x):
    subset = []
    min_x = returnNegatives(arr)
    max_x = returnPositives(arr)

    if(sum_x < min_x or sum_x > max_x or (not booleanArr[len(arr) - 1][sum_x - min_x])):
        return subset
    
    for i in range(len(arr)-1,-1,-1):
        if (arr[i] == sum_x):
            subset.append(arr[i])
            return subset
        elif (not booleanArr[i-1][sum_x - min_x]):
            subset.append(arr[i])
            sum_x = sum_x - arr[i]

    return subset


def solve(booleanArr, arr):
    min_x = returnNegatives(arr)
    max_x = returnPositives(arr)
    for i in range(0, len(arr)):
        for j in range(min_x, max_x):
            if i == 0:
                booleanArr[i][j - min_x] = (arr[i] == j)
            
            elif(min_x <= j - arr[i] and j - arr[i] <= max_x):
                booleanArr[i][j - min_x] = (arr[i] == j) or (booleanArr[i-1][j-min_x]) or (booleanArr[i-1][j - min_x - arr[i]])
            
            else:
                booleanArr[i][j - min_x] = arr[i] == j or booleanArr[i-1][j - min_x]

    return booleanArr


def cal():
    arr = [-1,6,4,2,3,-7,-5]
    _min = returnNegatives(arr)
    _max = returnPositives(arr)
    booleanArr = [[False] * (_max - _min + 1)] * len(arr)
    
    booleanArr = solve(booleanArr, arr)

    subSetArr = []
    subSetArr = getSubset(booleanArr,arr,0)

    print("Array is {}".format(arr))
    if(booleanArr[0][0] == True):
        print("Result is : True")
    else:
        print("Result is : False")



#########################################################################
### QUESTION 4 ...

def string_matching(str1, str2, miss, gap, match):
    
    m = len(str1)
    n = len(str2)
    maxVal = -11111
    dp = [[None]*(n) for j in range(m)]
    dp[0][0] = 0

    for i in range(1,m):
        dp[i][0] = i * gap
    
    for i in range(1,n):
        dp[0][i] = i * gap
    
    for i in range(1,m):
        for j in range(1,n):

            if str1[i-1] == str2[j-1]:
                dp_max = match
            else:
                dp_max = miss

            dp[i][j] = max(dp[i][j-1] + gap, dp[i-1][j] + gap, dp[i-1][j-1] + dp_max)

            if dp[i][j] >= maxVal:
                maxVal = dp[i][j]
    
    return maxVal

    
#########################################################################
### QUESTION 5 ...

def calc_operation(arr):
    _sum = 0
    newArr = [0] * (len(arr))
    for i in range(0,len(arr)):
        newArr[i] = arr[i]
    _min = min(newArr)
    newArr.remove(_min)
    while (len(newArr) != 0):
        _new_min = min(newArr)
        newArr.remove(_new_min)
        _min = _min + _new_min
        _sum = _sum + _min
    return _sum
    

###########################################
###             DRIVER CODE             ###
###########################################

## Driver Code for Question 1 ...

def driverQuestion1():
    n = 4;
    M = 10;
    ny_arr = [1,3,20,30]
    sy_arr = [50,20,2,4]
    
    print("n = {}   M = {}    NY = {}   SY = {}".format(n, M, ny_arr, sy_arr))
    print("RESULT : ", optimalBusiness(n,M,ny_arr,sy_arr))

print("\n#################### DRIVER CODE FOR QUESTION 1 ####################")
driverQuestion1()


## Driver Code for Question 2 ...
def driverQuestion2():
    s = [0 , 1 , 3 , 3 , 4 , 5, 6, 9] 
    f = [6 , 4 , 5 , 8 , 7 , 9, 10, 11] 
    x = find_max_symposium(s , f)
    print("START  = {}".format(s))
    print("FINISH = {}".format(f))
    print("Max count is {}. Symposium indexes are {}.".format(len(x),x))    

print("\n#################### DRIVER CODE FOR QUESTION 2 ####################")
driverQuestion2()


def driverQuestion3():
    cal()


print("\n#################### DRIVER CODE FOR QUESTION 3 ####################")
driverQuestion3()


def driverQuestion4():
    str1 = "ALIGNMENT"
    str2 = "SLIME"

    print("String 1 is {}".format(str1))
    print("String 2 is {}".format(str2))

    result = string_matching(str1,str2,-2,-1,2)
    print("Result is {}".format(result))



print("\n#################### DRIVER CODE FOR QUESTION 4 ####################")
driverQuestion4()



def driverQuestion5():
    arr = [1,2,3,4,5]
    result = calc_operation(arr)

    print("Array is {}".format(arr))
    print("Result is {}".format(result))


print("\n#################### DRIVER CODE FOR QUESTION 5 ####################")
driverQuestion5()