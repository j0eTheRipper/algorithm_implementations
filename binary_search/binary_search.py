def search(arr, element):
    mid = (len(arr) - 1) // 2
    mid_element = arr[mid]

    while True:
        if mid_element == element:
            return mid
        elif mid_element > element:
            mid //= 2
            mid_element = arr[mid]
        elif mid_element < element:
            mid = (mid // 2) + mid
            mid_element = arr[mid]
