from django.shortcuts import render, HttpResponse, render_to_response, redirect
from django.urls import reverse
from .models import Resume, Username, Type
from django.core.paginator import Paginator
from django.db.models import F
from django.views.generic import View
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from django.core.cache import cache


# Create your views here.


# 写一个函数用来验证第一个参数,返回符合要求的数据
# request是请求，sort_resume
# sort_resume 死用来获取HTML sort_resume 的值
# resumes_all 获取所有的数据
def _sort(request, sort_resume, resumes_all):
    # 这里得到的是一个参数
    sort_resumes = request.GET.get(f"{sort_resume}")
    if sort_resumes:
        pass
    else:
        sort_resumes = "synthesize"

    # 按照综合排序
    if sort_resumes == "synthesize":
        # print("synthesize")
        resumes_com = resumes_all.order_by(0 - F('resume_browse') - F('resume_down') / 2)
    # 按照下载量排序
    elif sort_resumes == "hot":
        # print("hot")
        resumes_com = resumes_all.order_by(0 - F('resume_down'))
    # 按照时间排序
    elif sort_resumes == "srecently":
        # print("srecently")
        resumes_com = resumes_all.order_by('-resume_onlinetime')

    return resumes_com, sort_resumes


# 这里来个分页的代码
# request为请求
# resumes_all为满足要求后的所有数据
def _page(request, resumes_all):
    # 这是分页，已12为一页
    paginator = Paginator(resumes_all, per_page=12)
    # print(f"打印的是多少页的内存地址{index_paginator}")
    # 设置第几页
    page = 1
    # 这里是获取页数
    page_str = request.GET.get("page")
    # print(f"打印第几页的数{index_page}")
    if page_str and page_str.isdigit():
        page = eval(page_str)
    # print(f"打印出page的值{page}")

    # 这里设置第page页的数据
    # page_data = paginator.page(page)
    # print(f"这是第{page}页的数据{index_resumes}")


    # 返回值是一个字典：paginator 所有数据的地址
    # print(paginator)
    # page_date当页数据
    # page当前页面
    dict_page = {
        "paginator": paginator,
        "page": page,
    }
    return dict_page


def index(request):
    # 获取

    # sort_resumes = request.GET.get("sort_resumes")
    #
    # if sort_resumes:
    #     pass
    # else:
    #     sort_resumes = "synthesize"
    #
    resumes_all = Resume.objects.all()
    # if sort_resumes == "synthesize":
    #     # print("synthesize")
    # #这里是查出所有的模板
    #     resumes_com = resumes_all.order_by(0 - F('resume_browse')- F('resume_down'))
    # elif sort_resumes == "hot":
    #     # print("hot")
    #     resumes_com = resumes_all.order_by(0-F('resume_down'))
    # elif sort_resumes =="srecently":
    #     # print("srecently")
    #     resumes_com = resumes_all.order_by('-resume_onlinetime')

    resumes_com, sort_resumes = _sort(request, 'sort_resumes', resumes_all)

    # 获取的一个字段，里面包括分页的地址，和返回的第几页
    dict_page = _page(request, resumes_com)
    # print(dict_page["page_data"])

    # print(resumes_com)
    # print(resumes_com)
    # 这是分页，已12为一页
    # index_paginator = Paginator(resumes_com,per_page=4)
    # # print(f"打印的是多少页的内存地址{index_paginator}")
    # #设置第几页
    # page = 1
    # #这里是获取页数
    # index_page = request.GET.get("page")
    # # print(f"打印第几页的数{index_page}")
    # if index_page and index_page.isdigit():
    #     page = eval(index_page)
    # # print(f"打印出page的值{page}")
    #
    # #这里设置第page页的数据
    # index_resumes = index_paginator.page(page)
    # # print(f"这是第{page}页的数据{index_resumes}")
    # max_page = index_paginator.num_pages

    kwgs = {
        # 当前页面的排标签
        "sort_resumes": sort_resumes,
        # 总页数
        "max_page": dict_page["paginator"].num_pages,
        # 当前页数
        "page": dict_page["page"],
        # 当前页面的数据
        "resumes_com": dict_page["paginator"].page(dict_page["page"]),
        # 全部数据
        "index_paginator": dict_page["paginator"],
    }

    return render(request, "index.html", kwgs)


def type(request, id):
    # 这是模板类型的id
    # print(id)
    tag_id = id
    # print(tag_id)
    my_type = Type.objects.get(id=id)
    # 获取该类型简历
    resumes_all = my_type.resume_set.all()

    resumes_com, sort_resumes = _sort(request, 'sort_resumes', resumes_all)

    dict_page = _page(request, resumes_com)

    kwags = {
        # 当前分类的数据
        "sort_resumes": sort_resumes,
        # 总页数
        'max_page': dict_page["paginator"].num_pages,
        # 当前页数
        'page': dict_page["page"],
        # 但前页面的数据
        "resumes_com": dict_page["paginator"].page(dict_page["page"]),
        # 类型的ID
        'tag_id': tag_id,
    }
    return render(request, "tag.html", kwags)


def _login(request, username, passwd):
    ret = True
    try:
        user = Username.objects.filter(username__exact=username).values()[0]
        # print(user)
        if user:
            # print(passwd, user['passwd'])
            if check_password(passwd, user['passwd']):
                # 1.生成随机的sessionID字符串
                # 2.将sessionID和用户的信息在数据库中保存为一个键值对
                # 3.通过cookie将sessionID保存在客户端上
                # 这时候通过用户再次向服务器发送请求时服务器就可以通过请求中的sessionID判断用户的信息了，从而达到保存登录状态的要求。
                request.session['user'] = user
            else:
                ret = False
                messages.add_message(request, messages.INFO, "用户登录失败")
        else:
            messages.add_message(request, messages.INFO, "用户不存在")
            ret = False
    except:
        ret = False
    return ret


class login(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        ret = False
        # 获取验证码：
        # 从前端获取验证码
        captcha_inp = request.POST.get("captcha_inp")
        # 从session获取验证码
        session_captcha_code = request.session.get('captcha_code', "a")
        # print(captcha_inp.lower(),session_captcha_code)
        # 从前端获取账号密码
        if captcha_inp.lower() == session_captcha_code.lower():
            username = request.POST.get("username")
            passwd = request.POST.get("passwd")
            # print(username, passwd)
            # 对账号密码进行验证
            ret = _login(request, username, passwd)
        # print(ret)
        # 验证成功跳转到主页
        if ret:
            return redirect(reverse('index'))
        return render(request, "login.html")


class reg(View):
    def get(self, request):
        return render(request, "reg.html")

    def post(self, request):
        # 获取所有的账号密码
        username = request.POST.get("username")
        email = request.POST.get("email")
        my_code = request.POST.get("my_code")
        passwd1 = request.POST.get("passwd1")
        passwd2 = request.POST.get("passwd2")
        print(username, email, my_code, passwd1, passwd2)
        if cache.get(email):
            if my_code.lower() == cache.get(email).lower() and passwd1 == passwd2:
                try:
                    user = Username.objects.filter(username=username).values()[0]
                    result = f"{username}已经注册"
                    # print(user)
                except:
                    try:
                        email = Username.objects.filter(email=email).values()[0]
                        result = f"{email}已经注册"
                        # print("email已经注册")
                    except:
                        user_add = Username.objects.get_or_create(username=username, email=email,passwd=make_password(passwd1))
                        print(user_add)
                        _login(request, username, passwd1)
                        return redirect(reverse('index'))
                        #     print("email没有注册")
                        # print("用户不存在")

            else:
                result = "验证码不对或者2次密码输入不一样"
                # print("验证码不对或者2次密码输入不一样")
        else:
            result = '验证码过期'
            # print("验证码过期")

        # ret = _login(request,username,passwd)
        # print(ret)
        # if ret:
        #     return redirect(reverse('index'))
        return render(request, "reg.html",{"result":result})


def logout(request):
    # auth_logout(request)
    del request.session["user"]
    return redirect(reverse("index"))


def search(request):
    return HttpResponse("该功能正在完善中……")
