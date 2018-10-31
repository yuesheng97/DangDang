import requests
from lxml import etree
import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DangDang.settings")# project_name 项目名称
django.setup()
from myapp.models import Phone

Area = "湖北武汉"
Detail = "智能手机具有优秀的操作系统、可自由安装各类软件（仅安卓系统）、完全大屏的全触屏式操作感这三大特性，其中Google(谷歌)、苹果、三星、诺基亚、HTC（宏达电） 这五大品牌在全世界最广为皆知"

url1  = "http://detail.zol.com.cn/cell_phone_index/subcate57_0_list_2000_0_8_1_0_1.html"
url2 = "http://detail.zol.com.cn/cell_phone_index/subcate57_0_list_3000_0_8_1_0_1.html"
url3 = "http://detail.zol.com.cn/cell_phone_index/subcate57_0_list_4000_0_8_1_0_1.html"
urlList = [url1,url2,url3]
n=1001

for url in urlList:
    response = requests.get(url=url)
    html = etree.HTML(response.text)
    phoneImg = html.xpath('//div[@class="list-box"]//div[@class="pic-box SP"]/a/img/attribute::src')
    phoneName = html.xpath('//div[@class="list-box"]//div[@class="pro-intro"]/h3/a/text()')
    phonePrice = html.xpath('//div[@class="list-box"]//div[@class="price-box"]/span/b[position()=2]/text()')

    li = ['OPPO', 'vivo', '华为', '三星', '荣耀', '一加', '苹果', '金立', '魅族', '中兴', 'Moto', '努比亚', '锤子'
                            , '小米', '夏普', '美图', '诺基亚', 'HTC', '黑莓', '海信', 'AGM', '索尼', '谷歌', 'LG']
    for i in phoneName:
        for j in li :
            if j.lower() in i or j.upper() in i:
                index = phoneName.index(i)
                mannufacture = j.lower()
                p = Phone(phoneId=n,phoneMode=phoneName[index],phonePrice=phonePrice[index],phoneDetail=Detail
                          ,phoneImgUrl=phoneImg[index],manufacturer=mannufacture,area=Area)
                n+=1
                p.save()




