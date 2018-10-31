import requests
from lxml import etree
import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DangDang.settings")# project_name 项目名称
django.setup()
from  myapp.models import College
url = "http://detail.zol.com.cn/cell_phone_index/subcate57_0_list_3000_0_1_1_0_1.html"
html = requests.get(url=url)
html.encoding ="gbk"

html2 = etree.HTML(html.text)
info = html2.xpath('//div[@id="J_ManuFilter"]/div/a/text()')
info2 = html2.xpath('//div[@id="J_ParamPrice"]/a[position()>1]/text()')
info3 = html2.xpath('//div[@id="J_ParamItem4"]/a/text()')
print(info)
print(info2)
print(info3)



