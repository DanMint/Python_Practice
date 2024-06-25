#Insertion sort
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i -1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key



#Selection sort
def selectionSort(arr):
    for i in range(0, len(arr)):
        min_value_index = i
        for j in range(i, len(arr)):
            if arr[min_value_index] > arr[j]:
                min_value_index = j
        
        temp = arr[min_value_index]
        arr[min_value_index] = arr[i]
        arr[i] = temp 


#Bubble sort
def bubbleSort(arr):
    for i in range(0, len(arr)):
        for j in range(1, len(arr) - i):
            if arr[j] > arr[j - 1]:
                continue

            temp = arr[j]
            arr[j] = arr[j - 1]
            arr[j - 1] = temp


#Merge sort
def mergeSort(arr, start, end):
    if start >= end:
        return
    
    middle = (start + end) // 2

    mergeSort(arr, start, middle)
    mergeSort(arr, middle + 1, end)
    merge(arr, start, middle, end)

def merge(arr, start, middle, end):
    n1 = middle - start + 1
    n2 = end - middle

    list1 = []
    list2 = []

    for i in range(0, n1):
        list1.append(arr[start + i])

    for i in range(0, n2):
        list2.append(arr[middle + 1 + i])

    list1.append(2147483647)  
    list2.append(2147483647) 

    i = 0
    j = 0

    for k in range(start, end + 1):  
        if list1[i] <= list2[j]:
            arr[k] = list1[i]
            i += 1
        else:
            arr[k] = list2[j]
            j += 1


#Heap sort
def max_heapify(arr, i, size):
    l = 2 * i + 1  
    r = 2 * i + 2  

    largest = i

    if l < size and arr[l] > arr[largest]:
        largest = l

    if r < size and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  
        max_heapify(arr, largest, size)

def build_max_heap(arr):
    size = len(arr)
    for i in range(size // 2 - 1, -1, -1):
        max_heapify(arr, i, size)

def heapSort(arr):
    size = len(arr)

    build_max_heap(arr)

    for i in range(size - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        size -= 1
        max_heapify(arr, 0, size)


#Quick sort

def partition(arr, start, end):
    x = arr[end]  
    i = start - 1

    for j in range(start, end):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1

def quickSort(arr, start, end):
    if start < end:
        q = partition(arr, start, end)
        quickSort(arr, start, q - 1)
        quickSort(arr, q + 1, end)


arr = [5, 6, 2, 3, 1, 10]
arr2 = [6, 5, 4, 3, 2, 1]
quickSort(arr, 0 , 5)
print(arr)