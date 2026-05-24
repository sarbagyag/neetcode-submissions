class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        p=0
        q=len(matrix)-1
        n=len(matrix[0])-1

        while(p<=q):
            k=(p+q)//2

            if (matrix[k][0]<=target and matrix[k][n]>=target):
                if(matrix[k][0]==target or matrix[k][n]==target):
                    return True

                l=0
                r=n

                while(l<=r):
                    m=(l+r)//2
                    if matrix[k][m]==target:
                        return True
                    elif matrix[k][m]>target:
                        r=m-1
                    else:
                        l=m+1
                return False
            
            elif(matrix[k][0]<target and matrix[k][n]<target):
                p=k+1
            
            else:
                q=k-1
        
        return False
        