from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.post_list , name='post_list'),
    path('about/', views.About_info, name='about'),
    path('post/<int:pk>/', views.post_view, name='post'),
    path('artwork/<int:pk>/', views.artwork_view, name='artwork'),
]

urlpatterns += staticfiles_urlpatterns()
