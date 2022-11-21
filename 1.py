class Solution:
   def solve(self, n):
      sign = '-' if n<0 else ''
      n = abs(n)
      if n < 3:
         return str(n)
      s = ''
      while n != 0:
         s = str(n%3) + s
         n = n//3
      return sign+s
m=int(input())
ob = Solution()
print(ob.solve(m))