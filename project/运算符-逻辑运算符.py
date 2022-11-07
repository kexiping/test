'''
逻辑运算符：
and or not
结果：
and: 与，并且
A and B
ture and true --->true
ture and False --->False
False and true --->Fasle
False and False --->Fasle

or 或
A or B  只要有一侧为true,结果即为:true
ture and true --->true
ture and False --->true
False and true --->true
False and False --->Fasle

not True --->False
not False --->True
'''


a = 1
b = 3
print(a and b) #and两边非0,结果是最后的数字值
c = 0
print(c and a) # and两边只要有一边为0，结果即为0
print(a > c and a < b)
print(a ==c  and a < b)

print('*_* ' * 20)
print(b or a)
print(a or b)
print(c or a)
print(c or b)

flag = True
print(not flag)