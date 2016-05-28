"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
import social.apps.django_app.urls
import paypal.standard.ipn.urls
import shop.views

urlpatterns = [
    url(r'^$', shop.views.main_page, name='main_page'),
    url(r'^reg/$', shop.views.reg_page, name='reg_page'),
    url(r'^passrecovery/$', shop.views.passrecovery_page, name='passrecovery_page'),
    url(r'^bag/$', shop.views.bag_page, name='bag_page'),
    url(r'^book/(?P<book_id>[0-9]+)$', shop.views.book_page, name='book_page'),
    url(r'^genre/(?P<genre>[0-9]+)$', shop.views.genre_page, name='genre_page'),
    url(r'^addtobag/$', shop.views.addtobag, name='addtobag'),

    url('', include(social.apps.django_app.urls, namespace='social')),
    url(r'^accounts/logout/$', shop.views.account_logout, name='logout'),
	url(r'^accounts/login/$', shop.views.account_login, name='login'),
	url(r'^accounts/profile/$', shop.views.account_profile, name='profile'),

	url(r'^payment/cart/$', shop.views.paypal_pay, name='cart'),
	url(r'^payment/success/$', shop.views.paypal_success, name='success'),
	url(r'^paypal/', include(paypal.standard.ipn.urls)),

    url(r'^admin/', admin.site.urls),
]
