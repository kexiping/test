'''
数据类型：
int
float
string
boolean

'''
money = 28  # 声明一个叫money的变量，赋值为28
type(money)
print(type(money)) #print()属于一个内置函数，负责输出结果

money = 28.9
print(type(money))
#通过type（变量名）输出变量类型
money = 0.98282
print(money)
print(type(money))

money = '一万'
print(money)
print(type(money))

money = '10000'
print(money)

print(type(money))

message = '世龙说：''你够狠今天吃得挺饱！'''
print(message)

#保留格式输出
shi = '''
            静夜思
            唐  李白
       窗前明月光，疑是地上霜  
       举头望明月，低头思故乡 
'''
print(shi)

#布尔类型 True or False
#主要用于开发中的判断。比如：是否登录成功，
isLogin = True
print(isLogin)

isLogin = False
print(type(isLogin))