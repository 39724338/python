print("热门综艺名称如下：\n")
art = ["向往的生活","歌手","中国好声音","巧手神探","欢乐喜剧人","笑傲江湖","王牌对王牌","奔跑吧","吐槽大会","奇葩说"]
for index,item in enumerate(art):
    if index%2 == 0:                       # 判断是否为偶数，为偶数时不换行
        print(item +"\t\t", end='')
    else:
        print(item + "\n")                   # 换行输出
