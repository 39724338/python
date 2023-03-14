'''selenium的介绍
1、 selenium是什么？  网页，web，不同的浏览器显示web
    用于Web应用程序测试的工具。可以驱动浏览器执行特定操作，自动按照脚本
    代码做出点击，输入，打开，验证等操作，就像真实用户所做的一样。
    支持的浏览器包括IE，Firefox，Safari，Chrome，Opera等。
2、selenium的工作原理
    浏览器具有webdriver驱动,这个驱动是根据不同的浏览器开发的，
    不同的浏览器使用不同的webdriver驱动程序且需要对应相应的浏览器版本，
    webdriver驱动程序可以通过浏览器内核控制浏览执行指定命令
3、如何使用selenium？
使用前准备： a、安装selenium库  b、驱动浏览器的内核驱动
a、安装selenium，使用pip install selenium -i https://pypi.mirrors.ustc.edu.cn/simple/
                或在pycharm中安装
b、chrome内核驱动地址    360浏览器使用的就是chrome的内核，QQ浏览器使用IE，IE，
https://chromedriver.storage.googleapis.com/index.html   首先确定你的浏览器是使用哪个内核？？
    windows系统：下载下来的文件解压后放置在python安装地址的Scripts中
    Linux和Mac系统：同上，注意：系统存在2个Python版本，确定当前运行的python
                    版本配置在环境变量中
'''

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys

# __browser_url = r"D:\Program Files (x86)\360Roaming\360se6\Application\360se.exe"  ##360浏览器的地址
# chrome_options = Options()
# chrome_options.binary_location = __browser_url    #

# driver = webdriver.Chrome(chrome_options=chrome_options)  #①
# driver.get('http://www.taobao.com')  #请求网页http://www.taobao.com
# driver.find_element_by_id("q").send_keys("Python" + Keys.RETURN)
# input_elemnt = driver.find_element_by_id('q')#当有多个标签时可能存在只能识别第一个标签信息
# input_elemnt = driver.find_element_by_xpath("//input[@id='q']")
# input_elemnt = driver.find_element_by_name('q')
# input_elemnt.send_keys("Python" + Keys.RETURN)  #②

'''①
webdriver具备多种不同浏览器的驱动，
browser = webdriver.Chrome()
browser = webdriver.Firefox()
browser = webdriver.Edge()
browser = webdriver.PhantomJS()
browser= webdriver.Safari()
其中.chrome.webdriver import WebDriver as Chrome定义了别名，Chrome代表WebDriver
'''

'''②
WebElement类：通常与文档交互的所有有趣的操作都将通过此接口执行。
WebElement.send_keys:模拟在元素中键入信息
    参数：send_keys用于键入或设置表单字段的字符串。
            对于设置文件输入，这可以是本地文件路径。
'''
'''上传图片'''
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys
#
# __browser_url = r"D:\Program Files (x86)\360Roaming\360se6\Application\360se.exe"  ##360浏览器的地址
# chrome_options = Options()
# chrome_options.binary_location = __browser_url    #
#
# driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.get('https://graph.baidu.com/pcpage/index?tpl_from=pc')  #请求网页http://www.taobao.com
# input_element = driver.find_element_by_xpath('//input[@name="file"]')
# input_element.send_keys(r"C:\Users\Administrator\Desktop\timg.jpg")


'''爬取标签：爬虫的本质目的是为了获取网页指定信息'''
'''获取淘宝首页中所有主题市场的名称'''
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# __browser_url = r"D:\Program Files (x86)\360Roaming\360se6\Application\360se.exe"  ##360浏览器的地址
# chrome_options = Options()
# chrome_options.binary_location = __browser_url
#
# driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.get('http://www.taobao.com')  #请求网页http://www.taobao.com
# elments = driver.find_elements_by_xpath("//li[contains(@role,'menuitem')]/a") #elements是获取所有标签
# for elment in elments:
#     print(elment.text,elment.get_attribute('href'),elment.location,\
#             elment.tag_name,elment.size)
# #elment.text:获取标签的文本
# #elment.get_attribute：获取标签的属性值
# #elment.location:获取标签的位置
# #elment.tag_name：获取标签名字
# #elment.size:获取标签的大小



'''模拟点击click方法'''
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys
#
# __browser_url = r"D:\Program Files (x86)\360Roaming\360se6\Application\360se.exe"  ##360浏览器的地址
# chrome_options = Options()
# chrome_options.binary_location = __browser_url
#
# driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.get('http://www.taobao.com')  #请求网页http://www.taobao.com
# elments = driver.find_elements_by_xpath("//li[contains(@role,'menuitem')]/a") #elements是获取所有标签
# elments[10].click()


'''切换到子框架'''
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.action_chains import ActionChains
#
# __browser_url = r"D:\Program Files (x86)\360Roaming\360se6\Application\360se.exe"  ##360浏览器的地址
# chrome_options = Options()
# chrome_options.binary_location = __browser_url
#
# driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.get('http://www.taobao.com')  #请求网页http://www.taobao.com
# elments = driver.find_elements_by_xpath("//li[contains(@role,'menuitem')]") #elements是获取所有标签
# ActionChains(driver).move_to_element(elments[2]).perform()
# chil_elments = driver.find_elements_by_xpath('//*')
# for elment in chil_elments:
#     print(elment)







'''前进后退刷新'''
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import time
# __browser_url = r"D:\Program Files (x86)\360Roaming\360se6\Application\360se.exe"  ##360浏览器的地址
# chrome_options = Options()
# chrome_options.binary_location = __browser_url
#
# driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.get('http://www.taobao.com')  #请求网页http://www.taobao.com
# driver.get('http://www.baidu.com')
# driver.get('http://www.qq.com')
# driver.back()  #网页返回到上一步
# time.sleep(5)  #
# driver.forward() #
# time.sleep(5)
# driver.refresh()  #刷新
# driver.quit()#关闭浏览器
# driver.close() #关闭当前窗口


'''cookies'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# __browser_url = r"D:\Program Files (x86)\360Roaming\360se6\Application\360se.exe"  ##360浏览器的地址
# chrome_options = Options()
# chrome_options.binary_location = __browser_url
#
# driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.get('http://www.taobao.com')  #请求网页http://www.taobao.com
# print(driver.get_cookies())
# driver.add_cookie({'name': 'zhangsan', 'value' : '98'})
# print(driver.get_cookies())


'''项目实现：苏宁易购网站获取医用口罩信息（包含价格、名称、评价数、店铺名称）'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

__browser_url = r"D:\Program Files (x86)\360Roaming\360se6\Application\360se.exe"  ##360浏览器的地址
chrome_options = Options()
# chrome_options.add_argument('--headless') #360不支持无界面模式，但是如果你用的是
                #chrome浏览器，那是支持的。
chrome_options.binary_location = __browser_url

driver = webdriver.Chrome(chrome_options = chrome_options)
driver.get('http://www.suning.com')  #请求网页http://www.taobao.com
element = driver.find_element_by_xpath("//div/input[@tabindex='0']")
element.send_keys("医用口罩" + Keys.RETURN)
time.sleep(20)
driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
time.sleep(20)
price_elements = driver.find_elements_by_xpath('//span[@class="def-price"]')
title_elements = driver.find_elements_by_xpath('//div[@class="title-selling-point"]')
evaluate_elements = driver.find_elements_by_xpath('//div[@class="info-evaluate"]')
store_elements = driver.find_elements_by_xpath('//div[@class="store-stock"]')
f = open('医用口罩.txt','w',encoding='utf-8')
for i in range(len(price_elements)):
    f.write(price_elements[i].text + '\t')
    f.write(title_elements[i].text + '\t')
    f.write(evaluate_elements[i].text + '\t')
    f.write(store_elements[i].text + '\n')
f.close()

'''chrome支持无界面模式


'''
