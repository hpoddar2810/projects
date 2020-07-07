# python3
global arr

def siftDown(i):
    global arr
    n = len(arr) - 1 
    k = i
    l = 2*i + 1
    if l <= n and arr[l] < arr[i]:
        k = l
    
    r = 2*i + 2
    if r <= n and arr[r] < arr[i]:
        k = r

    if k != i:
        arr[i], arr[k] = arr[k], arr[i]
        return siftDown(k)
    
    else: return i
        

def buildHeap(arr):
    #arr = li
    swaps = []
    n = len(arr) - 1

    for i in range(n//2, -1, -1):
        print(i)
        print(arr)
        j = siftDown(i)
        print(j)
        print(arr)

        if j != i:
            swaps.append((i,j))
    
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
