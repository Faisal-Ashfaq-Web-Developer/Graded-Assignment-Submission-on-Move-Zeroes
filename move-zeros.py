# Problem statement
# you are given an array of integers. your task is to move all the zeros to the end of the array while maintaining the relative order of the other elements. The modified array should have zeros at the end, and the non-zero elements should retain their original order.


def move_zeros(arr):
    # Initialize pointers i and j to the beginning of the array
    i, j = 0, 0

    # Length of the array
    n = len(arr)

    # Iterate through the array using pointer i
    while i < n:
        # Check if the current element is non-zero
        if arr[i] != 0:
            # Swap the elements at i and j
            arr[i], arr[j] = arr[j], arr[i]
            # Increment j to point to the next position
            j += 1
        # Move to the next element
        i += 1

    return arr

# Example usage
arr = [0, 1, 0, 3, 12]
print("Original array:", arr)
print("Array after moving zeros:", move_zeros(arr))
