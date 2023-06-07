# Given a bitonic sequence A of N distinct elements, write a program to find a given element B in the bitonic sequence in O(logN) time.
#
# NOTE:
#
# A Bitonic Sequence is a sequence of numbers which is first strictly increasing then after a point strictly decreasing.
#
# Problem Constraints
# 3 <= N <= 105
#
# 1 <= A[i], B <= 108
#
# Given array always contain a bitonic point.
#
# Array A always contain distinct elements.

# Output Format
# Return a single integer denoting the position (0 index based) of the element B in the array A if B doesn't exist in A return -1.

# [1,2,3,10,20,17,15,13,4]

# Complexity - O(logn)

class BitonicArray():
    def __init__(self, arr, num):
        self.arr = arr
        self.num = num

    def searchLeftArray(self, start, end):

        while start <= end:
            mid = (start+end) // 2

            if self.arr[mid] == self.num:
                return mid
            elif self.num < self.arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return -1

    def searchRightArray(self, start, end):


        while start <= end:
            mid = (start + end) // 2

            if self.arr[mid] == self.num:
                return mid
            elif self.num < self.arr[mid]:
                start = mid + 1
            else:
                end = mid - 1
        return -1

    def findBitonicIndex(self, arr_size):
        left = 0
        right = arr_size - 1

        while left <= right:
            mid = (left + right)//2

            if self.arr[mid] > self.arr[mid+1] and self.arr[mid] > self.arr[mid-1]:
                return mid
            elif self.arr[mid] < self.arr[mid+1]:
                left = mid + 1
            else:
                right = mid - 1

    def searchNumber(self):
        """steps -> 1) Find Bitonic Number index
        2) Search in left part of Bitonic number
        3) Search in the right part of Bitonic number"""

        sizeOfArray = len(self.arr)

        bitonic_index = self.findBitonicIndex(sizeOfArray)

        if self.arr[bitonic_index] == self.num:
            return bitonic_index
        else:
            numberInLeftArray = self.searchLeftArray(0,bitonic_index - 1)
            if numberInLeftArray != -1:
                return numberInLeftArray
            else:
                return self.searchRightArray(bitonic_index + 1, sizeOfArray - 1)

arr1 = [1,2,3,10,20,17,15,13,4]
arr2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,40,39,38,37,36,35,34,33,32,31,30,29,28,27,26,25,24,23,22,21]
arr3 = [1,2,3,4,5,10,9,8,7,6]
ba = BitonicArray(arr3,5)
print(ba.searchNumber())