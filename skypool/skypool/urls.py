"""skypool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from frontend import views as front_views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', front_views.HomeView.as_view(), name="home-page"),
    url(r'^home/$', front_views.HomeView.as_view(), name="home-page"),
    url(r'^activities/index/$', front_views.NewsIndexView.as_view(), name="news-index"),
    url(r'^activities/(\d+)/$', front_views.NewsShowView.as_view(), name="news-show"),
    url(r'^brand/(\d+)/$', front_views.BrandShowView.as_view(), name="brand-show"),
    url(r'^articles/(\d+)/$', front_views.ArticlesShowView.as_view(), name="article-show"),
]
