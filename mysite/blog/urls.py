from . import views
from django.urls import path

urlpatterns = [

    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('', views.PostList.as_view(), name='home'),
    # path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]
