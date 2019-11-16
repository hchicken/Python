"""my_resume URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from app01 import views as app01_views
from my_resume import settings
from django.views.static import serve
from app01 import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',app01_views.index,name="index"),
    url(r'^login/$',views.login.as_view(),name='login'),
    url(r"^reg/$", views.reg.as_view(), name='reg'),
    url(r"^logout/$", views.logout, name='logout'),
    url(r'^tag/(\d+)/$',app01_views.type,name='tag'),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^apis/',include('apis.urls',namespace='apis')),
    url(r'^search/$',app01_views.search,name='search'),

]
