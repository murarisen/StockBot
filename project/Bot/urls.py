from django.contrib import admin
from django.urls import path
from Bot import views


urlpatterns =[
    path("",views.index, name ='Bot'),
      path("index.html",views.index, name ='Bot'),
     
    path("about.html",views.about, name ='about'),
    path("base.html",views.market, name ='market'),
    path("News.html",views.contect, name ='news'),
    path("login.html",views.login, name ='login'),


]