from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.post_list, name='list'),
    path('create/', views.post_create),
    path('<id>/', views.post_details, name='details'),
    path('<id>/edit/', views.post_update, name='update'),
    path('<id>/delete/', views.post_delete, name='delete'),
]