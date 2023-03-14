##字符串格式化P13
##print("{}曰：学而时习之，不亦{}。".format("孔子","说乎"))



##字符串格式化P14
##print("{1}曰：学而时习之，不亦{0}。".format("孔子","说乎"))


##填充、对齐和宽度
##s = "等级考试"
##print("{0:*>25}Python语言".format(s))

##s = "等级考试"
##y = ''
##z = 25
##print("{0:*>25}Python语言".format(s,y,z))



##,.精度、类型主要用于对数值的规范

# print('{:,}'.format(1234567890))

# print("{:.2f}".format(12345.67890))
# print("{:.5}".format("Python是最近接人工智能的编程语言"))

# print("{0:b},{0:d},{0:o},{0:x},{0:X},{0:c}".format(425))
# print('{0:c}'.format(97))

# print("{0:e},{0:E},{0:f},{0:%}".format(3.14))
# print("{0:.2e},{0:.2E},{0:.2f},{0:.2%}".format(3.14))



# name = "Python语言" + "是最接近人工智能的编程语言"
# print(name)
#
# name = "Python语言！ " * 3
# print(name)
#
# name = "Python语言" + "是最接近人工智能的编程语言"
# print("语言fdaedef" in name)
#
# a = len("Python语言是最接近人工智能的编程语言")
# print(a)
# b = str(1000+10j)
# print(b,type(b))

#
# c = chr(97)
# print(c)
#
# d = ord('a')
# print(d)
#
# print(hex(10),type(hex(10)))
# print(oct(10))
# print(bin(20))


a = "Python"
# print(a.lower())
# print(a.upper())
# print(a.split('e'))
# print(a.split())
# print(a.count('e'))
# print(a.replace('e','P'))
# print(a.center(50,'#'))
# print(a.center(50))
# print(a.strip('+'))
# print(a.join('bcdefg'))
# print(a)




x = '3'    #x = 3 或 x = '3.1415926' 或x = '3'
print(type(x))
print(int(x),type(int(x)))
print(float(x),type(float(x)))
print(str(x),type(str(x)))