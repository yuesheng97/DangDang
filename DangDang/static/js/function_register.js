function showArea(){
	var i=document.getElementById("areaCode").style;
	var j=document.getElementById("listicon").style;
	if(i.display=="none"){
		i.display="block";
		j.transform="rotate(180deg)"
	}else{
		i.display="none";
		j.transform="rotate(360deg)"
	}
	var m = document.getElementById("areaNum");
	m.style.color="#000"
//	alert(i.display)
}
function cn(){
	document.getElementById('areaNum').value='+86';
	showArea()
}
function hongkong(){
	document.getElementById('areaNum').value='+852';
	showArea()
}
function macao(){
	document.getElementById('areaNum').value='+853';
	showArea()
}
function formosa(){
	document.getElementById('areaNum').value='+886';
	showArea()
}
function count(){
	document.getElementById("count_verify").style.left="0px";
	document.getElementById("count_error").style.display="none";
	document.getElementById("count_right").style.display="none";
	document.getElementById("rg_count").value="";
	var m = document.getElementById("rg_count");
	m.style.color="#000";
	document.getElementById("count_verify").innerHTML="*请输入2-4位中文用户名";
	var style1=document.getElementById("count_verify");
    style1.style.color="#3478FF"
}
function count2(){
	var count=document.getElementById("rg_count").value;

//	alert(i)
// 	document.getElementById("count_verify").innerText=""
	if(count==""){
//		alert("空")
		document.getElementById("rg_count").value="昵称";
        var m = document.getElementById("rg_count");
		m.style.color="#aaa"
	}
		document.getElementById("count_verify").innerHTML=""

}
function password1(){
	document.getElementById("password_verify").style.left="0px";
	document.getElementById("rg_password_bot").value="";
	document.getElementById("password_right").style.display="none";
	document.getElementById("password_error").style.display="none";
    var m = document.getElementById("rg_password");
	m.style.color="#000";
	document.getElementById("password_verify").innerHTML="*请输入6-12位密码,包含字母、数字、下划线"
    var n = document.getElementById("password_verify");
    n.style.color="#3487FF"

}
function password2(){
	document.getElementById("password_verify").style.left="0px";
	document.getElementById("password_right").style.display="none";
	document.getElementById("password_error").style.display="none";

var count=document.getElementById("rg_password").value;

//	alert(i)
	if(count==""){
		document.getElementById("rg_password_bot").value="密码"
	}
		document.getElementById("password_verify").innerHTML=""

	}

function rg_num1(){
	document.getElementById("num_verify").style.left="170px";
	document.getElementById("num_verify").style.color="#3487FF";
    document.getElementById("num_error").style.display="none";
	document.getElementById("num_right").style.display="none";
	document.getElementById("rg_num").value="";
    var m = document.getElementById("rg_num");
	m.style.color="#000";
	document.getElementById("num_verify").innerHTML="*请输入11位手机号,用于绑定用户"


}
function rg_num2(){

	if(document.getElementById("rg_num").value==""){

		document.getElementById("rg_num").value="手机号";
        var m = document.getElementById("rg_num");
		m.style.color="#aaa"
	}
	document.getElementById("num_verify").innerHTML=""

}

function checktreaty1() {
    var i=document.getElementById("gird");

    if(document.getElementById("gird").innerHTML==""){
        document.getElementById("gird").innerHTML='<img src="/static/rg_imgs/对勾.png" width="30px" style="margin-left: -3px;margin-top: -10px;">'
    }else{
            document.getElementById("gird").innerHTML=""
        }
}
seconddown=3;
function countdown1(){
	document.getElementById("second").innerHTML=seconddown;
	seconddown-=1;
	var s1=setTimeout("countdown1()",1000);
	if(seconddown<=0){
		clearTimeout(s1);
		location.replace('/ftapp/Main/')
	}

}
//下方为轮播图
 n=1;
m=0.3;
p=1;
index=3;
function t1(){

    n-=0.01;
    var i = document.getElementById('i2');
    i.style.opacity=n;
    ss1=setTimeout("t1()",60);
    if(n<=0.5){
        index+=1;
        t2();
        clearTimeout(ss1)
    }

}
function t2(){
    n+=0.01;
    var j = document.getElementById('i1');
    j.style.opacity=n;
    j.style.zIndex=index;
    ss2=setTimeout("t2()",60);
    if(n>=1){
        clearTimeout(ss2);
        index+=1;
        t3()
    }
}
function t3(){
    var i = document.getElementById("i1");
    n-=0.01;
    i.style.opacity=n;
    i.style.zIndex=index;
    ss3=setTimeout('t3()',60);
    if(n<=0.5){
        clearTimeout(ss3);
        index+=1;
        t4()
    }
}
function t4(){
    var i = document.getElementById("i2");
    n+=0.01;
    i.style.opacity=n;
    i.style.zIndex=index;
    ss4=setTimeout("t4()",60);
    if(n>=1){
        clearTimeout(ss4);
        t1()
    }
}