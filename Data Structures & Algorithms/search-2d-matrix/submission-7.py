import bisect

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m: int = len(matrix)
        n: int = len(matrix[0]) 
        l: int = 0
        r: int = m-1
        row_no = 0
        while l<=r:
            print(f"l :{l}, r: {r}, row_no: {row_no}")
            mid: int = (l+r)//2
            if matrix[mid][0] < target:
                l = mid+1
                row_no = mid
            elif matrix[mid][0] > target:
                r = mid-1
                row_no = mid-1
            else:
                return True
        
        
        index = bisect.bisect_left(matrix[row_no], target)
        print(index)
        if index<n  and matrix[row_no][index] == target :
            return True
        else:
            return False
