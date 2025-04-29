'''
s = str(input("Enter a string: "))

reversed_text = " "

for i in s:
    reversed_text = i + reversed_text 

print(reversed_text)
'''

'''Palindrome'''
'''
s = str(input("Enter a string: "))

is_palindrome = s == s[::-1]

print(is_palindrome)
'''

'''count vowels

s = "Programming"
vowels = "aeiouAEIOU"

vow_count = sum(1 for char in s if char in vowels)
others = sum(1 for char in s if char.isalpha() and char not in vowels)

print(vow_count, others)

'''

''' remove duplicates in string

s = "programming"
results = ""

for i in s:
    if i not in results:
        results += i

print(results)

'''
'''
arr = [1, 2, 2, 3, 4, 4, 5]

unique_arr = []

for i in arr:
    if i not in unique_arr:
        unique_arr.append(i)
print(unique_arr)

'''

'''
arr = [2, 4, 3, 5, 6, 7]
target = 9
pairs = []

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == target:
             pairs.append((arr[i], arr[j]))

print(pairs)
'''

'''

strings   = ["hello", "worlld", "shell", "holld"]

sub = "ll"

for i in strings:
    count = i.count(sub)
    print(count)
    '''
s = "The quick brown fox jumps over the lazy dog"
words = s.split()
print(words)
longest_word = max(words, key=len)
print(longest_word)
