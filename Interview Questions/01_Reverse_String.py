class Solution:
    def reverseString(self, arr: str) -> None:
        arr = list(arr)
        i = 0
        j = len(arr)-1
        
        while(i<j):
            arr[i],arr[j] = arr[j],arr[i]
            i+=1
            j-=1
        return arr

s = Solution()
s.reverseString("Hello")