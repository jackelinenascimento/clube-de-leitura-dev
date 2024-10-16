def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        print("left:", left)
        middle = [x for x in arr if x == pivot]
        print("middle:", middle)
        right = [x for x in arr if x > pivot]
        print("right:", right)
        return quicksort(left) + middle + quicksort(right)

# Exemplo de uso
if __name__ == "__main__":
    arr = [3, 6, 8, 10, 1, 2, 1]
    print("Array original:", arr)
    sorted_arr = quicksort(arr)
    print("Array ordenado:", sorted_arr)