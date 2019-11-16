from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^get_down/$',views.get_down,name="get_down"),
    url(r'get_collect/$',views.get_collect,name='get_collect'),
    url(r"^get_captcha/$",views.get_captcha,name="get_captcha"),
    url(r"^check_captcha/$", views.check_captcha, name="check_captcha"),
    url(r"^get_code/$",views.get_code,name="get_code")
]