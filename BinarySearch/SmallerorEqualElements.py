# Problem Description
# Given an sorted array A of size N. Find number of elements which are less than or equal to B.
# NOTE: Expected Time Complexity O(log N)
#
# Problem Constraints
# 1 <= N <= 106
#
# 1 <= A[i], B <= 109

# Output Format
# Return an integer denoting the number of elements which are less than or equal to B.

class SmallorEqual:
    # @param A : list of integers
    # @param B : integer
    # @return an integer

    """My Solution -> Complexity O(logn), in special case can be O(n)"""
    def solve(self, A, B):
        start = 0
        end = len(A) - 1
        numbers = 0

        while start <= end:
            mid = (start + end) // 2
            if A[mid] == B:
                numbers += len(A[0:mid + 1])
                if B in A[mid + 1:]:
                    countB = A[mid + 1:].count(B)
                    numbers += countB
                return numbers
            elif B <= A[mid]:
                end = mid - 1
            else:
                start = mid + 1

        numbers += len(A[0:end+1])
        return numbers  # or just return end+1 instead of above two lines

    def solveImproved(self, A, B):
        """ Will always be O(logn)"""
        start = 0
        end = len(A) - 1
        # numbers_count = 0

        while start < end:
            mid = (start+end)//2
            if B < A[mid]:
                end = mid
            else:
                start = mid + 1
        return end


arr1 = [1,2,3,4,4,5,6]
se = SmallorEqual()

print(se.solveImproved(arr1,4))
print(se.solve(arr1,4))




