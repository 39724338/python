grade=int(input("请输入成绩："))
if grade>=90 and grade<=100:
    print("成绩是:",grade,",优秀")
elif grade>=70 and grade<=89:
    print("成绩是:",grade,",良好")
elif grade>=60 and grade<=69:
    print("成绩是:",grade,",及格")
else:
    print("成绩是:",grade,",不及格")
