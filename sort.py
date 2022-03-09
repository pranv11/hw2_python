def sort_list(list1):
    n = len(list1)
    i = 0

    while i < n :
        if type(list1[i]) == int:
            x = 0

            while x < n - i - 1 :
                if list1[x] > list1[x+1]:
                    tmp = list1[x]
                    list1[x] = list1[x+1]
                    list1[x+1] = tmp
                x = x+1
            i += 1
        return list1



def printL(list1):
    for i in range(len(list1)):
        print(list1[i])

try:
    abc = [1,8, 4, 3, 9 ,57]

    printL(sort_list(abc))
except:
    print('the input is incorrect')



