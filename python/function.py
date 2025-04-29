'''Notes
'''
'''
def l(a, *args):
    lenth_word=len(a)
    lenth_w=len(args[i])
    print(lenth_word, lenth_w)

l("vijay", ('sugu'))
'''


'''
Write a function that prints "Hello, World!".
def hello(a="Hello World"):
    print(f"{a}")

hello(a="Fuck you !")

'''

'''
def square(a):
    return(a**2)
    

print(square(2))
'''

'''
def summ(a):
    total = 0
    for i in a:
       total += i
    return total

ls = input("Enter a list of number please: ")

total = summ(ls)
'''


'''
def pan(a, *args):
    is_palindromes_pal = a == a[::-1]
    
    for i in range(len(args)):
        reversed_word = args[i][::-1]
        if reversed_word == args[i]:
            print(f"{args[i]} is a palindrom")
        else:
            print(f"{i} is a not palindrom")
    print(is_palindromes_pal)
    
pan("mam",('madam'))
'''


'''
##function for factorial
def fact(a):
    if a < 1:
        print("Enter a number above 1!")
    elif a > 1:
        factorial = 1
        for i in range(1, a+1):
             factorial *=i
        print(factorial)
fact(5)
'''



'''
---//find largest number in a given list
def largest(num):
    new_list = sorted(num)
    print(new_list[-1])
    #return(new_list[-1])


ls = [2,3, 6, 1, 3, 3, 1]
ans = largest(ls)
'''
'''

def vowel(ab):
    vowels = "aeiouAEIOU"
    summ = 0
    for i in ab:
        
        if i in vowels and i == "a" or i == "A":
            summ+=1
    print(summ)
vowel("Writing quick scripts to automate tasks (file parsing, data extraction, API calls).")

'''

'''
def prime(num):
    if num < 1:
        print("Please give a number above 1")
        return
    elif num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
                return(num)

def check(start,end):
      ls = []
      for i in range(3, end):
           if prime(i):
                ls.append(i)
      print(ls)

check(10, 100)
'''

'''
reverse a list
def reverse_list(ls):
    new_list = ls.split()
    #print(new_list)
    reversed_ls = []
    for i in new_list:
        # reversed_ls = i + reversed_ls
          reversed_ls = new_list[::-1]
    print(reversed_ls)

reverse_list("Hello world")

'''

'''
Write a function that takes two lists and returns a list with elements common to both.

def common(list1,list2):
    set1 = set(list1)
    set2 = set(list2)

    new_list = list(set1 & set2)
    print(new_list)

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

common(list1,list2)

'''

'''
def count(v):
    vowels = 'aeiouAEIOU'
    vowel_count = sum(1 for i in v if i in vowels)
    summ = 0
    for i in v:
        if i in vowels and i == 'a':
            summ +=1
    print (f"a was found {summ} times")

    print(vowel_count)

count("aaaaa")
'''

'''
def fibnoci(n):
    a = 0
    b = 1
    for n in range (2, n+1):
        a, b = b, a + b
        print(b)
fibnoci(10)
'''


def dup(a):
    set1 = set(a)
    new_list = list(set1)
    print(new_list)
a = [2, 3, 5, 3, 2, 1]
dup(a)