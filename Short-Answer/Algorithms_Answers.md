#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
    O(log n)


b)
    O(n log n)


c)
    O(n!) (This psuedocode will inifitely loop)

## Exercise II


For this exercise (n-story building with eggs to drop) I would use Binary Search, with a complexity of **O(log n)**

```python
def safe_egg_floor(floors, f):
    if not floors:
        return -1 # not found
    low = 0 # intitializing our range at the first floor,
    high = len(floors) -1 # and the top floor
    while low <= high:
        mid - (low + high) // 2 # this is the middle floor
        if floors[mid] == target:
            return mid
        if floors[mid] < target:
            low = mid + 1
            continue
        high = mid
    return -1 # not found

```