# Problem Description
# # Given an integer A.Compute and return the square root of A. If A is not a perfect square, return floor(sqrt(A)).
# # DO NOT USE SQRT FUNCTION FROM STANDARD LIBRARY.
# # NOTE: Do not use sort function from standard library. Users are expected to solve this in O(log(A)) time.
# #
# # Problem Constraints
# # 0 <= A <= INTMAX
# #
# #
# # Output Format
# # Return floor(sqrt(A))
# #
# # Example Input
# # I/p - 11
# # Output = 3

class SqrtofInteger:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        start = 0
        end = A
        ans = -1

        while start <= end:
            mid = (start + end) // 2

            mid_square = mid * mid

            if mid_square == A:
                return mid
            elif mid_square < A:
                ans = mid
                start = mid + 1
            else:
                # ans = mid  # updating ans here is redundant
                end = mid - 1 # test with updating the ans=mid here also

        return ans # or return start-1

number = 100
sqrtCls = SqrtofInteger()
print(sqrtCls.sqrt(number))

