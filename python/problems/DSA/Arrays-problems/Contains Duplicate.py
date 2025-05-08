'''
https://leetcode.com/problems/contains-duplicate/description/?envType=problem-list-v2&envId=array
'''
def remove_duplicates(num):

    ls = []

    for i in num:
        if num.count(i) > 1:
            return True
    else:
        return False

num = [3, 4, 5, 6]
print(remove_duplicates(num))
