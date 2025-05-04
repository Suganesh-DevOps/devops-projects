----- Easy approch----
from collections import Counter

def ana(str1, str2):
    return Counter(str1) == Counter(str2)

print(ana("suu", "sugu"))      # False
print(ana("listen", "silent"))  # True

-----my approach---
# check anagaram
def ana(str1, str2):
    char_count = {}
    for char in str1:
        if char in char_count:
            char_count[char] += 1
        else:
             char_count[char] = 1
    
    char_count_1 = {}
    for char1 in str2:
        if char1 in char_count_1:
            char_count_1[char1] += 1
        else:
             char_count_1[char1] = 1


  
    return char_count == char_count_1
-----------
