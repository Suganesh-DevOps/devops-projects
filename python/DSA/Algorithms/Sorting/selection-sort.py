#Repeatedly finds the smallest element and places it at the beginning.
#	T--> O(n²)	S->O(1)
# in-place sorting


def selection_sort(arr):
  n = len(arr)
  for i in range(n):
    mini = i
    for j in range(1, n):
      if arr[j] < arr[mini]:
            mini = j
    arr[i], arr[mini] = arr[mini], arr[i]
  return arr
  


def score_board(score):
    
    n = len(score)

    for i in range(n):
        mini =  i
        for j in range(i+1, n):
            if score[j] < score[mini]:
                mini = j
        score[i], score[mini] = score[mini], score[i]
    
    print(f"Sorted Scores: {score}")
    print(f"Highest Score: {score[-1]}")
    print(f"Second Highest Score: {score[-2]}")
    print(f"Lowest Score: {score[0]}")

scores = [55, 89, 76, 45, 92, 67, 38]
score_board(scores)
