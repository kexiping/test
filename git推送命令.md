- [1.拉取与推送](#1拉取与推送)
- [2.如何同步更新本地代码与GitHub代码](#2如何同步更新本地代码与github代码)
  - [2.1.将在GitHub上更改的内容更新到本地](#21将在github上更改的内容更新到本地)
  - [2.2.将在本地更新后的代码上传到GitHub](#22将在本地更新后的代码上传到github)
# 1.拉取与推送
把GitHub上面的文件拉取下来

git pull origin main -allow-unrelated-histories

本地强制推送

git push -u origin main -f

# 2.如何同步更新本地代码与GitHub代码

## 2.1.将在GitHub上更改的内容更新到本地
1、在GitHub上修改完后记得保存

2、进入你本地建立的文件夹，右键git bash here

3、输入pwd确认位置后，输入git pull origin

4、查看本地是否更新成功
## 2.2.将在本地更新后的代码上传到GitHub

1、更改本地文件

2、在本地文件夹下右键git bash here，

3、输入pwd确认位置

4、输入git add .

5、输入git commit -m ‘update’

6、输入git push

7、打开GitHub查看是否成功