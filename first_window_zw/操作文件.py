import os


'''返回当前工作目录os.getcwd()'''
print(os.getcwd())


'''把目录和文件名合成一个路径,解决了不同系统，路径表示方式不同'''
# dir_new= os.path.join(os.getcwd(), 'nnnn','孙子文件夹')
# print(dir_new,type(dir_new))


'''创建新文件夹（目录）os.makedirs()类似mkdir命令'''
# dir_new = os.path.join('第一个文件', '子文件夹','孙子文件夹')
# print(dir_new)   #360  QQ
# os.makedirs(dir_new)


'''改变当前工作目录到指定的路径os.chdir(path)
    参数path -- 要切换到的新路径。'''
# dir_new = os.path.join(os.getcwd(), '第一个文件')
# print(dir_new)
# os.chdir(dir_new)
# print(os.getcwd())
# dir_new_1 = os.path.join(os.getcwd(), '第一个文件中的1')
# print(dir_new_1)
# os.makedirs(dir_new_1)

'''os.path() 模块：获取文件的属性
    1、关于路径获取
    .表示当前路径
    ..表示父目录
'''
# print(os.path.abspath('.')) #返回参数的绝对路径的字符串
# print(os.path.abspath('..'))
# print(os.path.abspath('./第一个文件'))
# print(os.path.abspath('../..'))
# print(os.path.abspath('../../..'))


'''判断相对路径和绝对路径os.path.isabs(path)
    如果参数是一个绝对路径，就返回 True，如果参数是
    一个相对路径，就返回 False
'''
# a=os.path.isabs('.')
# a=os.path.isabs('D:\PycharmProjects')
# print(a)

# '''一个路径到另一个路径的路线，
# 调用 os.path.relpath(path, start)将返回从 start 路径到 path 的相对路径的字符串。'''
# print(os.path.relpath('.',os.path.abspath('../venv/Lib')))

'''获取一个文件路径的文件名和路径名'''
# path = r'D:\PycharmProjects\untitled\课程源码\a.txt'
# file_name = os.path.basename(path)
# dir_name = os.path.dirname(path)
# file_dir_name = os.path.split(path)  #
# print(file_name)
# print(dir_name)
# print(file_dir_name)

'''os.path() 模块：获取文件的属性
    2、查看文件大小和文件夹内容'''
# path = r'D:\PycharmProjects\untitled\课程源码\正则表达式.py'
# print(os.path.getsize(path))  #查看文件大小单位字节
# print(os.listdir('..'))  #查看文件夹下所有文件，列表

'''小项目--检测当前文件夹中文件大小的总和'''
# file_total_size = 0
# for file_name in os.listdir('.'):
#     print(file_name)
#     # print(os.path.getsize('./'+file_name))
#     file_dir = os.path.join(os.getcwd(), file_name)
#     file_total_size += os.path.getsize(file_dir)
# print(file_total_size)

'''判断是文件还是文件夹
    os.path.exists(path)--判断path所指的文件或文件夹存在，存在则返回True，
                            否则返回 False。
    os.path.isfile(path)--如果path是否为一个文件，存在则返回True，
                            否则返回 False。
    os.path.isdir(path)--如果path是否为一个文件夹，存在则返回True，
                            否则返回 False。                      
'''
# path = r'D:\PycharmProjects\untitled\课程源码'
# print(os.path.exists(path))
# print(os.path.isfile(path))
# print(os.path.isdir(path))

'''小项目--检测当前文件夹中文件大小的总和'''
# file_total_size = 0
# file_total_size_child = 0
# for file_name in os.listdir('.'):
#     print(file_name)
#     # print(os.path.getsize('./'+file_name))
#     file_dir = os.path.join(os.getcwd(), file_name)
#     file_total_size += os.path.getsize(os.path.join(file_dir))
#     if os.path.isdir(file_dir):
#         for file_name_child in os.listdir(file_dir):
#             file_dir = os.path.join(os.getcwd(), file_name,file_name_child)
#             print(file_dir)
#             print(os.path.getsize(os.path.join(file_dir)))
#             file_total_size_child += os.path.getsize(os.path.join(file_dir))
# #
# print(file_total_size+file_total_size_child)
