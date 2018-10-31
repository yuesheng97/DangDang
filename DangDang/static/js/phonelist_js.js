character = new Array('全面屏', '大屏幕', '大容量电池', '拍照手机', '自拍手机', '双卡双待', '2K屏',
							'面部识别', '指纹识别', '双屏手机', '游戏手机')
model = new Array('OPPO', 'vivo', '华为', '三星', '荣耀', '一加', '苹果', '金立', '魅族', '中兴', 'Moto', '努比亚', '锤子'
                        , '小米', '夏普', '美图', '诺基亚', 'HTC', '黑莓', '海信', 'AGM', '索尼', '谷歌', 'LG')
price = new Array('500元以下', '500-1000元', '1000-1500元', '1500-2000元', '2000-3000元', '3000-4000元', '4000-5000元', '5000元以上')
n="";
m="";
p="";


function func(){
    for(var i=0;i<character.length;i++){
        m += "<li><a>"+character[i]+"</a></li>"
    }
document.getElementById("u3").innerHTML=m
}
function func1(){
    for(var i=0;i<model.length;i++){
    n+= "<li onclick=\"nate(this)\"><a >"+model[i]+"</a></li>"
}
    document.getElementById("u1").innerHTML=n
}
function func2(){
    for(var i=0;i<price.length;i++){
    p+= "<li><a >"+price[i]+"</a></li>"
}
    document.getElementById("u2").innerHTML=p
}
 function lastPage() {
    var page = document.getElementById("pageNum").value;
    var model = document.getElementById("UrlModel").value;
    if (page<=1){
        alert("已经是最后一页啦")
    }else{
    var nowPage = parseInt(page)-1;
    document.getElementById("pageNum").value=nowPage;
    location.replace("/myapp/phone/"+model+"/"+nowPage)
    }

}
function nextPage() {
    var grossPages = document.getElementById("grossPages").value;

    var page = document.getElementById("pageNum").value;
    var model = document.getElementById("UrlModel").value;
    if (page>=parseInt(grossPages)){
        alert("已经是最后一页啦")
    }else{
    var nowPage = 1+parseInt(page);
    document.getElementById("pageNum").value=nowPage;
    location.replace("/myapp/phone/"+model+"/"+nowPage)
    }

}