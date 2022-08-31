"""djshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve

# 引入模块的views接口
from user import views as user_views
from goods import views as goods_views
from cart import views as cart_views
from order import views as order_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # 会从这个接口获取到 图片信息。后面是serve的参数，匹配后访问的路径，使用相对路径
    re_path(r'^upload/(?P<path>.*)$', serve, {'document_root': 'upload/'}),
    # 添加路由，并且绑定到对应的api接口上
    path('signin/', user_views.signin),
    # 添加路由，并且绑定到对应的api接口上
    path('search/', goods_views.search),
    # 添加路由，并且绑定到对应的api接口上
    path('home/ad/', goods_views.index),
    # 添加路由，并且绑定到对应的api接口上
    path('home/hot/', goods_views.hot),
    # 添加路由，并且绑定到对应的api接口上
    path('detail/', goods_views.detail),
    # 添加路由，并且绑定到对应的api接口上
    path('cart/get/', cart_views.get),
    # 添加路由，并且绑定到对应的api接口上
    path('cart/delete/', cart_views.delete),
    # 添加路由，并且绑定到对应的api接口上
    path('cart/add/', cart_views.add),
    # 添加路由，并且绑定到对应的api接口上
    path('order/list/', order_views.list),
    # 添加路由，并且绑定到对应的api接口上
    path('order/add/', order_views.add),
    # 添加路由，并且绑定到对应的api接口上
    path('order/pay/', order_views.pay),
    # 添加路由，并且绑定到对应的api接口上
    path('signup/', user_views.signup),
    # 添加路由，并且绑定到对应的api接口上
    path('delete/', user_views.delete),
    # 添加路由，并且绑定到对应的api接口上
    path('remove/', user_views.remove),
]
