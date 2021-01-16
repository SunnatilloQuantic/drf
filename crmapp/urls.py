from django.urls import path
from .import views

urlpatterns = [
    path('list/', views.eventList, name = 'list'),
    path('detail/<str:pk>/', views.eventDetail, name = 'deatail'),
    path('create/', views.eventCreate, name = 'create'),
    path('update/<str:pk>/', views.eventUpdate, name = 'update'),
    path('delete/<str:pk>/',views.eventDelete, name = 'delete'),
]