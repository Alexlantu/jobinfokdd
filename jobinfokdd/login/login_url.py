from django.conf.urls import include, url
from django.contrib import admin
from . import views


urlpatterns = [
    # Examples:
    # url(r'^$', 'jobinfokdd.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'company/',views.do_app),

]
