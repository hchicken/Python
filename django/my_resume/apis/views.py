from django.shortcuts import render,HttpResponse,redirect,reverse
from django.http import HttpResponseRedirect
from app01.models import Resume
from django.http import JsonResponse
from io import BytesIO
from libs import verifications,email_code
import base64
from django.core.cache import cache

# Create your views here.


def get_add(request,add_num):
    #获取ID
    id = int(request.POST.get('id'))
    try:
        resume_id = Resume.objects.get(id=id)
    except:
        print("报错")
    resume_down = int(resume_id.add_num)
    resume_down +=1
    resume_down=str(resume_down)
    resume_id.save()



#ajax动态加载下载次数
def get_down(request):
    id = int(request.POST.get('id'))
    try:
        resume_id = Resume.objects.get(id=id)
    except:
        print("报错")
    print(f"{resume_id.resume_down}")
    resume_down = int(resume_id.resume_down)
    resume_down +=1
    resume_down=str(resume_down)
    resume_id.resume_down = resume_down
    resume_id.save()

    ret ={
        "code":200,
    }
    return JsonResponse(ret)



#
def login_request(fun):
    # print("denglu")
    def _login(request):
        # print("denglu1")
        if request.session.get("user"):
            # print("denglu2")
            result = fun(request)
            print(result)
            return result
        else:
            print("tan")
            kwgs={
                "url":reverse('login')
            }
            return  JsonResponse(kwgs)
    return _login



@login_request
def get_collect(request):
    id = int(request.POST.get('id'))
    # print(id,type(id))
    try:
        resume_id = Resume.objects.get(id=id)
    except:
        print("报错")
    # print(f"{resume_id.resume_down}")
    resume_browse = int(resume_id.resume_browse)
    resume_browse +=1
    resume_browse = str(resume_browse)
    resume_id.resume_browse = resume_browse
    resume_id.save()

    ret ={
        "code":200,
    }
    return JsonResponse(ret)


def get_captcha(request):
    # 直接在内存开辟一点空间存放临时生成的图片
    f = BytesIO()
    # 调用check_code生成照片和验证码
    img, code = verifications.create_validate_code()
    # 将验证码存在服务器的session中，用于校验
    request.session['captcha_code'] = code
    # 生成的图片放置于开辟的内存中
    img.save(f, 'PNG')
    # 将内存的数据读取出来，并以HttpResponse返回
    # return HttpResponse(f.getvalue())
    ret_type = "data:image/jpg;base64,".encode()
    ret = ret_type + base64.encodebytes(f.getvalue())
    del f
    # print(ret)
    return HttpResponse(ret)

#对验证码进行校验
def check_captcha(request):
    ret = {"code": 400, "msg": "验证码错误！"}
    post_captcha_code = request.GET.get('captcha_code')
    session_captcha_code = request.session.get('captcha_code',"a")
    # print(post_captcha_code, session_captcha_code)
    if post_captcha_code.lower() == session_captcha_code.lower():
        ret = {"code": 200, "msg": "验证码正确"}
    return JsonResponse(ret)


def get_code(request):
    #邮件获取验证码
    my_code = email_code.random_num()
    my_email = request.POST.get("my_code")
    # print(my_email)
    ret = email_code.email_send(my_email,my_code)
    # 将短信验证码写入redis
    cache.set(my_email, my_code, 300)
    if ret:
        result = "发送成功"
    else:
        result = "发送失败"

    kwgs={
        "result":result
    }
    return JsonResponse(kwgs)