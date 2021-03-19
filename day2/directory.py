'''
info = {
    'stu01':"TengLan Wu",
    'stu02':"LongZe Luola",
    'stu03':"XiaoZe MALIYA"
}
print(info)
print(info.get('stu05'))    #安全取值
print('stu01' in info)      #判断值是否在字典中，布尔
'''


'''
info['stu01'] = '武藤兰'   #修改
info['stu04'] = 'Cang Jingkong'     #添加
# del info['stu02']   #删除
# info.pop('stu02')     #删除
info.popitem()      #删除
print(info)
'''




av_catalog = {
    "欧美":{
        "www.youporn.com":["很多免费的,世界最大的","质量一般"],
        "www. pornhub.com":["很多免费的,也很大", "质量比yourporn高点"],
        "letmedothistoyou.com":["多是自拍,高质量图片很多","资源不多,更新慢"],
        "x-art.com" :["质量很高,真的很高”,”全部收费,属比请绕过"]
    },
    "日韩":{
        "tokyo- hot":["质量怎样不清楚,个人已经不喜欢日韩范了", "听说是收费的"]
    },
    "大陆":{
        "1024":["全部免费,真好，好人- -生平安","服务器在国外,慢"]
    }
}
av_catalog["大陆"]["1024"][1] = '国内可以做镜像'

#print(av_catalog.setdefault("大陆",{'www.baidu.com':[1,2]}))  #如果key存在，返回已有的值。否则添加指定值


print(av_catalog)



