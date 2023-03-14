def fun_bmi(person, height, weight):
    print(person + "的身高：" + str(height) + "米 \t 体重：" + str(weight) + "千克")
    bmi = weight / (height * height)  # 用于计算BMI指数，公式为：BMI=体重/身高的平方
    print(person + "的BMI指数为：" + str(bmi))  # 输出BMI指数
    # 判断身材是否合理
    if bmi < 18.5:
        print("您的体重过轻 ~@_@~\n")
    if bmi >= 18.5 and bmi < 24.9:
        print("正常范围，注意保持 (-_-)\n")
    if bmi >= 24.9 and bmi < 29.9:
        print("您的体重过重 ~@_@~\n")
    if bmi >= 29.9:
        print("肥胖 ^@_@^\n")

# *****************************调用函数*********************************** #
fun_bmi("路人甲", 1.83, 60)  # 计算路人甲的BMI指数
fun_bmi("路人乙", 1.60, 50)  # 计算路人乙的BMI指数 
