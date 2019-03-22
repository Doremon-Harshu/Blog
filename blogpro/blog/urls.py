from django.urls import path
from . import views

urlpatterns = [
    # path('',views.base,name='base'),
    path('about/', views.about, name='about'),
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('blog1/', views.blog1, name='blog1'),
    path('blog1/', views.blog2, name='blog2'),
    path('reg/', views.reg, name='reg')

]
