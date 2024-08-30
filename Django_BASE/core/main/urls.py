from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home,name='cat'),
    path('prod/<int:id>/',views.Info,name='prod')
]