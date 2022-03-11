def sort_list(list1):
    n = len(list1)
    i = 0
    try:
        while (i < n):
            
            j = 0
            while (j < n - i - 1) :
                if (list1[j] > list1[j+1]):
                    temp = list1[j]
                    list1[j] = list1[j+1]
                    list1[j+1] = temp
                j += 1
            i += 1    
        return list1
    except:
        print("Invalid Input")


def printL(list1):
    for i in range(len(list1)):
        print(list1[i])

# abc= [1,6,4,2,6]
abc = ['a', 'c','r', 'b']

printL(sort_list(abc))




