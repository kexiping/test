#条件语句
'''
if
if ...else
if...elif ..else
if 条件:
    条件成立要执行的语句

if 条件:
    条件成立要执行的语句
else：



'''
# print(1)
# print(2)
# print(3)
# #4.5有条件打印
# result = input('请输入（y/n):')
# if result == 'y':
#     print(4)
#     print('over~~~~')
# print('~~~~~~~~~~~')

#随机数
import random
ran = random.randint(1, 10)
print(ran)
guess = input('请输入你猜测的数:')
if ran == int(guess):
    print('恭喜猜对了')
else:
    print('很遗憾，你猜错了')
