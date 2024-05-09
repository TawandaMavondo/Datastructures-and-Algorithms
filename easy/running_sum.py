
input_arr = [3,4,58,90,81,97]

def running_sum(arr:list):
    # Initialize sum to 0
    sum = 0
    # Iterate through the array and add the current element to the sum
    for i in range(len(arr)):
        # Add the current element to the sum
        sum += arr[i]
        # Update the current element with the sum
        arr[i] = sum
        # Repeat the process for the next element
    return arr


if __name__ == "__main__":
    print(running_sum(input_arr))

# Time Complexity: O(n)
# Space Complexity: O(1)