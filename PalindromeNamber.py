# class Solution(object):
#     def isPalindrome(self, x):
#         s=str(x)
#         rev=s[::-1]
#         l=len(s)
#         counter=0
#         for _ in range(0,l):
#                 if s[_]==rev[_]:
#                         counter+=1
#                 else:
#                         return False
#         if counter==l:
 
#                 return True

def x(c):
    oo=str(c)
    rev=oo[::-1]


    return oo==rev 
dd=x(13341)
print(dd)