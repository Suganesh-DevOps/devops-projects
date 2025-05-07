
def add_up_to_target(lists, target):

    for i in range(len(lists)):
        for j in range(i+1, len(lists)):
            if lists[i] + lists[j] == target:
                print(f"{lists[i]} and {lists[j]} will add up to {target}")
                
ls = [1, 2, 3, 5, 6, 3, 4]
add_up_to_target(ls, 9)
                 
