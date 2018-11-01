from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from myapp.models import User,Phone
from django.core.paginator import Paginator


def Main(request):
    return render(request,'main.html')

def signin(request):
    return render(request,'register.html')

def phoneTest(request,num):
    global p,pi
    p = Phone.objects.all()
    pi = Paginator(p,10)
    pageN = pi.num_pages
    pi2 = pi.page(num).object_list
    return render(request,'phone.html',{"phoneInfo":pi2,"pageN":pageN,"num":num})

def base(request):
    return render(request,'base.html')

def getmodel(request):                      #此处为ajax的方法
    manufacturer = request.POST['manufacturer'].lower()
    
    PList = [i.phoneMode for i in p if i.manufacturer==manufacturer]
    PDetail = [i.phoneDetail for i in p if i.manufacturer==manufacturer]
    Pprice = [i.phonePrice for i in p if i.manufacturer == manufacturer]
    PArea = [i.area for i in p if i.manufacturer == manufacturer]
    Pimg = [i.phoneImgUrl for i in p if i.manufacturer == manufacturer]
    Pgrade = [i.phoneGrade for i in p if i.manufacturer == manufacturer]

    return JsonResponse({"pl":PList,"pd":PDetail,"pp":Pprice,"pa":PArea,"pi":Pimg,"pg":Pgrade,"manufacturer":manufacturer})

def selectModel(request,model,num):
    global p
    p = Phone.objects.all()
    modelList = [i.manufacturer for i in p]
    if model.lower() in modelList:
        phoneInfo1 = p.filter(manufacturer=model.lower())
    else:
        phoneInfo1 = p

    pi = Paginator(phoneInfo1,10)
    PageNum = pi.num_pages
    phoneInfo = pi.page(num).object_list

    return render(request,'phone.html',{"phoneInfo":phoneInfo,"PageNum":PageNum,"num":num,"model":model})



def detail(request):

    return render(request,'detail.html')

def getdetail(requests):
    p = Phone.objects.all()
    model = requests.GET.get('model')
    pobj = p.get(phoneMode=model)
    price = pobj.phonePrice
    pimg = pobj.phoneImgUrl
    return render(requests,'detail.html',{"price":price,"pimg":pimg,"model":model})


#以下为支付宝需要的视图
from django.shortcuts import render, redirect, HttpResponse
from utils.pay import AliPay
import json
import time


def ali():
    # 商户app_id
    app_id = "2016092000557856" #复制来自支付宝生成的id
    # 服务器异步通知页面路径 需http: // 格式的完整路径，不能加?id = 123 这类自定义参数，必须外网可以正常访问
    # 发post请求
    notify_url = "http://127.0.0.1:8000/page2/"  #将这两个链接复制到支付宝中

    # 页面跳转同步通知页面路径 需http: // 格式的完整路径，不能加?id = 123 这类自定义参数，必须外网可以正常访问
    # 发get请求
    return_url = "http://127.0.0.1:8000/page2/"
    # 商户私钥路径
    merchant_private_key_path = "keys/pri"   #设置公钥和私钥的地址，文件上下两行begin和end是必须的，公钥就放在第二行。
    # 支付宝公钥路径
    alipay_public_key_path = "keys/pub"

    alipay = AliPay(
        appid=app_id,
        app_notify_url=notify_url,
        return_url=return_url,
        app_private_key_path=merchant_private_key_path,
        alipay_public_key_path=alipay_public_key_path,  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥
        debug=True,  # 默认False,
    )
    return alipay


def page1(request):
        money = float(request.POST.get('money'))
        alipay = ali()
        # 生成支付的url
        query_params = alipay.direct_pay(
            subject="铛铛商城商品支付",  # 商品简单描述
            out_trade_no="x2" + str(time.time()),  # 商户订单号
            total_amount=money,  # 交易金额(单位: 元 保留俩位小数)
        )
        pay_url = "https://openapi.alipaydev.com/gateway.do?{}".format(query_params)
        #支付宝网关链接，去掉dev就是生产环境了。
        return redirect(pay_url)


def page2(request):
    alipay = ali()
    if request.method == "POST":
        # 检测是否支付成功
        # 去请求体中获取所有返回的数据：状态/订单号
        from urllib.parse import parse_qs

        # request.body                  => 字节类型
        # request.body.decode('utf-8')  => 字符串类型

        body_str = request.body.decode('utf-8')
        post_data = parse_qs(body_str)
        # {k1:[v1,],k2:[v2,]}

        # {k1:v1}
        post_dict = {}
        for k, v in post_data.items():
            post_dict[k] = v[0]


        print(post_dict)

        sign = post_dict.pop('sign', None)

        status = alipay.verify(post_dict, sign)
        if status:
            print(post_dict['stade_status'])
            print(post_dict['out_trade_no'])

        return HttpResponse('POST返回')
    else:
        # QueryDict = {'k':[1],'k1':[11,22,3]}
        params = request.GET.dict()
        sign = params.pop('sign', None)
        status = alipay.verify(params, sign)
        print('GET验证', status)
        return render(request,'main.html')