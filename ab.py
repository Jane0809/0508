 '''
 def swap(a,b)
     a=a^b
     b=b^a
     a=a^b
     return (a,b)
'''
 a=18
 b=14
 
 while (a!=0 and b!=0):
     if a > b:
         a = a - b
     elif b >= a:
         b = b - a
         
 if a!=0:
     print(a)
 if b!=0:
     print(b)