#BUBBLE_SORT
#SPACE - o(n)
#TIME - o(n2)

# in place swap
# not that much important but good to know 

def bubble_sort(ls):
    
    lenth = len(ls)
    flag = True

    while flag:

        flag = False

        for i in range(1, lenth):
            
            if ls[i-1] > ls[i]:
                flag = True
                ls[i], ls[i-1] =  ls[i-1], ls[i]
    return ls
ls = [-2, 3, -1, 5]
print(bubble_sort(ls))
