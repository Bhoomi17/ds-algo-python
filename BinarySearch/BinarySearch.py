# Complexity O(logn); input size getting divided by 2 in each iteration,

class BinarySearch():
    def __init__(self, arr, num):
        self.arr = arr
        self.num = num

    def searchNumber(self):
        sizeofArr = len(self.arr)
        start = 0
        end = sizeofArr - 1

        while start <= end:
            mid = (start + end)//2

            if self.num == self.arr[mid]:
                return mid
            elif self.num < self.arr[mid]:
                end = mid - 1
            else:
                start = mid + 1

        return -1


number_list = [1,2,3,5,9,33,46,47,49]
#find if number 47 is present an dreturn index

# bs = BinarySearch(number_list,47)
bs = BinarySearch(number_list,4)
isPresentAt = bs.searchNumber()
print(isPresentAt)
