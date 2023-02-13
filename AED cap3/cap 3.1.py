def bubbleSort(self):

    for last in range(self.__nItems-1, 0, -1):
        for inner in range(last):

            if self.__a[inner] > self.__[inner+1]:

                self.swap(inner, inner+1)

def bidirectional_bubble_sort(arr):
    n = len(arr)
    left = 0
    right = n - 1
    
    while left <= right:
        for i in range(left, right):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        right -= 1
        
        for i in range(right, left, -1):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
        left += 1
    
    return arr