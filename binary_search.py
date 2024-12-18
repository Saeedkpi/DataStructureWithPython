def binary_search(L, x):
    left, right = 0, len(L)-1

    while left <= right:
        mid = (left + right) // 2 # For Integer division

        if L[mid] == x:
            return mid # Find the search value
        if L[mid] < x:
            left = mid + 1
        if L[mid] > x:
            right = mid - 1
    
    return -1

if __name__ == "__main__":
    my_list = [1, 2, 3, 5, 7, 9, 10, 12, 15, 20]

    for x in range(1, len(my_list)):
        position = binary_search(my_list, x)

        if position == -1:
            if x in my_list:
                print(x, "is in List, but function returned -1")
            else:
                print(x, "not in List")
        else:
            if my_list[position] == x:
                print(x, "Found in correct position.")
            else:
                print("Binary search returned", position, "for", x, "which is incorrect")
    print("Program terminated")