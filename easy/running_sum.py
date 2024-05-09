
input_arr = [3,4,58,90,81,97]

def running_sum(arr:list):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
        arr[i] = sum
    return arr


if __name__ == "__main__":
    print(running_sum(input_arr))