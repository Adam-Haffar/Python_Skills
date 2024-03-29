def mergesort(numberlist):
    if len(numberlist) < 2:
        return numberlist

    middle = int(len(numberlist) / 2)
    lefthalf = mergesort(numberlist[:middle])
    righthalf = mergesort(numberlist[middle:])

    return merge(lefthalf, righthalf)


def merge(lefthalf, righthalf):

    left = 0
    right = 0
    sortedlist = []
    leftlength = len(lefthalf)
    rightlength = len(righthalf)

    for _ in range(leftlength + rightlength):

        if left < leftlength and right < rightlength:
            if lefthalf[left] <= righthalf[right]:
                sortedlist.append(lefthalf[left])
                left += 1
            else:
                sortedlist.append(righthalf[right])
                right += 1
        elif left == leftlength:
            sortedlist.append(righthalf[right])
            right += 1
        elif right == rightlength:
            sortedlist.append(lefthalf[left])
            left += 1

    return sortedlist


def main():
    mynumbers = [23, 30, 91, 21, 88, 45, 9, 72, 186, 5]
    print("Unsorted List: " + str(mynumbers))
    mynumbers = mergesort(mynumbers)
    print("Sorted List: " + str(mynumbers))


main()
