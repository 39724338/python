'''
  PDFminer   命令 解析pdf 如何？
pdf2txt.py [-P password] [-o output] [-t text|html|xml|tag]
             [-O output_dir] [-c encoding] [-s scale] [-R rotation]
             [-Y normal|loose|exact] [-p pagenos] [-m maxpages]
             [-S] [-C] [-n] [-A] [-V]
             [-M char_margin] [-L line_margin] [-W word_margin]
             [-F boxes_flow] [-d]
             input.pdf ...
  先准备一个pdf
-P password ：PDF密码。
-o output ：输出文件名，也可以转换为html格式
-t text|html|xml|tag：输出类型。（默认值：从输出文件名自动推断。）
-O output_dir ：提取图像的输出目录。
-c encoding：输出编码。（默认值：utf-8）
-s scale ：输出比例。
-R rotation ：以度为单位旋转页面。
-Y normal|loose|exact：指定布局模式。（仅用于HTML输出。）
-p pagenos ：仅处理某些页面。
-m maxpages ：限制要处理的最大页面数。
-S ：去除控制字符。
-C ：禁用资源缓存。
-n ：禁用布局分析。
-A ：对包括文本在内的所有文本应用布局分析。
-V ：自动检测垂直书写。
-M char_margin ：指定char边距。
-W word_margin ：修饰单词margin。
-L line_margin ：专门说明行边距。
-F boxes_flow ：具体说明箱式流量比。
-d ：打开调试输出。
'''
'''
1、 python pdf2txt.py -o a.txt 富有之谓大业.pdf
    使用pdf2txt.py将富有之谓大业.pdf 转换为文本a.txt中
    
2、 python pdf2txt.py 富有之谓大业.pdf
    使用pdf2txt.py将富有之谓大业.pdf 转换为文本直接输出到屏幕中
    
3、 python pdf2txt.py -o a.html 富有之谓大业.pdf
    使用pdf2txt.py将富有之谓大业.pdf 转换为html格式
    支持text文本、html、xml、tag格式
    
4、python pdf2txt.py -o b.html ../samples/nonfree/naacl06-shinyama.pdf
使用pdf2txt.py将pdf格式的论文naacl06-shinyama.pdf转换为html格式
pdf本质是二进制，
'''


from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter
from pdfminer.layout import *
from pdfminer.converter import PDFPageAggregator
from pdfminer.image import ImageWriter

# fp = open('富有之谓大业.pdf', 'rb')
# parser = PDFParser(fp)#来创建一个pdf文档分析器
# document = PDFDocument(parser)#创建一个PDF文档对象存储文档结构
# rsrcmgr=PDFResourceManager()# 创建一个PDF资源管理器对象来存储共享资源
#
# # 创建一个PDF设备对象  #基础 device=PDFDevice(rsrcmgr)
# device=PDFPageAggregator(rsrcmgr,laparams = LAParams())
# interpreter=PDFPageInterpreter(rsrcmgr,device)# 创建一个PDF解释器对象
# for page in PDFPage.create_pages(document):# PDFPage保存有关页的信息的对象。
#     interpreter.process_page(page)  #处理每一页
#     layout=device.get_result()
#     for x in layout:
#         print(x.get_text())



'''带有图片的Python办公自动化大全 - 样章.pdf如何提取文本？'''
# fp = open('Python办公自动化大全 - 样章.pdf', 'rb')
# fi = open('Python办公自动化大全 - 样章.txt','w')
# parser = PDFParser(fp)#来创建一个pdf文档分析器
# document = PDFDocument(parser)#创建一个PDF文档对象存储文档结构
# rsrcmgr=PDFResourceManager()# 创建一个PDF资源管理器对象来存储共享资源
#
# # 创建一个PDF设备对象  #基础 device=PDFDevice(rsrcmgr)
# device=PDFPageAggregator(rsrcmgr,laparams = LAParams())
# interpreter=PDFPageInterpreter(rsrcmgr,device)# 创建一个PDF解释器对象
# for page in PDFPage.create_pages(document):# PDFPage保存有关页的信息的对象。
#     interpreter.process_page(page)
#     # 接受该页面的LTPage对象
#     layout=device.get_result()
#     for x in layout:
#         if(isinstance(x,LTTextBoxHorizontal)):  #isinstance用于判断x是否是LTTextBoxHorizontal类创建的实例
#             fi.write(x.get_text())
# fp.close()
# fi.close()

'''所有可识别的pdf部分
LTPage :表示整个页。可能会含有LTTextBox，LTFigure，LTImage，LTRect，LTCurve和LTLine子对象。
LTTextBox:表示一组文本块可能包含在一个矩形区域。注意此box是由几何分析中创建，并且不一定表示该文本的一个逻辑边界。它包含LTTextLine对象的列表。使用 get_text（）方法返回文本内容。
LTTextLine :包含表示单个文本行LTChar对象的列表。字符对齐要么水平或垂直，取决于文本的写入模式。使用get_text（）方法返回文本内容。
LTAnno:在文本中字母实际上被表示为Unicode字符串。需要注意的是，虽然一个LTChar对象具有实际边界，LTAnno对象没有，因为这些是“虚拟”的字符，根据两个字符间的关系（例如，一个空格）由布局分析后插入。
LTImage:表示一个图像对象。嵌入式图像可以是JPEG或其它格式，但是目前PDFMiner没有放置太多精力在图形对象。
LTLine:代表一条直线。可用于分离文本或附图。
LTRect:表示矩形。可用于框架的另一图片或数字。
LTCurve:表示一个通用的Bezier曲线
'''


fp = open('Python办公自动化大全 - 样章.pdf', 'rb')
parser = PDFParser(fp)
document = PDFDocument(parser)
rsrcmgr=PDFResourceManager()
device=PDFPageAggregator(rsrcmgr,laparams = LAParams())
interpreter=PDFPageInterpreter(rsrcmgr,device)
for page in PDFPage.create_pages(document):
    interpreter.process_page(page)
    layout=device.get_result()
    for x in layout:
        def render(item):
            if isinstance(item, LTContainer):
                for child in item:
                    render(child)
            elif isinstance(item, LTText):
                print('LTText',end='')
            if isinstance(item, LTTextBox):
                print('LTTextBox')
            elif isinstance(item, LTImage):
                image_adr = './image'
                ImageWriter(image_adr).export_image(item)
                print('LTImage')
        render(x)
fp.close()




# import io
# from pdfminer.converter import  TextConverter
# from pdfminer.pdfinterp import PDFPageInterpreter,PDFResourceManager
# from pdfminer.pdfpage import PDFPage
#
# #ResourceManager有助于重用共享资源，如字体和图像，这样就不会多次分配大型对象。
# resource_manager = PDFResourceManager()
#
# f = io.StringIO()   #字符串的方式从内存中的文件读取数据
# converter = TextConverter(resource_manager,f)  #包含PDFdevice
# page_interpreter = PDFPageInterpreter(resource_manager,converter)
# fp = open('富有之谓大业.pdf','rb')
# for page in PDFPage.get_pages(fp,caching=True,check_extractable=True):
#     page_interpreter.process_page(page)
# text = f.getvalue()  #返回文件数据
# print(text)
# converter.close()
# f.close()
# fp.close()













