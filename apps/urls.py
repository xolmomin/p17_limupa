from django.urls import path

from apps.views import index_page, login_page, register_page, blog_detail_page, logout_page,blog_list_page

urlpatterns = [
    path('', index_page, name='index_page'),
    path('blog-list', blog_list_page, name='blog_list_page'),
    path('blog-detail/<int:pk>', blog_detail_page, name='blog_detail_page'),
    path('logout', logout_page, name='logout_page'),
    path('login', login_page, name='login_page'),
    path('register', register_page, name='register_page')
]
