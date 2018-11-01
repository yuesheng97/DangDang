 $(document).ready(function () {
        $("#rg_count").blur(function () {
            nickname=document.getElementById("rg_count").value;
            sty1=document.getElementById("count_verify");

            $.ajax({
                type:'post',
                data:{"nickname":nickname},
                dataType:"json",
                url:"/ftapp/getname/",
                success:function (result) {
                    result1=result["status"];
                    if(result1=="0"){
                        sty1.style.color="red";
                        sty1.innerHTML="用户名格式不正确";
                        sty1.style.left="27px";
                        document.getElementById("count_error").style.display="block"
                    }
                    else if (result1=="3"){
                        sty1.style.color="#00FF00";
                        sty1.innerHTML="用户名可用";
                        sty1.style.left="27px";
                        document.getElementById("count_right").style.display="block"
                    }


                }
            })
        });
     $("#rg_password").blur(function () {
        var password=document.getElementById("rg_password").value;
         style1=document.getElementById("password_verify");

             $.ajax({
                 data:{"password":password},
                 dataType:"json",
                 method:"post",
                 url:"/ftapp/getpwd/",
                 success:function (result) {
                     var info = result['status'];
                     if (info == "0") {
                         style1.style.color="red";
                         style1.innerHTML= "密码格式不对,请重新输入";
                         style1.style.left="27px";
                         document.getElementById("password_error").style.display="block"
                     }
                     if (info == "1") {
                         style1.style.color = "#00FF00";
                         style1.innerHTML= "密码格式正确";
                         style1.style.left="27px";
                         document.getElementById("password_right").style.display="block"
                     }
                 }
             })
     });
     //此处写别的监听事件
    $("#rg_num").blur(function () {

        $.ajax({
            type:"post",
            datatype:"json",
            url:"/ftapp/getnum/",
            data:{"rg_num":document.getElementById("rg_num").value},
            success:function (result) {
                numstatus=result["status"];
                if(numstatus=="0"){
                    num_util("197px","#FF0000","您输入手机号格式不正确","block","none")
                }
                else  if (numstatus=="2"){
                    num_util("170px","#3487FF","","none","none","none")
                }else if (numstatus=="3"){
                    num_util("197px","#FF0000","此手机号已被注册","block","none")
                }
                else {
                    num_util("197px","#00FF00","此手机号可用","none","block")
                }
            }

        })
    });
     function num_util(interval,color,inner,errordisplay,rightdisplay) {
         document.getElementById("num_verify").style.left=interval;
                    document.getElementById("num_verify").style.color=color;
                    document.getElementById("num_verify").innerHTML=inner;
                    document.getElementById("num_error").style.display=errordisplay;
                    document.getElementById("num_right").style.display=rightdisplay;
     }
     $("#register").click(function () {
          count1 =document.getElementById("rg_count").value;
          password2=document.getElementById("rg_password").value;
          num1=document.getElementById("rg_num").value;
         $.ajax({
             url:"/ftapp/submit/",
             method:"post",
             data:{"count":count1,"password":password2,"num":num1},
             dataType:"json",
             success:function (response) {
                 var status = response['status'];
                 if (status=="0"){
                     document.getElementById("info").style.display="block"
                 }else{
                     document.getElementById("success").style.display="block";
                     countdown1()
                 }
             }
         })
     })

});
