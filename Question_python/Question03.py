# Finding a Pair with a Given Sum in a Sorted Array (Opposite Direction)

def list_sum_pair(arr, target):
    right = len(arr) - 1 #five values then 4 concider
    left =  0

    while left < right:
        current_sum = left + right

        if current_sum == target:
            return (left, right)
        elif current_sum < target:
            left += 1
        else:
            right -= 1
        
    return None

print(list_sum_pair([1,2,3,4,5,6,7], 10))