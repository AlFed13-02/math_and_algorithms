
def merge_sort(A, p, r):
    """Implements the merge sort algorithm."""
    
    if p == r:
        return 
    elif p < r:
        q = (p+r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)

        first_part =A[p:q+1]
        second_part = A[q+1:r+1]
        first_part_index = 0
        second_part_index = 0
        insert_index = p

        while (first_part_index < len(first_part)
               and second_part_index < len(second_part)):
            if first_part[first_part_index] <= second_part[second_part_index]:
                A[insert_index] = first_part[first_part_index]
                first_part_index += 1
            else:
                A[insert_index] = second_part[second_part_index]
                second_part_index += 1
            insert_index += 1

        if first_part_index >= len(first_part):
            leftover = second_part[second_part_index:]
        else:
            leftover = first_part[first_part_index:]

        A[insert_index: r+1] = leftover
            

        

        
if __name__ == "__main__":
    A = [1, 4, 23, 2, 3, 21, 17, 15, 25]
    A = [1, 5, 3, 2, 4]
    merge_sort(A, 0, len(A)-1)
