# python3

def shiftDown(i, arr, b, a):
    while (i <= (len(arr) - 1)//2 ):
        print("2:",i)
        if 2*i+2 <= len(arr)-1:
            print("3:", i)
            if arr[i] > arr[2*i+1] or arr[i] > arr[2*i+2]:
                if arr[2*i+2] > arr[2*i+1]:
                    arr[i], arr[2*i+1] = arr[2*i+1], arr[i]
                    i = 2*i + 1
                    b = i
                    print("4: ", i)
                    
                else:
                    arr[i], arr[2*i+2] = arr[2*i+2], arr[i]
                    i = 2*i + 2
                    b = i
                    print("5: ", i)

            else:
                return
        
        elif 2*i+1 <= len(arr) - 1:
            if arr[i] > arr[2*i+1]:
                    arr[i], arr[2*i+1] = arr[2*i+1], arr[i]
                    i = 2*i + 1
                    b = i
                    print("6: ", i)
            
            else:
                return
        
        else:
            return

    if b != -1:
        print(a,b)
        swaps.append([a,b])

def buildHeap(arr):
    swaps = []
    n = len(arr)-1
    for i in range(n//2):
        print("1")
        a = n//2 - i
        b = -1
        shiftDown(n//2 - i, arr, b, a)
    
    print(arr)
    return swaps


def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                swaps.append((i, j))
                data[i], data[j] = data[j], data[i]
    return swaps




def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = buildHeap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
