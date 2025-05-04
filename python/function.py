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

'''
def dup(a):
    set1 = set(a)
    new_list = list(set1)
    print(new_list)
a = [2, 3, 5, 3, 2, 1]
dup(a)

'''

'''
a = input("ENter a list")
b = int(input("ENter a target"))

mylist = list(map(int, a.split()))

found = False
for i in range(len(mylist)):
    for j in range(i+1, len(mylist)):
      if mylist[i] + mylist[j] == b:
             print("found")
             found = True
if not found:
    "Nothing found"

'''

'''
palanendrom for number

def pal(num):
    num1 = str(num)
    return num1 == num1[::-1]
    

print(pal(55))

'''
'''

def pyramid(num):
    for i in range(num):
        space = ' ' * (num - i -1)
        star = '*' * (2 * i + 1)
        print(space + star + space)

pyramid(10)

'''
'''
def rev(s):
    new = ''
    for i in s:
        new = i + new
    print(new)

rev('sugu')

'''
'''
def fact(num):
    num1 = 1
    for i in range(1, num+1):
        num1 = i * num1
    print(num1)


fact(100)
'''
'''
def pal(string):
    return string == string[::-1]  

print(pal('sir'))
'''
'''
# fizzbuzz
# Print numbers 1-100, but for multiples of 3, print "Fizz"; for 5, "Buzz"; for both, "FizzBuzz".

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i} - Fizzbuzz")
    elif i % 5 == 0:
        print(f"{i} - Fizz")
    elif i % 3 == 0:
        print(f"{i} - buzz")
'''
'''
In = [2, 7, 11, 15]
target = 9

for i in range(len(In)):
    for j in range(i+1, len(In)):
        if In[i] + In[j] == target:
            print(f"{i}, {j}")
'''

'''
def word_count(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
             char_count[char] = 1
    return char_count
    print(char_count)

print(word_count('Kiruthik devi oru lusu'))
'''
'''
def nonrepeating(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
             char_count[char] = 1
    for ch in string:
        if char_count[ch] == 1:
           return ch
           break
        
print(nonrepeating('sugu'))

'''
'''
2. Best Time to Buy and Sell Stock
Given an array of prices where prices[i] is the price of a given stock on the ith day, find the maximum profit you can achieve.

def max_profit(q):
    m = q[0]
    h = 0

    for i in q[1:]:
        if i < m:
            m = i
        else:
            h = max(h, i-m )
    return(h)

print(max_profit([1, 3, 4, 5, 7]))

'''
'''

def longest(string):
    ls = string.split()

    max = 0
    max_str = ''
    for i in ls:
        if len(i) > max:
            max = len(i)
            max_str = i
    print(max_str, max)

longest("Sugu rohit abcsgegi kjoiajojalmaiouao joiaoiyoahlDJH9R9Hkljifgbk ")
'''

'''
FInd median of the sorted array

def median(num1, num2):

    new_list = sorted(num1 + num2)

    n = len(new_list)
    
    if n % 2 == 1:
        return new_list[n // 2]
    else:
        m1 = new_list[n // 2-1]
        m2 = new_list[n // 2]
        return (m1 + m2) / 2

num1 = [1, 3, 4, 5, 6]
num2 = [3, 5, 99]

print(median(num1, num2))

'''
'''
Product of Array Except Self – LeetCode #238
Return array where each element is product of all others.

def product(n):
   new_arr = [] 

   for i in range(len(n)):
        product = 1
        temp = n[:i] + n[i+1:]
        for j in temp:
            product *= j
        new_arr.append(product)
   return new_arr




arr = [1, 2, 3, 4, 5]
print(product(arr))
'''
'''
def count(string):
    dict = {}
    for char in string:
        if char in dict:
            dict[char] +=1
        else:
            dict[char] = 1
    print(dict)

print(count("abcd"))
'''

print(int(1000**0.5))