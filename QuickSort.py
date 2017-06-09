def quickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)


def quickSortHelper(alist, first, last):
    if first < last:
        splitPoint = partition(alist, first, last)

        quickSortHelper(alist, first, splitPoint - 1)
        quickSortHelper(alist, splitPoint + 1, last)


def partition(alist, first, last):
    pivotvlue = alist[first]

    leftmark = first + 1
    rightmark = last
    done = False

    while not done:
        while alist[leftmark] <= pivotvlue and leftmark <= rightmark:
            leftmark += 1
        while alist[rightmark] >= pivotvlue and rightmark >= leftmark:
            rightmark -= 1

        if leftmark > rightmark:
            done = True
        else:
            alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]
    alist[rightmark], alist[first] = alist[first], alist[rightmark]
    return rightmark


def qsort(lists, low, high):
    print('this', lists[low:high + 1])
    left = low
    right = high
    pivot = low
    while high > low:
        while lists[high] >= lists[pivot] and high > low:
            high -= 1
        while lists[low] <= lists[pivot] and high > low:
            low += 1
        lists[high], lists[low] = lists[low], lists[high]
        print('swape', lists, high, low)
        high -= 1
        low += 1
    pivot = low - 1
    lists[left], lists[pivot] = lists[pivot], lists[left]
    print('parted', lists, 'left', left, 'pivot', pivot)
    if pivot > left + 1:
        qsort(lists, left, pivot - 1)
    if pivot < right - 1:
        qsort(lists, pivot + 1, right)
    return lists


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
alist2 = [1]
print(alist2)
quickSort(alist2)
print(alist2)
print(alist)
quickSort(alist)
print(alist)
