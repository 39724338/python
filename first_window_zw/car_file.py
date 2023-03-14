class Car():   #创建一个类，类的名称为Car，通常按规范，类的名称首字母大写
    """ 汽车目前价值估计程序"""
    def __init__(self,make,model,year):   #当类Car被创建一个对象时，Python会自动运行该方法。
                                        # 下划线是一种约定，避免Python默认的方法与普通的方法名称冲突
                                        #self必不可少，且必须位于其他形参的前面。
        self.make = make   #可通过对象访问的变量称为属性
        self.model = model
        self.year = year
        self.this_year  = 2018
    def mod_this_year(self,new_year):
        self.this_year = new_year

    def detection(self):  #方法detection
        duration = self.this_year - self.year
        price  =  30 - 2 * duration
        long_name = "你的" + self.make + self.model + "到目前已经行驶了" + str(duration)\
                    +"年,"+"目前价值" +str(price)+ "万"
        return long_name

class ElectricCar(Car):     #父类须位于子类前面
    def __init__(self,make,model,year):
            # super函数将父类和子类关联起来。让python调用ElectricCar的父类的方法__init__()
        super().__init__(make,model,year)  #父类称为超类，super因此而得名。
    def battery(self,capacity):
        self.capacity_num = capacity
        print("您选择的电池容量为:",self.capacity_num,"kWh")
    def detection(self):  #重写父类
        duration = self.this_year - self.year
        price = 30 - duration - (500/self.capacity_num )
        long_name = "你的" + self.make + self.model + "到目前已经行驶了" + str(duration) \
                    + "年," + "目前价值" + str(price) + "万"
        return long_name

