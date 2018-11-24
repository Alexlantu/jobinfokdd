from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
from login import views as tv
from login import login_url

urlpatterns = [
    # Examples:
    # url(r'^$', 'jobinfokdd.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'',TemplateView.as_view(template_name="index.html")),

    url(r'^normalmap/',tv.do_normalmap),
    url(r'^withparam/(?P<year>[0-9]{4})/(?P<month>[0,1][0-9])',tv.withparam),

    # 约定凡是以login开头的url都以login开头
    url(r'^login/',include(login_url)),
    # 嵌套参数的应用。?:表示后面的内容忽略;\d+表示至少有一个数字
    url(r'^book/(?:page-(?P<pn>\d+)/)$', tv.do_param2),

    # 传递一个额外的参数
    url(r'^yourname/', tv.extremParam, {"name" : "Alex"}),

    # url反向解析
    url(r'^yourname1/$', tv.revParse, name="askname"),

    # url重定向
    url(r'^cdx/',tv.do_cdx,name="cdx"),
    url(r'^cdx1',tv.do_cdx1,name="cdx1"),

    url(r'^v8/',tv.v8_get),

    url(r'^v9_get',tv.v9_get),
    url(r'^v9_post',tv.v9_post),

    url(r'^render_test',tv.render_test),
    url(r'^render_test2',tv.render_test2),
]
