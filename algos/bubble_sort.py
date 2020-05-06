def bubble_sort(data):
    """An implementation of the bubble sort algorithm."""
    for pass_ in range(len(data) - 1):
        for cur in range(len(data) - pass_ -1):
            if data[cur] > data[cur + 1]:
                data[cur], data[cur + 1] = data[cur + 1], data[cur]


if __name__ == "__main__":
    data = [9,8,7,6,5,4,3,2,1,0]
    bubble_sort(data)
    print(data)
        
