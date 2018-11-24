from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import loader
# Create your views here.

def do_normalmap(request):
    return HttpResponse("This is normalmap")
def withparam(request, year, month):
    return HttpResponse("This is with param {0},{1}".format(year, month))

def do_app(request):
    return HttpResponse("这是一个子路由")

def do_param2(r, pn):
    return HttpResponse("The page number is {0}".format(pn))

def extremParam(r, name):
    return HttpResponse("My name is {0}".format(name))

def revParse(r):
    return HttpResponse("your URL is {0}".format(reverse('askname')))

def do_cdx(request):
    return HttpResponseRedirect(reverse('cdx1'))

def do_cdx1(request):
    return HttpResponse("这是重定向的页面！当前的URL为{0}",format(reverse('cdx1')))

def v8_get(request):
    rst = ""
    for k, v in request.GET.items():
        rst += k + "->" +v
        rst += ","
    return HttpResponse("Get value of request is {0}".format(rst))

def v9_get(request):
    # 渲染并返回
    return render_to_response("for_post.html")

def v9_post(request):
    rst = ""
    for k, v in request.POST.items():
        rst += k + "->" + v
        rst += ","
    print("this is my"+ rst)
    return HttpResponse("Post value of request is {0}".format(rst))

def render_test(request):
    c = dict()
    # 环境变量，作用是将变量传到模板里
    c["name"] = "Alex"
    rsp = render(request, "render.html", context=c)
    return rsp

def render_test2(request):
    t = loader.get_template("render.html")
    r =t.render({"name":"Alex"})
    return HttpResponse(r)
