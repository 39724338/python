print("\n手机店正在打折，活动进行中……")                           # 输出提示信息
strWeek = input("请输入中文星期（如星期一）：")                     # 输入星期，例如，星期一
intTime = int(input("请输入时间中的小时（范围：0~23）："))          # 输入时间
# 判断是否满足活动参与条件（使用了if条件语句)
if (strWeek == "星期二" and  (intTime >= 10 and intTime <= 11)) or (strWeek == "星期五" 
and (intTime >= 14 and intTime <= 15)):
    print("恭喜您，获得了折扣活动参与资格，快快选购吧！")           # 输出提示信息
else:
    print("对不起，您来晚一步，期待下次活动……")                   # 输出提示信息
