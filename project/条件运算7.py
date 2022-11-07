money = 500000
if 10000 < money <= 50000:
    print('奖励10000元，恭喜！')
elif 50000 < money <= 100000:
    print('奖励笔记本IBM！恭喜！')
elif 100000 < money <= 1000000:
    print('奖励iphone12！恭喜！')
elif money > 1000000:
    print('奖励一部特斯拉！恭喜')
else:
    print('鼓励奖，毛绒玩具')

'''
人员管理系统，功能：添加员工，删除员工，查询员工 修改员工信息
'''
print('---------欢迎进入人员管理系统--------')
choice = input('请选择功能：\n1.添加员工\n2.删除员工\n3.查询员工\n4.修改员工信息\n')
#将choice逐个比较
if choice == '1':
    print('添加员工')
elif choice == '2':
    print('删除员工')
elif choice == '3':
    print('查询员工')
elif choice == '4':
    print('修改员工信息')


