
def longest_substring(str):
    string = str.split()
    max = 0
    longest_str = ' '

    for i in string:
        if len(i) > max:
            max = len(i)
            longest_str = i
    return longest_str

print(longest_substring('Suganesh oru lusu'))
