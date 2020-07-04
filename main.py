import collections
import numpy














"""งง///////////////////                                            ////////////////////// """

""" i=6
while(i>0):
    j=6
    while(j>i):
        print("*",end=' ')
        j-=1
    i-=1
    print()
 """


""" for i in range(1,6):
    for j in range(i):
        print('*', end='')
    print()
 """






""" listed = []

for i in 'anxiety':
    listed.append(i)

print(listed)
 """








"""/////Sorted Number//////"""
""" sort = [3,2,4,15,25,1]
Sorting = sorted(sort)

print(Sorting)

 """




"""///////////////////////Even Number In Range//////////////////////"""
""" even = [i*2 for i in range(1,11)]
print(even) """



"""List"""
""" list = ['first','second','third']

print(list[:3])
 """






"""////////////////OrderedDict/////////////////"""

""" d = collections.OrderedDict()

d[1] = 'e'
d[2] = 's'
d[3] = 't'
d[4] = 'd'
d[5] = 'a'
d[6] = '1'


print(d.keys())
print(d.items())

 """



"""/////////////////////Switcher//////////////////////"""

""" class switcher(object):
    def direct(self, i):
        method_name = 'Number_'+ str(i)
        method = getattr(self, method_name,lambda : 'Invalid')
        return method()
    def Number_1(self):
        return '1'
    def Number_2(self):
        return '2'
s = switcher()
a = s.direct(1)

print(a)
 """
""" x = lambda a,b,c : a + b + c

print(x(1,2,3)) """



""" def week(i):
    switcher={
        0:'Sunday',
        1:'Monday',
        2:'Tuesday',
        3:'Wednesday',
        4:'Thursday',
        5:'Friday',
        6:'Saturday'
    }
    return switcher.get(i, "valid day of the week")
    


WeekPrint = week(2)
print(WeekPrint) """
""" 
i = int(input("Enter a number "))

if i % 2 == 0:
    print("even")
else:
    print("odd") """