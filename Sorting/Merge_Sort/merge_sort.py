def sort(arr):
    if len(arr) < 2:
        return
    mid_index = len(arr)//2
    left_arr = arr[:mid_index]
    right_arr = arr[mid_index:]
    sort(left_arr)
    sort(right_arr)
    merge(left_arr, right_arr, arr)


def merge(left_arr, right_arr, result):
    i, j, k = 0, 0, 0
    while(i < len(left_arr) and j < len(right_arr)):
        if left_arr[i] < right_arr[j]:
            result[k] = left_arr[i]
            i += 1
        else:
            result[k] = right_arr[j]
            j += 1
        k += 1

    if i < len(left_arr):
        result[k:] = left_arr[i:]

    if j < len(right_arr):
        result[k:] = right_arr[j:]


def merge_sort(arr):
    sort(arr)
    return arr


if __name__ == "__main__":
    arr = [1, 3, 2, 1, 4, 5, 8, 3, 9]
    print(merge_sort(arr))
