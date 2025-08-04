import random

def quicksort(arr):
    def sort(left, right):
        if left >= right:
            return
        
        i = left
        for j in range(left, right):
            if arr[j] < arr[right]:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[right] = arr[right], arr[i]
        sort(left, i-1)
        sort(i+1, right)

    sort(0, len(arr)-1)

if __name__ == "__main__":
    arr = [i for i in range(10)]
    random.shuffle(arr)
    print(f"Randomly generated array: {arr}")
    quicksort(arr)
    print(f"Array sorted with Quicksort: {arr}")