'''
leet code ref
https://leetcode.com/problems/median-of-two-sorted-arrays/?envType=problem-list-v2&envId=array
'''

def median(l1, l2):

    new =  sorted(l1 + l2)
    print(f"Sorted array is {new}")


    lenth =  len(new)

    if lenth % 2 == 1:
        return new[lenth // 2]
    else:
        m1 = new[lenth // 2]
        m2 = new[lenth // 2 - 1]
        median = (m1 + m2) / 2
    return median
num1 = [1, 3, 4, 5, 6]
num2 = [3, 5]

print(median(num1, num2))''
