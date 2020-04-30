def insertion_sort(array):
    """An implementation of the insertion sort algorithm."""
    for k in range(1, len(array)):
        cur = array[k]
        j = k
        while j > 0 and array[j-1] > cur:
            array[j] = array[j-1]
            j -= 1
        array[j] = cur


if __name__ == "__main__":
    array = [4,6,8,9,4,3,6,5,8,7,1,2,3,23,45,11]
    print(array)
    insertion_sort(array)
    print(array)
